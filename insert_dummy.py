'''
Database email: firoha5361@acroins.com
Database password: Password1234
Database link: https://www.freemysqlhosting.net/
Password: AB4DeU48AR
Port number: 3306
'''

import mysql.connector

def create_database_and_tables():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='sql5.freemysqlhosting.net',
        port=3306,
        user='sql5740507',     # Replace with your MySQL username
        password='AB4DeU48AR'  # Replace with your MySQL password
    )

    cursor = connection.cursor()

    # List of SQL commands
    sql_commands = [
        "USE sql5740507;",
        """
        INSERT INTO ETextbook (ID, Title) VALUES
        (1, 'Introduction to SQL'),
        (2, 'Advanced SQL Concepts');
        """,
        """
        INSERT INTO Chapter (Title, Number, TextbookID) VALUES
        ('Basics of SQL', '1', 1),
        ('Joins and Subqueries', '2', 1),
        ('Advanced Queries', '1', 2);
        """,
        """
        INSERT INTO Section (Title, Number, TextbookID, ChapterTitle) VALUES
        ('Introduction', 1, 1, 'Basics of SQL'),
        ('Creating Tables', 2, 1, 'Basics of SQL'),
        ('Inner Joins', 1, 1, 'Joins and Subqueries'),
        ('Outer Joins', 2, 1, 'Joins and Subqueries'),
        ('Complex Queries', 1, 2, 'Advanced Queries');
        """,
        """
        INSERT INTO ContentBlock (Type, ID, DisplayOrder, Content, SectionTitle, TextbookID, ChapterTitle, Hidden) VALUES
        ('T', 1, 1, 'Introduction to SQL basics.', 'Introduction', 1, 'Basics of SQL', FALSE),
        ('T', 2, 2, 'How to create tables.', 'Creating Tables', 1, 'Basics of SQL', FALSE),
        ('T', 3, 1, 'Understanding inner joins.', 'Inner Joins', 1, 'Joins and Subqueries', FALSE),
        ('T', 4, 2, 'Understanding outer joins.', 'Outer Joins', 1, 'Joins and Subqueries', FALSE),
        ('T', 5, 1, 'Learning advanced SQL queries.', 'Complex Queries', 2, 'Advanced Queries', FALSE);
        """,
        """
        INSERT INTO Activity (Question, ID, ContentID, SectionTitle, ChapterTitle, TextbookID, Hidden) VALUES
        ('What is SQL?', 1, 1, 'Introduction', 'Basics of SQL', 1, FALSE),
        ('How to join tables?', 2, 3, 'Inner Joins', 'Joins and Subqueries', 1, FALSE);
        """,
        """
        INSERT INTO Role (Role) VALUES
        ('Faculty'),
        ('TA'),
        ('Admin'),
        ('Student');
        """,
        """
        INSERT INTO User (ID, FirstName, LastName, Email, Password, Role) VALUES
        ('U001', 'Alice', 'Smith', 'alice@example.com', 'password1', 'Faculty'),
        ('U002', 'Bob', 'Johnson', 'bob@example.com', 'password2', 'TA'),
        ('U003', 'Charlie', 'Brown', 'charlie@example.com', 'password3', 'Student'),
        ('U004', 'Marques', 'Brownlee', 'marques@example.com', 'password4', 'Admin');
        """,
        """
        INSERT INTO Course (ID, Title, StartDate, EndDate, Type, Faculty, ETextbookID) VALUES
        ('C001', 'Database Systems', '2024-01-10', '2024-04-30', 'L', 'U001', 1),
        ('C002', 'Advanced Databases', '2024-01-15', '2024-05-15', 'L', 'U001', 2);
        """,
        """
        INSERT INTO Student (ID, UserID, CourseID, TotalPoints, ParticipationPoints) VALUES
        ('S001', 'U003', 'C001', 80, 10),
        ('S002', 'U003', 'C002', 85, 15);
        """,
        """
        INSERT INTO CourseEnrollment (CourseID, StudentID, EnrollmentStatus) VALUES
        ('C001', 'S001', 'Enroll'),
        ('C002', 'S002', 'Enroll');
        """,
        """
        INSERT INTO ActiveCourse (CourseID, Token, Capacity, Enrollment) VALUES
        ('C001', 'TOKEN1', 30, 10),
        ('C002', 'TOKEN2', 30, 15);
        """,
        """
        INSERT INTO EvaluationCourse (CourseID, EvaluationMethod, TotalMarks) VALUES
        ('C001', 'Midterm', 100),
        ('C002', 'Final', 100);
        """,
        """
        CREATE TABLE IF NOT EXISTS CourseTA (
            CourseID VARCHAR(7),
            UserID VARCHAR(8),
            PRIMARY KEY (CourseID, UserID),
            FOREIGN KEY (CourseID) REFERENCES Course(ID),
            FOREIGN KEY (UserID) REFERENCES User(ID)
        );
        """,
        """
        INSERT INTO CourseTA (CourseID, UserID) VALUES
        ('C001', 'U002');
        """,
        """
        INSERT INTO Faculty (FacultyID, UserID) VALUES
        ('F001', 'U001');
        """,
        """
        CREATE TABLE IF NOT EXISTS Notification (
            ID VARCHAR(10) PRIMARY KEY,
            Message VARCHAR(20),
            UserID VARCHAR(8),
            IsRead BOOLEAN,
            Datetime DATETIME,
            FOREIGN KEY (UserID) REFERENCES User(ID)
        );
        """,
        """
        INSERT INTO ActivityScore (ActivityScoreID, StudentID, ActivityID, ContentID, SectionTitle, ChapterTitle, TextbookID, Score, Timestamp) VALUES
        ('AS001', 'S001', 1, 1, 'Introduction', 'Basics of SQL', 1, 10, '2024-01-15 10:00:00'),
        ('AS002', 'S002', 2, 3, 'Inner Joins', 'Joins and Subqueries', 1, 15, '2024-01-16 10:00:00');
        """,
        """
        INSERT INTO Notification (ID, Message, UserID, IsRead, Datetime) VALUES
        ('N001', 'New assign', 'U003', FALSE, '2024-01-15 09:00:00'),
        ('N002', 'Midterm.', 'U003', TRUE, '2024-03-01 10:00:00');
        """,
        """
        INSERT INTO Answer (Text, Description, Type, ActivityID, ContentID, SectionTitle, ChapterTitle, TextbookID) VALUES
        ('SQL stands for Structured Query Language.', 'This answer explains what SQL is.', 'C', 1, 1, 'Introduction', 'Basics of SQL', 1),
        ('A join combines records from two or more tables.', 'Describes the purpose of joins.', 'C', 2, 3, 'Inner Joins', 'Joins and Subqueries', 1);
        """
    ]

    try:
        for command in sql_commands:
            cursor.execute(command)
            print(f"Executed command:\n{command.strip()}\n")
        print("All tables created successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database_and_tables()
