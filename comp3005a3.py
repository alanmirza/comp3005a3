#Alan Mirza, 101217710
import psycopg

def db_connect():
    #Create a connection to the database
        conn = psycopg.connect(
            "dbname='postgres' user='alanmirza' password='A53005' host='localhost' port='5430'"
        )
        return conn

def getAllStudents():
    #Retrieve all student records from the database
    conn = db_connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            for record in cur.fetchall():
                print(record)
        conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    #Insert a new student record into the database
    conn = db_connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date)
            )
            conn.commit()
        conn.close()

def updateStudentEmail(student_id, new_email):
    #Update a student's email address
    conn = db_connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE students SET email = %s WHERE student_id = %s",
                (new_email, student_id)
            )
            conn.commit()
        conn.close()

def deleteStudent(student_id,):
    #Delete a student record from the database
    conn = db_connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM students WHERE student_id = %s",(student_id,)
            )
            conn.commit()
        conn.close()

# Main function to execute the operations primary functionality
def main():
   getAllStudents() #you should change this according to the functionality you want to use ex. addStudent(first_name, last_name, email, enrollment_date) and replace the inside parameters with what you require, same with UpdateStudentEmail(new_email, student_id) replace parameters inside, and deleteStudent() sepcify the student number you want to delete

if __name__ == "__main__":
    main() # Ensures the operation runs only when executed directly