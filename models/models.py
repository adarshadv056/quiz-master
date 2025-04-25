from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class user_info(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    qualification = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    role = db.Column(db.Integer, default=1)

class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text)
    chapters = db.relationship('Chapter', backref='subject', lazy=True)

class Chapter(db.Model):
    __tablename__ = 'chapter'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    quizzes = db.relationship('Quiz', backref='chapter', lazy=True)

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    date_of_quiz = db.Column(db.Date)
    time_duration = db.Column(db.String)  
    remarks = db.Column(db.Text)
    questions = db.relationship('Question', backref='quiz', lazy=True)
    
class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_title = db.Column(db.Text, nullable=False)
    question_statement = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String)
    option2 = db.Column(db.String)
    option3 = db.Column(db.String)
    option4 = db.Column(db.String)
    correct_option = db.Column(db.Integer, nullable=False)

class Score(db.Model):
    __tablename__ = 'score'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    time_stamp_of_attempt = db.Column(db.Date, default=datetime.utcnow().date())
    total_score = db.Column(db.Integer)
    quiz = db.relationship('Quiz', backref='scores')
    total_questions = db.Column(db.Integer)