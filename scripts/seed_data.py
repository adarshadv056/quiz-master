import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from models.models import db, Subject, Chapter, Quiz, Question
from datetime import date

def seed_database():
    with app.app_context():
        print("Starting database seeding...")

        # Update or clean up placeholder subjects if they exist
        math_sub = Subject.query.filter_by(id=1).first()
        if math_sub:
            math_sub.name = "Mathematics & Linear Algebra"
            math_sub.description = "Vector spaces, matrix decompositions, multivariable calculus, and discrete mathematics."

        dl_sub = Subject.query.filter_by(id=2).first()
        if dl_sub:
            dl_sub.name = "Deep Learning & Neural Networks"
            dl_sub.description = "Backpropagation, convolutional architectures, transformer attention, and optimization."

        # Define curriculum structure
        curriculum = [
            {
                "subject": "Database Management Systems",
                "description": "Relational algebra, SQL, normalization, concurrency control, ACID properties, and query indexing.",
                "chapters": [
                    {
                        "name": "Relational Model & SQL Queries",
                        "description": "Schema definitions, relational integrity, primary/foreign keys, joins, and nested subqueries.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:15",
                            "remarks": "Official assessment covering SQL semantics, relational algebra, and joins.",
                            "questions": [
                                {
                                    "title": "Primary Key Integrity",
                                    "statement": "Which of the following conditions MUST be satisfied by a primary key in a relational table?",
                                    "op1": "It may contain NULL values as long as they are distinct.",
                                    "op2": "It must uniquely identify each tuple and cannot contain NULL values.",
                                    "op3": "It must always be an auto-incrementing integer data type.",
                                    "op4": "A table may have multiple primary keys defined concurrently.",
                                    "correct": 2
                                },
                                {
                                    "title": "SQL Join Behavior",
                                    "statement": "Which SQL JOIN returns all rows from the left table even if there are no matching rows in the right table?",
                                    "op1": "INNER JOIN",
                                    "op2": "CROSS JOIN",
                                    "op3": "LEFT OUTER JOIN",
                                    "op4": "NATURAL JOIN",
                                    "correct": 3
                                },
                                {
                                    "title": "Aggregate Functions & WHERE",
                                    "statement": "Why can aggregate functions like AVG() or COUNT() NOT be directly placed inside an SQL WHERE clause?",
                                    "op1": "WHERE filters individual rows before grouping takes place; HAVING must be used.",
                                    "op2": "Aggregate functions can only be executed in SQLite.",
                                    "op3": "Aggregate functions require an explicit index on the target column.",
                                    "op4": "The SQL parser treats aggregates as stored procedures.",
                                    "correct": 1
                                },
                                {
                                    "title": "SQL Subqueries",
                                    "statement": "What type of subquery executes once for each candidate row evaluated by the outer query?",
                                    "op1": "Correlated subquery",
                                    "op2": "Scalar subquery",
                                    "op3": "Independent subquery",
                                    "op4": "Common table expression (CTE)",
                                    "correct": 1
                                }
                            ]
                        }
                    },
                    {
                        "name": "Normalization & ACID Properties",
                        "description": "Functional dependencies, 1NF through BCNF decomposition, and transaction management.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:20",
                            "remarks": "Exam covering database design anomalies, lossless join decomposition, and ACID guarantees.",
                            "questions": [
                                {
                                    "title": "Third Normal Form (3NF)",
                                    "statement": "A relational table is in Third Normal Form (3NF) if it is in 2NF and has no:",
                                    "op1": "Partial functional dependencies",
                                    "op2": "Transitive functional dependencies on any candidate key",
                                    "op3": "Multi-valued dependencies",
                                    "op4": "Foreign key relationships",
                                    "correct": 2
                                },
                                {
                                    "title": "ACID Properties - Isolation",
                                    "statement": "In the ACID model of database transactions, what does 'Isolation' guarantee?",
                                    "op1": "All transactions are written directly to permanent disk storage.",
                                    "op2": "Concurrent execution of transactions results in a state equivalent to serial execution.",
                                    "op3": "All constraints and database invariants are checked at commit time.",
                                    "op4": "Either all transaction actions complete, or none of them do.",
                                    "correct": 2
                                },
                                {
                                    "title": "Boyce-Codd Normal Form (BCNF)",
                                    "statement": "For a relation to be in BCNF, for every non-trivial functional dependency X -> Y, X must be a:",
                                    "op1": "Superkey",
                                    "op2": "Foreign key",
                                    "op3": "Prime attribute",
                                    "op4": "Secondary index",
                                    "correct": 1
                                },
                                {
                                    "title": "Deadlock Detection",
                                    "statement": "Which graph data structure is typically constructed by a DBMS engine to detect transaction deadlocks?",
                                    "op1": "B-Tree directory",
                                    "op2": "Wait-For Graph (WFG)",
                                    "op3": "Precedence execution schedule",
                                    "op4": "Spanning forest",
                                    "correct": 2
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "subject": "Operating Systems & Kernel Architecture",
                "description": "Processes, CPU scheduling algorithms, synchronization primitives, virtual memory, and file systems.",
                "chapters": [
                    {
                        "name": "Process Synchronization & CPU Scheduling",
                        "description": "Critical section problem, semaphores, mutexes, deadlocks, and preemptive scheduling policies.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:15",
                            "remarks": "Test your mastery of concurrent process coordination and CPU dispatcher algorithms.",
                            "questions": [
                                {
                                    "title": "CPU Scheduling - Shortest Job First",
                                    "statement": "What is the primary drawback of the non-preemptive Shortest Job First (SJF) scheduling algorithm?",
                                    "op1": "It produces the highest possible average turnaround time.",
                                    "op2": "Long jobs can suffer from indefinite starvation if short jobs arrive continuously.",
                                    "op3": "It requires hardware timer interrupt support.",
                                    "op4": "Context switching overhead exceeds process execution time.",
                                    "correct": 2
                                },
                                {
                                    "title": "Critical Section Requirements",
                                    "statement": "Which three criteria MUST be satisfied by any valid solution to the Critical Section problem?",
                                    "op1": "Mutual Exclusion, Progress, and Bounded Waiting",
                                    "op2": "Atomicity, Consistency, and Durability",
                                    "op3": "Preemption, Aging, and Quantum Sharing",
                                    "op4": "Deadlock, Starvation, and Race Resolution",
                                    "correct": 1
                                },
                                {
                                    "title": "Semaphores vs Mutexes",
                                    "statement": "How does a counting semaphore differ primarily from a binary mutex?",
                                    "op1": "A counting semaphore can only be initialized to zero.",
                                    "op2": "A counting semaphore can regulate access to a finite pool of multiple identical resources.",
                                    "op3": "A binary mutex can be unlocked by any arbitrary thread.",
                                    "op4": "A counting semaphore operates purely in user-space without kernel traps.",
                                    "correct": 2
                                },
                                {
                                    "title": "Deadlock Coffman Conditions",
                                    "statement": "Which of the following is NOT one of Coffman's four necessary conditions for deadlock?",
                                    "op1": "Mutual Exclusion",
                                    "op2": "Hold and Wait",
                                    "op3": "Preemption Allowed",
                                    "op4": "Circular Wait",
                                    "correct": 3
                                }
                            ]
                        }
                    },
                    {
                        "name": "Virtual Memory Management & Paging",
                        "description": "Page tables, Translation Lookaside Buffer (TLB), page faults, and replacement algorithms.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:20",
                            "remarks": "Core assessment on memory paging hierarchy, address translation, and page replacement.",
                            "questions": [
                                {
                                    "title": "Page Fault Definition",
                                    "statement": "What condition directly triggers a hardware page fault exception in the MMU?",
                                    "op1": "A memory write operation exceeds the page table buffer limit.",
                                    "op2": "An instruction references a virtual page whose valid/invalid bit is set to invalid in RAM.",
                                    "op3": "The TLB hit ratio exceeds 99% during a clock tick.",
                                    "op4": "A thread attempts to deallocate physical frame 0.",
                                    "correct": 2
                                },
                                {
                                    "title": "Translation Lookaside Buffer (TLB)",
                                    "statement": "What is the primary role of the Translation Lookaside Buffer (TLB) in virtual memory systems?",
                                    "op1": "To cache recently translated virtual-to-physical address mappings for fast lookup.",
                                    "op2": "To store inactive process images on secondary disk storage.",
                                    "op3": "To compute cryptographic checksums on memory pages.",
                                    "op4": "To resolve external fragmentation in kernel heap allocations.",
                                    "correct": 1
                                },
                                {
                                    "title": "Belady's Anomaly",
                                    "statement": "Belady's anomaly occurs when allocating more physical memory frames increases page faults under which algorithm?",
                                    "op1": "Least Recently Used (LRU)",
                                    "op2": "First-In, First-Out (FIFO)",
                                    "op3": "Optimal Page Replacement (OPT)",
                                    "op4": "Least Frequently Used (LFU)",
                                    "correct": 2
                                }
                            ]
                        }
                    }
                ]
            },
            {
                "subject": "Data Structures & Python Algorithms",
                "description": "Algorithmic complexity, linear structures, search trees, priority queues, and graph algorithms.",
                "chapters": [
                    {
                        "name": "Trees, Heaps & Search Structures",
                        "description": "Binary search trees, balanced AVL trees, binary heaps, and priority queue implementations.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:15",
                            "remarks": "Comprehensive challenge on tree traversal orders, heap operations, and balancing.",
                            "questions": [
                                {
                                    "title": "BST Inorder Traversal Property",
                                    "statement": "An inorder (left-root-right) traversal of a valid Binary Search Tree (BST) visits nodes in:",
                                    "op1": "Descending numerical order",
                                    "op2": "Strictly ascending sorted order",
                                    "op3": "Breadth-first level order",
                                    "op4": "Reverse topological order",
                                    "correct": 2
                                },
                                {
                                    "title": "Binary Min-Heap Insertion",
                                    "statement": "What is the worst-case time complexity of inserting a new key into a binary min-heap with n elements?",
                                    "op1": "O(1)",
                                    "op2": "O(log n)",
                                    "op3": "O(n)",
                                    "op4": "O(n log n)",
                                    "correct": 2
                                },
                                {
                                    "title": "AVL Tree Balance Factor",
                                    "statement": "In an AVL balanced tree, what are the permissible values for the balance factor (height(left) - height(right))?",
                                    "op1": "0 only",
                                    "op2": "-1, 0, or +1",
                                    "op3": "-2, 0, or +2",
                                    "op4": "Any integer <= log(n)",
                                    "correct": 2
                                },
                                {
                                    "title": "Python Dictionary Time Complexity",
                                    "statement": "In standard Python (CPython), what is the average-case time complexity for key lookup in a dict?",
                                    "op1": "O(1)",
                                    "op2": "O(log n)",
                                    "op3": "O(n)",
                                    "op4": "O(k) where k is the string length squared",
                                    "correct": 1
                                }
                            ]
                        }
                    },
                    {
                        "name": "Graph Algorithms & Shortest Paths",
                        "description": "Graph representation, BFS, DFS, Dijkstra's algorithm, and minimum spanning trees.",
                        "quiz": {
                            "date": date.today(),
                            "duration": "00:20",
                            "remarks": "Graph theory exam covering adjacency representations, traversal invariants, and pathfinding.",
                            "questions": [
                                {
                                    "title": "Dijkstra's Algorithm Precondition",
                                    "statement": "Under what condition will Dijkstra's single-source shortest path algorithm fail to guarantee optimal paths?",
                                    "op1": "The graph contains directed edges.",
                                    "op2": "The graph contains cycle structures.",
                                    "op3": "The graph contains negative edge weights.",
                                    "op4": "The graph has more edges than vertices.",
                                    "correct": 3
                                },
                                {
                                    "title": "Topological Sort Application",
                                    "statement": "A topological ordering of vertices is possible if and only if the graph is a:",
                                    "op1": "Complete undirected graph",
                                    "op2": "Directed Acyclic Graph (DAG)",
                                    "op3": "Bipartite graph with equal partitions",
                                    "op4": "Planar tree with no bridges",
                                    "correct": 2
                                },
                                {
                                    "title": "Breadth-First Search Queue Invariant",
                                    "statement": "What data structure is fundamentally utilized by Breadth-First Search (BFS) to discover vertices level by level?",
                                    "op1": "LIFO Call Stack",
                                    "op2": "FIFO Queue",
                                    "op3": "Disjoint-Set Union (DSU)",
                                    "op4": "Segment Tree",
                                    "correct": 2
                                }
                            ]
                        }
                    }
                ]
            }
        ]

        # Populate curriculum
        for sub_data in curriculum:
            sub = Subject.query.filter_by(name=sub_data["subject"]).first()
            if not sub:
                sub = Subject(name=sub_data["subject"], description=sub_data["description"])
                db.session.add(sub)
                db.session.commit()
                print(f"Added Subject: {sub.name} (id={sub.id})")
            else:
                sub.description = sub_data["description"]
                db.session.commit()

            for chap_data in sub_data["chapters"]:
                chap = Chapter.query.filter_by(name=chap_data["name"], subject_id=sub.id).first()
                if not chap:
                    chap = Chapter(name=chap_data["name"], description=chap_data["description"], subject_id=sub.id)
                    db.session.add(chap)
                    db.session.commit()
                    print(f"  Added Chapter: {chap.name} (id={chap.id})")
                else:
                    chap.description = chap_data["description"]
                    db.session.commit()

                quiz_data = chap_data.get("quiz")
                if quiz_data:
                    quiz = Quiz.query.filter_by(chapter_id=chap.id).first()
                    if not quiz:
                        quiz = Quiz(
                            chapter_id=chap.id,
                            date_of_quiz=quiz_data["date"],
                            time_duration=quiz_data["duration"],
                            remarks=quiz_data["remarks"]
                        )
                        db.session.add(quiz)
                        db.session.commit()
                        print(f"    Added Quiz: #{quiz.id} under {chap.name}")
                    else:
                        quiz.date_of_quiz = quiz_data["date"]
                        quiz.time_duration = quiz_data["duration"]
                        quiz.remarks = quiz_data["remarks"]
                        db.session.commit()

                    for q_item in quiz_data.get("questions", []):
                        existing_q = Question.query.filter_by(quiz_id=quiz.id, question_title=q_item["title"]).first()
                        if not existing_q:
                            new_q = Question(
                                quiz_id=quiz.id,
                                question_title=q_item["title"],
                                question_statement=q_item["statement"],
                                option1=q_item["op1"],
                                option2=q_item["op2"],
                                option3=q_item["op3"],
                                option4=q_item["op4"],
                                correct_option=q_item["correct"]
                            )
                            db.session.add(new_q)
                            db.session.commit()
                            print(f"      Added Question: {new_q.question_title}")

        print("Curriculum database seeding successfully completed!")

if __name__ == "__main__":
    seed_database()
