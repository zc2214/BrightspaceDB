import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="brightspaceDB"
)

mycursor = mydb.cursor()

def query1():
# 大一以上没有专业
    query = ''' SELECT Email
    FROM Students NATURAL JOIN Users
    WHERE Year > 1 AND Major = "Undecided"
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query2():
#F22有课的老师
    query = ''' SELECT Users.Lname
    FROM Users INNER JOIN Courses
    ON Users.NetID = Courses.Instructor
    WHERE Courses.Term = "F22"
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query3():
#算成绩 # change var
    query = ''' SELECT Net_ID, SUM(Final)
    FROM (SELECT Net_ID, QA_ID, Greade * Weight AS Final
    FROM Performance NATURAL JOIN QA
    WHERE Course_ID = "CSCI-UA-60") AS T
    GROUP BY Net_ID
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query4():
#HW2 讨论
    query = ''' SELECT NetID, Message, Topic, Replyto
    FROM Discussion
    WHERE COURSE_ID = "CSCI-UA-60" AND Time <
    (SELECT B_Date
    FROM QA
    WHERE COURSE_ID = "CSCI-UA-60" AND QA_name = "HW2")
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query5():
#每个admin 管理的 instructor
    query = '''SELECT Admins.NetID, Instructors.NetID, Admins.D_name 
    FROM Admins INNER JOIN Instructors
    ON Admins.D_name = Instructors.D_name
    WHERE Admins.A_rank = "Dept Head"
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query5():
#每个admin 管理的 instructor
    query = '''SELECT Admins.NetID, Instructors.NetID, Admins.D_name 
    FROM Admins INNER JOIN Instructors
    ON Admins.D_name = Instructors.D_name
    WHERE Admins.A_rank = "Dept Head"
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

def query5():
#最热门内容
    query = '''SELECT Con_name, D_count
    FROM Content
    WHERE COURSE_ID = "CSCI-UA-60" AND D_count >=
    (SELECT MAX(D_count) As Num
    FROM Content
    WHERE COURSE_ID = "CSCI-UA-60")
    '''

    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

if __name__ == "__main__":
    print(query5())

