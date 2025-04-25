from flask import Flask, render_template, request, url_for, redirect, session
from models.models import *
from flask import current_app as app
from datetime import datetime,date
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/home", methods=["GET", "POST"])
def home1():
    if request.method == "POST":
        return render_template("user_login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uemail = request.form.get("email")
        upassword = request.form.get("password")
        user = user_info.query.filter_by(email=uemail, password=upassword).first()
        if user and user.role == 0:
            session["user_id"] = user.id
            return redirect(url_for("admin_dashboard", name=user.name))
        elif user and user.role == 1:
            session["user_id"] = user.id
            return redirect(url_for("user_dashboard", name=user.name))
        else:
            return render_template("user_login.html", mssg="Invalid Credentials")
    return render_template("user_login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form.get("user_name")
        uemail = request.form.get("email")
        upassword = request.form.get("password")
        uqualification = request.form.get("qualification")
        udob = request.form.get("dob")
        user = user_info.query.filter_by(email=uemail).first()
        if user:
            return render_template("user_registration.html", mssg="User already exists")
        new_user = user_info(name=uname,email=uemail,password=upassword,qualification=uqualification,dob=udob)
        db.session.add(new_user)
        db.session.commit()
        return render_template("user_login.html", mssg="Registration Successful")
    return render_template("user_registration.html")


@app.route("/admin/<name>")
@login_required
def admin_dashboard(name):
    subject = get_subjects()
    chapter = get_chapters()
    total_questions= 0
    for chap in chapter:
        chap.total_questions = sum(len(quiz.questions) for quiz in chap.quizzes)
    return render_template("admin_dashboard.html",name=name,subjects=subject,chapters=chapter,total_questions=total_questions)

def get_quiz(today):
    quiz = Quiz.query.filter(Quiz.date_of_quiz<=today).all()
    return quiz

@app.route("/user/<name>")
@login_required
def user_dashboard(name):
    today = date.today()
    quizs=get_quiz(today)
    return render_template("user_dashboard.html", name=name,quizs=quizs)


def get_subjects():
    subjects = Subject.query.all()
    return subjects


def get_chapters():
    chapters = Chapter.query.all()
    return chapters

@app.route("/new_subject/<name>", methods=["GET", "POST"])
@login_required
def new_subject(name):
    if request.method == "POST":
        sname = request.form.get("name")
        sdesc = request.form.get("desc")
        newsub = Subject(name=sname, description=sdesc)
        db.session.add(newsub)
        db.session.commit()
        return redirect(url_for("admin_dashboard", name=name))
    return render_template("new_sub.html", name=name)


@app.route("/new_chap/<subject_id>/<name>", methods=["GET", "POST"])
@login_required
def new_chapter(subject_id, name):
    subject = Subject.query.filter_by(id=subject_id).first()
    if request.method == "POST":
        cname = request.form.get("name")
        cdesc = request.form.get("desc")
        newchap = Chapter(name=cname, description=cdesc, subject_id=subject_id)
        db.session.add(newchap)
        db.session.commit()
        return redirect(url_for("admin_dashboard", name=name))
    return render_template("new_chap.html", name=name, subject_id=subject_id, subject=subject)


def search_by_subj(search_txt):
    subjects = Subject.query.filter(Subject.name.ilike("%" + search_txt + "%")).all()
    return subjects


def search_by_chap(search_txt):
    chapters = Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%")).all()
    subjects = {chapter.subject for chapter in chapters}
    return list(subjects)

def search_quiz_by_subj(search_txt):
    subjects = Subject.query.filter(Subject.name.ilike("%" + search_txt + "%")).all()
    quizzes = []
    for subject in subjects:
        for chapter in subject.chapters:
            for quiz in chapter.quizzes:
                quizzes.append(quiz)
    return quizzes

def search_quiz_by_chap(search_txt):
    chapters = Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%")).all()
    quizzes = []
    for chapter in chapters:
            for quiz in chapter.quizzes:
                quizzes.append(quiz)
    return quizzes

def search_quiz_by_question(search_txt):
    questions = Question.query.filter(db.or_(
        Question.question_title.ilike(f"%{search_txt}%"),
        Question.question_statement.ilike(f"%{search_txt}%")
        )).all()
    quizzes = []
    for question in questions:
        if question.quiz not in quizzes:
            quizzes.append(question.quiz)
    return quizzes
    
def search_user(search_txt):
    users = user_info.query.filter(user_info.name.ilike(f"%{search_txt}%")).all()
    return users

@app.route("/admin/search/<name>", methods=["GET", "POST"])
@login_required
def admin_search(name):
    search_txt = request.form.get("search", "").strip()
    current_page = request.form.get("page", "home")
    
    by_subject = search_by_subj(search_txt)
    by_chapter = search_by_chap(search_txt)
    quiz_by_subject = search_quiz_by_subj(search_txt)
    quiz_by_chapter = search_quiz_by_chap(search_txt)
    by_question = search_quiz_by_question(search_txt)
    by_user = search_user(search_txt)
    if by_user:
        return render_template("user_detail.html",name=name,users=by_user)
    elif by_question:
        return render_template("quiz_management.html", name=name, quizs=by_question,current_page="quiz")
    else:
        if current_page == "home":
            if by_subject:
                return render_template("admin_dashboard.html", name=name, subjects=by_subject,current_page="home")
            elif by_chapter:
                return render_template("admin_dashboard.html", name=name, subjects=by_chapter,current_page="home")
            else:
                return render_template("admin_dashboard.html", name=name ,current_page="home")
        elif current_page == "quiz":
            if quiz_by_subject:
                return render_template("quiz_management.html", name=name, quizs=quiz_by_subject,current_page="quiz")
            elif quiz_by_chapter:
                return render_template("quiz_management.html", name=name, quizs=quiz_by_chapter,current_page="quiz")
            else:
                return render_template("quiz_management.html", name=name, current_page="quiz")
    return render_template("not_found.html", name=name,text=search_txt+" " + "Not Found")


@app.route("/edit_chap/<chapter_id>/<name>", methods=["GET", "POST"])
@login_required
def edit_chapter(chapter_id, name):
    chap = Chapter.query.filter_by(id=chapter_id).first()
    if request.method == "POST":
        chap.name = request.form.get("name")
        chap.description = request.form.get("desc")
        db.session.commit()
        return redirect(url_for("admin_dashboard", name=name))
    return render_template("edit_chap.html", name=name, chapter=chap, subject_id=chap.subject_id)


@app.route("/del_chap/<chapter_id>/<name>", methods=["GET", "POST"])
@login_required
def delete_chapter(chapter_id, name):
    chap = Chapter.query.filter_by(id=chapter_id).first()
    quizs=Quiz.query.filter_by(chapter_id=chapter_id).all()
    for quiz in quizs:
        questions = Question.query.filter_by(quiz_id=quiz.id).all()
        for q in questions:
            db.session.delete(q)
        db.session.delete(quiz)
    db.session.delete(chap)
    db.session.commit()
    return redirect(url_for("admin_dashboard", name=name))


@app.route("/edit_sub/<subject_id>/<name>", methods=["GET", "POST"])
@login_required
def edit_subject(subject_id, name):
    sub = Subject.query.filter_by(id=subject_id).first()
    if request.method == "POST":
        sub.name = request.form.get("name")
        sub.description = request.form.get("desc")
        db.session.commit()
        return redirect(url_for("admin_dashboard", name=name))
    return render_template("edit_sub.html", name=name, subject=sub, subject_id=sub.id)


@app.route("/del_sub/<subject_id>/<name>", methods=["GET", "POST"])
@login_required
def delete_subject(subject_id, name):
    sub = Subject.query.filter_by(id=subject_id).first()
    chapters = Chapter.query.filter_by(subject_id=subject_id).all()
    for chap in chapters:
        quizs=Quiz.query.filter_by(chapter_id=chap.id).all()
        for quiz in quizs:
            questions = Question.query.filter_by(quiz_id=quiz.id).all()
            for q in questions:
                db.session.delete(q)
            db.session.delete(quiz)
        db.session.delete(chap)
    db.session.delete(sub)
    db.session.commit()
    return redirect(url_for("admin_dashboard", name=name))

@app.route("/admin/quiz_management/<name>", methods=["GET", "POST"])
@login_required
def quiz_management(name):
    quiz = get_quiz_for_admin()
    q = get_question()
    sub = get_subjects()
    chap=get_chapters()
    return render_template("quiz_management.html", name=name, subject=sub, quizs=quiz, questions=q,chapter=chap)


def get_quiz_for_admin():
    quiz = Quiz.query.all()
    return quiz


def get_question():
    question = Question.query.all()
    return question


@app.route("/admin/quiz_management/new_quiz/<name>", methods=["GET", "POST"])
@login_required
def new_quiz(name):
    if request.method == "POST":
        chap_id = request.form.get("id")
        date = request.form.get("date")
        duration = request.form.get("duration")
        remarks = request.form.get("remarks")
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        chap = Chapter.query.filter_by(id=chap_id).first()
        if not chap:
            return render_template("new_quiz.html",name=name, mssg="Chapter does not exist, Kindly add Chapter first")
        else:
            newquiz = Quiz(chapter_id=chap_id,date_of_quiz=date_obj,time_duration=duration,remarks=remarks)
            db.session.add(newquiz)
            db.session.commit()
            return redirect(url_for("quiz_management", name=name))
    return render_template("new_quiz.html", name=name)


@app.route("/edit_quiz/<quiz_id>/<name>", methods=["GET", "POST"])
@login_required
def edit_quiz(quiz_id, name):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if request.method == "POST":
        quiz.chapter_id = request.form.get("id")
        quiz.name = request.form.get("name")
        quiz.time_duration = request.form.get("duration")
        quiz.date_of_quiz = datetime.strptime(request.form.get("date"), "%Y-%m-%d").date()
        quiz.description = request.form.get("desc")
        chap = Chapter.query.filter_by(id=quiz.chapter_id).first()
        if not chap:
            return render_template("new_quiz.html",name=name, mssg="Chapter does not exist, Kindly add Chapter first")
        else:
            db.session.commit()
            return redirect(url_for("quiz_management", name=name))
    return render_template("edit_quiz.html", name=name, quiz=quiz, quiz_id=quiz.id,chapter_id=quiz.chapter_id)

@app.route("/del_quiz/<quiz_id>/<name>", methods=["GET", "POST"])
@login_required
def delete_quiz(quiz_id, name):
    quiz = Quiz.query.filter_by(id=quiz_id).first()
    if quiz:
        questions = Question.query.filter_by(quiz_id=quiz_id).all()
        for q in questions:
            db.session.delete(q)
        db.session.delete(quiz)
        db.session.commit()
    return redirect(url_for("quiz_management", name=name))

@app.route("/new_q/<quiz_id>/<name>", methods=["GET", "POST"])
@login_required
def new_q(quiz_id, name):
    chap=None
    quiz= Quiz.query.filter_by(id=quiz_id).first()
    if quiz:
        chap = Chapter.query.filter_by(id=quiz.chapter_id).first()
    if request.method == "POST":
        chap_id = request.form.get("id")
        q_title = request.form.get("question_title")
        q_statement = request.form.get("question_statement")
        o_1 = request.form.get("option_1")
        o_2 = request.form.get("option_2")
        o_3 = request.form.get("option_3")
        o_4 = request.form.get("option_4")
        c_o = request.form.get("correct_option")
        quiz = Quiz.query.filter_by(id=quiz_id).first()
        chap = Chapter.query.filter_by(id=chap_id).first()
        if not chap:
            return render_template("new_q.html", name=name, chapter=chap, mssg="Chapter does not exist, Kindly add Chapter first")
        if quiz.chapter_id != int(chap_id):
            return render_template("new_q.html", name=name, chapter=chap, mssg="This quiz does not belong to this chapter")
        else:
            newq = Question(quiz_id=quiz_id,question_title=q_title,question_statement=q_statement,option1=o_1,option2=o_2,option3=o_3,option4=o_4,correct_option=c_o)
            db.session.add(newq)
            db.session.commit()
            return redirect(url_for("quiz_management", name=name))
    return render_template("new_q.html", name=name, quiz_id=quiz_id,chapter=chap,quiz=quiz)

@app.route("/edit_q/<question_id>/<name>", methods=["GET", "POST"])
@login_required
def edit_q(question_id, name):
    chap=None
    q = Question.query.filter_by(id=question_id).first()
    if request.method == "POST":
        chap_id = request.form.get("id")
        q.chapter_id = request.form.get("id")
        q.question_title = request.form.get("question_title")
        q.question_statement = request.form.get("question_statement")
        q.option1 = request.form.get("option_1")
        q.option2 = request.form.get("option_2")
        q.option3 = request.form.get("option_3")
        q.option4 = request.form.get("option_4")
        q.correct_option = request.form.get("correct_option").strip()
        db.session.commit()
        chap = Chapter.query.filter_by(id=chap_id).first()
        return redirect(url_for("quiz_management", name=name))
    return render_template("edit_q.html", name=name,chapter=chap,question=q)

@app.route("/del_q/<question_id>/<name>", methods=["GET", "POST"])
@login_required
def delete_q(question_id, name):
    q = Question.query.filter_by(id=question_id).first()
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for("quiz_management", name=name))

def get_quiz_by_id(id):
    quiz = Quiz.query.filter_by(id=id).first()
    return quiz 

@app.route("/admin/users/<name>", methods=["GET", "POST"])
@login_required
def user_detail(name):
    users = user_info.query.filter_by(role=1).all()
    return render_template("users.html", name=name, users=users)

@app.route("/user/view/quiz/<quiz_id>/<name>", methods=["GET", "POST"])
def view_quiz(quiz_id,name):
    quiz = get_quiz_by_id(quiz_id)
    return render_template("view_quiz.html", name=name, quiz=quiz)

app.secret_key="ad"

@app.route("/user/start/quiz/<quiz_id>/<name>", methods=["GET", "POST"])
@login_required
def start_quiz(quiz_id,name):
    quiz = get_quiz_by_id(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    if not questions:
        return render_template("not_found.html", name=name, text="No Questions Found")
    time = quiz.time_duration.split(":")
    total_time_in_seconds = int(time[0])*3600 + int(time[1])*60
    session["question_no"] = 0
    session["time_left"] = total_time_in_seconds
    session["total_time"] = total_time_in_seconds
    session["quiz_start_time"] = datetime.utcnow().isoformat()
    remaining_time = total_time_in_seconds
    return render_template("start_quiz.html", name=name, quiz=quiz, question=questions[0],time_left=(remaining_time))

@app.route("/user/start/quiz/next_q/<quiz_id>/<name>", methods=["GET", "POST"])
def next_q(quiz_id,name):
    quiz = get_quiz_by_id(quiz_id)
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    question_no = session.get("question_no",0)
    u_ans = request.form.get("s_o")
    if "ans" not in session or session.get("question_no", 0) == 0:
        session["ans"]=[]
    session["ans"].append(u_ans if u_ans else "NONE")
    
    total_time = session.get("total_time", 0)
    start_time_str = session.get("quiz_start_time")
    if start_time_str:
        quiz_start_time = datetime.fromisoformat(start_time_str)
        elapsed = (datetime.utcnow() - quiz_start_time).total_seconds()
    else:
        elapsed = 0
    remaining_time = max(int(total_time - elapsed), 0)
    session["time_left"] = remaining_time
    if question_no < len(questions)-1:
        question_no += 1
        session["question_no"] = question_no
    elif question_no == len(questions)-1:
        return  render_template("start_quiz.html", name=name, quiz=quiz, question=questions[question_no], mssg="No Questions Left, Click on Submit",time_left=remaining_time)
    return render_template("start_quiz.html", name=name, quiz=quiz, question=questions[question_no],time_left=remaining_time)


@app.route("/user/submit/quiz/<quiz_id>/<name>", methods=["GET", "POST"])
def submit_quiz(quiz_id,name):
    questions = Question.query.filter_by(quiz_id=quiz_id).all()
    user_ans= session.get("ans",[])
    scores=0
    total_score = int(len(questions))
    i=0
    results = {}
    for q in questions:
        correct_option = q.correct_option
        q_title = q.question_title
        q_id = q.id
        if i < len(user_ans):
            user_answer = user_ans[i]
        else:
            user_answer = "Unattempted" 
        is_correct = user_answer.isdigit() and int(user_answer) == correct_option
        if is_correct:
            scores += 1
        results[q_id] = { "question_no": i + 1,"question_title": q_title,"correct_option": correct_option,"user_option": user_answer,"score": 1 if is_correct else 0}
        session["results"] = results
        i += 1
    score = Score(quiz_id=quiz_id,user_id=session["user_id"],total_score=scores,time_stamp_of_attempt=datetime.utcnow().date(),total_questions=total_score)
    db.session.add(score)
    db.session.commit()
    session.pop("ans", None)
    scores = Score.query.filter_by(user_id=session["user_id"]).all()
    # return render_template("scores.html", name=name, scores=scores)
    # return redirect(url_for("view_result", name=name))
    return redirect(url_for("view_result", name=name))

@app.route("/user/view/result/<name>", methods=["GET", "POST"])
def view_result(name):
    results = session.get("results", {})
    scores = Score.query.filter_by(user_id=session["user_id"]).all()
    total_score = int(len(results))
    return render_template("quiz_result.html", name=name, results=results, scores=scores, total_score=total_score)

@app.route("/user/view/scores/<name>", methods=["GET", "POST"])
@login_required
def view_scores(name):
    scores = Score.query.filter_by(user_id=session["user_id"]).all()
    return render_template("scores.html", name=name, scores=scores)

def get_user_bar_summary():
    scores=Score.query.filter_by(user_id=session["user_id"]).all()
    if scores:
        summary = {}        
        for score in scores:
            if score.quiz_id is None:
                sub_name = "N/A"
                if sub_name not in summary:
                    summary[sub_name] = 0
                summary[sub_name] += 1
            else:
                quiz = Quiz.query.get(score.quiz_id)
                if quiz.chapter_id is None:
                    sub_name = "N/A"
                    if sub_name not in summary:
                        summary[sub_name] = 0
                    summary[sub_name] += 1
                else:
                    chapter = Chapter.query.get(quiz.chapter_id)
                    if chapter.subject_id is None:
                        sub_name = "N/A"
                        if sub_name not in summary:
                            summary[sub_name] = 0
                        summary[sub_name] += 1
                    else:
                        subject = Subject.query.get(chapter.subject_id)
                        sub_name = subject.name
                        if sub_name not in summary:
                            summary[sub_name] = 0
                        summary[sub_name] += 1
        if not summary:
            return None
        x_names = list(summary.keys())
        y_count = list(summary.values())
        plt.bar(x_names,y_count,color=["blue", "green", "orange", "purple","red"],width=0.4)
        plt.title("Subject wise quiz attempt")
        plt.xlabel("Subjects")
        plt.ylabel("No of quizz attempted")
        graph_path= "./static/images/user_barchart.jpeg"
        plt.savefig(graph_path)
        plt.close()
    return graph_path

def get_user_pie_summary():
    scores=Score.query.filter_by(user_id=session["user_id"]).all()
    monthly_summary = {}
    for score in scores:
        if not score.quiz_id:
            month=score.time_stamp_of_attempt.strftime("%b %Y")
        month=score.time_stamp_of_attempt.strftime("%b %Y")
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += 1
    labels = list(monthly_summary.keys())
    sizes = list(monthly_summary.values())
    plt.figure(figsize=(7, 7))
    wedges, texts, autotexts = plt.pie(
        sizes, labels=labels, startangle=90, colors=["blue", "green", "orange", "purple","red"],
        autopct=lambda p: f'{round(p * sum(sizes) / 100)}'
    )
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_fontsize(12)
        autotext.set_color("white")
    plt.title("Month-wise Quiz Attempts")
    graph_path = "./static/images/user_piechart.jpeg"
    plt.savefig(graph_path)
    plt.close()
    return graph_path

@app.route("/user/user_summary/<name>", methods=["GET", "POST"])
@login_required
def user_summary(name):
    try:
        bar_graph = get_user_bar_summary()
        pie_graph = get_user_pie_summary()
        if not bar_graph or not pie_graph:
            return render_template("not_found.html", name=name, text="No Data Right Now")
        return render_template("user_summary.html", name=name)
    except Exception as e:
        return render_template("not_found.html", name=name, text="No Data Right Now")

def get_admin_bar_summary():
    scores=Score.query.all()
    subject_wise_score = {}        
    for score in scores:
        if score.quiz_id is None:
            sub_name = "N/A"
            subject_wise_score[sub_name] = score.total_score
        else:
            quiz = Quiz.query.get(score.quiz_id)
            if quiz.chapter_id is None:
                sub_name = "N/A"
                subject_wise_score[sub_name] = score.total_score
            else:
                chapter = Chapter.query.get(quiz.chapter_id)
                if chapter.subject_id is None:
                    sub_name = "N/A"
                    subject_wise_score[sub_name] = score.total_score
                else:
                    subject = Subject.query.get(chapter.subject_id)
                    if subject.name not in subject_wise_score or score.total_score > subject_wise_score[subject.name]:
                        sub_name = subject.name
                        subject_wise_score[sub_name] = score.total_score
    if not subject_wise_score:
        return None
    x_names = list(subject_wise_score.keys())
    y_count = list(subject_wise_score.values())
    plt.bar(x_names,y_count,color=["blue", "green", "orange", "purple","red"],width=0.4)
    plt.title("Subject wise heighest score",fontsize=20, fontweight='bold')
    plt.xlabel("Subjects")
    plt.ylabel("Heighest score")
    graph_path= "./static/images/admin_barchart.jpeg"
    plt.savefig(graph_path)
    plt.close()
    return graph_path

def get_subject_wise_user_attmept():
    scores=Score.query.all()
    subject_wise_user_attempt = {}        
    for score in scores:
        sub_name = "N/A"
        if score.quiz:
            quiz = Quiz.query.get(score.quiz_id)
            if quiz and quiz.chapter_id:
                chapter = Chapter.query.get(quiz.chapter_id)
                if chapter and chapter.subject_id:
                    subject = Subject.query.get(chapter.subject_id)
                    if subject and subject.name:
                        sub_name = subject.name
        if sub_name not in subject_wise_user_attempt:
            subject_wise_user_attempt[sub_name] = 0
        subject_wise_user_attempt[sub_name] += 1
    if not subject_wise_user_attempt:
        return None
    subjects = list(subject_wise_user_attempt.keys())
    count_of_attempt = list(subject_wise_user_attempt.values())
    total_attempts = sum(count_of_attempt)
    colors=["blue", "green", "orange", "purple", "red", "cyan", "pink", "yellow"]
    fig,ax=plt.subplots(figsize=(8,8))
    radius=0.8
    max_attempts = max(count_of_attempt)
    min_width = 0.1
    max_width = 0.35
    for i in range(len(subjects)):
        width = (count_of_attempt[i] / max_attempts) * max_width
        width = max(width, min_width)
        ax.pie([1],radius=radius, colors=[colors[i % len(colors)]],wedgeprops=dict(width=width, edgecolor='white'),startangle=90)
        ax.text(0,radius-(width/2),f"{subjects[i]} {count_of_attempt[i]}",horizontalalignment='center',verticalalignment='center',fontsize=12,fontweight='bold',color='w')
        radius -= width
    plt.text(0, 0, f"Total\n{total_attempts}", ha='center', va='center',fontsize=18, fontweight='bold', color="black")
    plt.title("Subject wise user attempts",fontsize=30, fontweight='bold')
    graph_path= "./static/images/admin_bullseye_chart.jpeg"
    plt.savefig(graph_path)
    plt.close()
    return graph_path

@app.route("/admin/admin_summary/<name>", methods=["GET", "POST"])
@login_required
def admin_summary(name):
    try:
        get_admin_bar_summary()
        get_subject_wise_user_attmept()
        return render_template("admin_summary.html", name=name)
    except Exception as e:
        return render_template("not_found.html", name=name, text="No Data Right Now")

def search_quiz_by_subj_for_user(search_txt):
    subjects = Subject.query.filter(Subject.name.ilike("%" + search_txt + "%")).all()
    quizzes = []
    today= date.today()
    for subject in subjects:
        for chapter in subject.chapters:
            for quiz in chapter.quizzes:
                if quiz.date_of_quiz <=today:
                    quizzes.append(quiz)
    return quizzes

def search_quiz_by_chap_for_user(search_txt):
    chapters = Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%")).all()
    quizzes = []
    today = date.today()
    for chapter in chapters:
            for quiz in chapter.quizzes:
                if quiz.date_of_quiz <=today:
                    quizzes.append(quiz)
    return quizzes

def search_score_by_subj(search_txt):
    subjects = Subject.query.filter(Subject.name.ilike("%" + search_txt + "%")).all()
    scores = []
    for subject in subjects:
        for chapter in subject.chapters:
            for quiz in chapter.quizzes:
                for score in quiz.scores:
                    scores.append(score)
    return scores

def search_score_by_chap(search_txt):
    chapters = Chapter.query.filter(Chapter.name.ilike(f"%{search_txt}%")).all()
    scores = []
    for chapter in chapters:
            for quiz in chapter.quizzes:
                for score in quiz.scores:
                    scores.append(score)
    return scores

def search_score_by_date(search_txt):
    scores = Score.query.filter(Score.time_stamp_of_attempt.ilike(f"%{search_txt}%")).all()
    return scores

def search_score_by_score(search_txt):
    scores = Score.query.filter(Score.total_score == search_txt).all()
    return scores
@app.route("/user/search/<name>", methods=["GET", "POST"])
@login_required
def user_search(name):
    search_txt = request.form.get("search", "").strip()
    current_page = request.form.get("page", "home")
    
    quiz_by_subject = search_quiz_by_subj_for_user(search_txt)
    quiz_by_chapter = search_quiz_by_chap_for_user(search_txt)
    score_by_subject = search_score_by_subj(search_txt)
    score_by_chapter = search_score_by_chap(search_txt)
    score_by_date = search_score_by_date(search_txt)
    score_by_score = search_score_by_score(search_txt)
    if current_page == "home":
        if quiz_by_subject:
            return render_template("user_dashboard.html", name=name, quizs=quiz_by_subject,current_page="home")
        elif quiz_by_chapter:
            return render_template("user_dashboard.html", name=name, quizs=quiz_by_chapter,current_page="home")
        else:
            return render_template("user_dashboard.html", name=name, current_page="home")
    elif current_page == "scores":
        if score_by_subject:
            return render_template("scores.html", name=name, scores=score_by_subject,current_page="scores")
        elif score_by_chapter:
            return render_template("scores.html", name=name, scores=score_by_chapter,current_page="scores")
        elif score_by_score:
            return render_template("scores.html", name=name, scores=score_by_score,current_page="scores")
        elif score_by_date:
            return render_template("scores.html", name=name, scores=score_by_date,current_page="scores")
        else:
            return render_template("scores.html", name=name, current_page="scores")
        
    return render_template("not_found.html", name=name,text=search_txt+" " + "Not Found")
