import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="brightspaceDB"
)

mycursor = mydb.cursor()

createUsers = '''CREATE TABLE IF NOT EXISTS  Users (
                            NetID VARCHAR(10) NOT NULL PRIMARY KEY,
                            Email VARCHAR(50),
                            Number VARCHAR(10),
                            Birth Date,
                            Gender CHAR(1),
                            Fname VARCHAR(50),
                            Mname VARCHAR(50),
                            Lname VARCHAR(50)
                            );
                            '''
mycursor.execute(createUsers)


with open("Users.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Users VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\"," + record[2] + ",\"" + record[
            3] +"\",\""+record[4]+"\",\""+record[5]+ "\",\"" + record[6]+"\",\"" + record[7]+"\""+")"
        mycursor.execute(line)
mydb.commit()


createStudents = '''CREATE TABLE IF NOT EXISTS  Students (
                            NetID VARCHAR(10) NOT NULL REFERENCES Users(NetID),
                            Major VARCHAR(50) NOT NULL,
                            Year REAL,
                            GPA REAL,
                            PRIMARY KEY (NetID, Major)
                            );
                            '''
mycursor.execute(createStudents)


with open("Students.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Students VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\"," + record[2] + "," + record[
            3]+")"
        mycursor.execute(line)
mydb.commit()


createDept = '''CREATE TABLE IF NOT EXISTS  Dept (
                            D_name VARCHAR(50) NOT NULL PRIMARY KEY,
                            School VARCHAR(50),
                            HEAD_ID VARCHAR(10) REFERENCES Users(NetID)
                            );
                            '''
mycursor.execute(createDept)


with open("Dept.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Dept VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\",\"" + record[2] + "\"" + ")"
        mycursor.execute(line)
mydb.commit()


createAdmins = '''CREATE TABLE IF NOT EXISTS  Admins (
                            NetID VARCHAR(10) NOT NULL PRIMARY KEY REFERENCES Users(NetID),
                            A_rank VARCHAR(50),
                            D_name VARCHAR(50) REFERENCES Dept(D_name)
                            );
                            '''
mycursor.execute(createAdmins)


with open("Admins.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Admins VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\",\"" + record[2] + "\"" + ")"
        mycursor.execute(line)
mydb.commit()


createInstructors = '''CREATE TABLE IF NOT EXISTS  Instructors (
                            NetID VARCHAR(10) NOT NULL PRIMARY KEY REFERENCES Users(NetID),
                            A_rank VARCHAR(50),
                            D_name VARCHAR(50) REFERENCES Dept(D_name)
                            );
                            '''
mycursor.execute(createInstructors)


with open("Instructors.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Instructors VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\",\"" + record[2] + "\"" + ")"
        mycursor.execute(line)
mydb.commit()


createCourses = '''CREATE TABLE IF NOT EXISTS  Courses (
                            Course_ID VARCHAR(20) NOT NULL PRIMARY KEY,
                            C_name VARCHAR(50),
                            Term VARCHAR(10),
                            S_date DATE,
                            E_date DATE,
                            ZoomID REAL,
                            D_name VARCHAR(50) REFERENCES Dept(D_name),
                            Instructor VARCHAR(10) REFERENCES Instructors(NetID)
                            );
                            '''
mycursor.execute(createCourses)


with open("Courses.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Courses VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\",\"" + record[2]+ "\",\"" + record[3] +\
            "\",\"" + record[4] +"\"," + record[5] +",\"" + record[6] +"\",\"" + record[7] +"\")"
        mycursor.execute(line)
mydb.commit()


createEnrollment = '''CREATE TABLE IF NOT EXISTS  Enrollment (
                            NetID VARCHAR(10) NOT NULL REFERENCES Students(NetID),
                            Course_ID VARCHAR(20) NOT NULL REFERENCES Courses(Course_ID),
                            PRIMARY KEY (NetID, Course_ID)
                            );
                            '''
mycursor.execute(createEnrollment)


with open("Enrollment.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Enrollment VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\")"
        mycursor.execute(line)
mydb.commit()


createContent = '''CREATE TABLE IF NOT EXISTS Content (
                            Course_ID VARCHAR(20) NOT NULL REFERENCES Courses(Course_ID),
                            Con_ID REAL NOT NULL,
                            Con_name VARCHAR(50),
                            D_count REAL,
                            U_time DATE,
                            Uploader VARCHAR(10) REFERENCES Instructors(NetID),
                            PRIMARY KEY (Course_ID, Con_ID)
                            );
                            '''
mycursor.execute(createContent)


with open("Content.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Content VALUES (" + "\""+record[0] + "\"," + record[1] + ",\"" + record[2] + "\","+\
            record[3]+",\""+record[4]+"\",\""+record[5]+"\")"
        mycursor.execute(line)
mydb.commit()


createQA = '''CREATE TABLE IF NOT EXISTS QA (
                            Course_ID VARCHAR(20) NOT NULL REFERENCES Courses(Course_ID),
                            QA_ID REAL NOT NULL,
                            QA_name VARCHAR(50),
                            Weight REAL,
                            B_date DATETIME,
                            Duration REAL,
                            Due DATETIME,
                            PRIMARY KEY (Course_ID, QA_ID)
                            );
                            '''
mycursor.execute(createQA)


with open("QA.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        if record[5] == "NULL":
            line = "INSERT INTO QA VALUES (" + "\""+record[0] + "\"," + record[1] + ",\"" + record[2] + "\","+\
            record[3]+",\""+record[4]+"\","+ "NULL" +",\""+record[6]+"\")"
        else:
            line = "INSERT INTO QA VALUES (" + "\""+record[0] + "\"," + record[1] + ",\"" + record[2] + "\","+\
            record[3]+",\""+record[4]+"\","+ record[5] +",\""+record[6]+"\")"
        mycursor.execute(line)
mydb.commit()


createPerformance = '''CREATE TABLE IF NOT EXISTS Performance (
                            Net_ID VARCHAR(10) NOT NULL REFERENCES Students(Net_ID),
                            Course_ID VARCHAR(20) NOT NULL REFERENCES Courses(Course_ID),
                            QA_ID REAL NOT NULL REFERENCES QA(QA_ID),
                            Greade REAL,
                            PRIMARY KEY (Net_ID, Course_ID, QA_ID)
                            );
                            '''
mycursor.execute(createPerformance)


with open("Performance.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        line = "INSERT INTO Performance VALUES (" + "\""+record[0] + "\",\"" + record[1] + "\"," + record[2] + ","+\
            record[3]+")"
        mycursor.execute(line)
mydb.commit()

createDiscussion = '''CREATE TABLE IF NOT EXISTS Discussion (
                            Course_ID VARCHAR(20) NOT NULL REFERENCES Courses(Course_ID),
                            Dis_ID REAL NOT NULL,
                            Message VARCHAR(500),
                            Topic VARCHAR(100),
                            Time DATETIME,
                            Replyto REAL REFERENCES Discussion(Dis_ID),
                            NetID VARCHAR(10) REFERENCES Users(Net_ID),
                            PRIMARY KEY (Course_ID, Dis_ID)
                            );
                            '''
mycursor.execute(createDiscussion)

with open("Discussion.csv", "r") as ip:
    csv_reader = csv.reader(ip)
    next(csv_reader)
    for record in csv_reader:
        if record[-2] == "NULL":
            line = "INSERT INTO Discussion VALUES (" + "\""+record[0] + "\"," + record[1] + ",\"" + record[2] + "\",\""+\
            record[3]+"\",\""+record[4]+"\","+"NULL"+",\""+record[6]+"\""+")"
        else:
            line =  "INSERT INTO Discussion VALUES (" + "\""+record[0] + "\"," + record[1] + ",\"" + record[2] + "\",\""+\
            record[3]+"\",\""+record[4]+"\","+record[5]+",\""+record[6]+"\""+")"
        mycursor.execute(line)
mydb.commit()
