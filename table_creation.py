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
        "CREATE DATABASE IF NOT EXISTS sql5740507;",
        "USE sql5740507;",
        """
        CREATE TABLE IF NOT EXISTS ETextbook (
            ID INT PRIMARY KEY,
            Title VARCHAR(255)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Chapter (
            Title VARCHAR(255),
            Number VARCHAR(6),
            TextbookID INT,
            PRIMARY KEY (TextbookID, Title),
            FOREIGN KEY (TextbookID) REFERENCES ETextbook(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Section (
            Title VARCHAR(255),
            Number INT,
            TextbookID INT,
            ChapterTitle VARCHAR(255),
            PRIMARY KEY (TextbookID, ChapterTitle, Title),
            FOREIGN KEY (TextbookID, ChapterTitle) REFERENCES Chapter(TextbookID, Title)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ContentBlock (
            Type CHAR(1),
            ID INT,
            DisplayOrder INT,
            Content VARCHAR(255),
            SectionTitle VARCHAR(255),
            TextbookID INT,
            ChapterTitle VARCHAR(255),
            Hidden BOOL,
            PRIMARY KEY (TextbookID, ChapterTitle, SectionTitle, ID),
            FOREIGN KEY (TextbookID, ChapterTitle, SectionTitle) REFERENCES Section(TextbookID, ChapterTitle, Title)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Activity (
            Question VARCHAR(255),
            ID INT,
            ContentID INT,
            SectionTitle VARCHAR(255),
            ChapterTitle VARCHAR(255),
            TextbookID INT,
            Hidden BOOL,
            PRIMARY KEY (TextbookID, ChapterTitle, SectionTitle, ID),
            FOREIGN KEY (TextbookID, ChapterTitle, SectionTitle, ContentID) REFERENCES ContentBlock(TextbookID, ChapterTitle, SectionTitle, ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Role (
            Role VARCHAR(10) PRIMARY KEY
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS User (
            ID VARCHAR(8) PRIMARY KEY,
            FirstName VARCHAR(255),
            LastName VARCHAR(255),
            Email VARCHAR(255),
            Password VARCHAR(255),
            Role VARCHAR(10),
            FOREIGN KEY (Role) REFERENCES Role(Role)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Course (
            ID VARCHAR(255) PRIMARY KEY,
            Title VARCHAR(255),
            StartDate DATE,
            EndDate DATE,
            Type CHAR(1),
            Faculty VARCHAR(8),
            ETextbookID INT,
            FOREIGN KEY (ETextbookID) REFERENCES ETextbook(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Student (
            ID VARCHAR(8) PRIMARY KEY,
            UserID VARCHAR(8),
            CourseID VARCHAR(6),
            TotalPoints INT,
            ParticipationPoints INT,
            FOREIGN KEY (UserID) REFERENCES User(ID),
            FOREIGN KEY (CourseID) REFERENCES Course(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS CourseEnrollment (
            CourseID VARCHAR(8),
            StudentID VARCHAR(8),
            EnrollmentStatus VARCHAR(6),
            PRIMARY KEY (StudentID, CourseID),
            FOREIGN KEY (StudentID) REFERENCES Student(ID),
            FOREIGN KEY (CourseID) REFERENCES Course(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ActiveCourse (
            CourseID VARCHAR(7) PRIMARY KEY,
            Token CHAR(7),
            Capacity INT,
            Enrollment INT DEFAULT 0,
            FOREIGN KEY (CourseID) REFERENCES Course(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS EvaluationCourse (
            CourseID VARCHAR(7) PRIMARY KEY,
            EvaluationMethod VARCHAR(255),
            TotalMarks INT,
            FOREIGN KEY (CourseID) REFERENCES Course(ID)
        );
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
        CREATE TABLE IF NOT EXISTS Faculty (
            FacultyID VARCHAR(8) PRIMARY KEY,
            UserID VARCHAR(8),
            FOREIGN KEY (UserID) REFERENCES User(ID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ActivityScore (
            ActivityScoreID VARCHAR(8),
            StudentID VARCHAR(8),
            ActivityID INT,
            ContentID INT,
            SectionTitle VARCHAR(255),
            ChapterTitle VARCHAR(255),
            TextbookID INT,
            Score INT,
            Timestamp DATETIME,
            FOREIGN KEY (StudentID) REFERENCES Student(ID),
            FOREIGN KEY (TextbookID, ChapterTitle, SectionTitle, ContentID, ActivityID) REFERENCES Activity(TextbookID, ChapterTitle, SectionTitle, ContentID, ID),
            PRIMARY KEY (TextbookID, ChapterTitle, SectionTitle, ContentID, ActivityID, ActivityScoreID)
        );
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
        CREATE TABLE IF NOT EXISTS Answer (
            Text VARCHAR(255),
            Description VARCHAR(255),
            Type CHAR(1),
            ActivityID INT,
            ContentID INT,
            SectionTitle VARCHAR(255),
            ChapterTitle VARCHAR(255),
            TextbookID INT,
            PRIMARY KEY (TextbookID, ChapterTitle, SectionTitle, ContentID, ActivityID),
            FOREIGN KEY (TextbookID, ChapterTitle, SectionTitle, ContentID, ActivityID) REFERENCES Activity(TextbookID, ChapterTitle, SectionTitle, ContentID, ID)
        );
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
