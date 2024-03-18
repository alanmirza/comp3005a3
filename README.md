Alan Mirza, 101217710
1. make sure you have python installed, and PostgreSQL, and psycopg library for python, to install psycopg use: pip install psycopg
2. open PostgreSQL and start your own server, and create table named students and insert information into it as shown below:
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

3. open the python file comp3005a3.py in the db_connect function replace the dbname, user, password, host, and port number with your own PostgreSQL information
4. run the application using: python comp3005a3.py
5. the different functionalities you can test using the main function include default I've placed in the database
getAllStudents() #gets all students records
addStudent(first_name, last_name, email, enrollment_date) #adds a new student record
updateStudentEmail(student_id, new_email) #updates the email address of a specific student
deleteStudent(student_id) #deletes a student record using student ID
6. youtube video for application demonstration: https://youtu.be/OO2RaaX6hoI?si=Y03twqmEN_T3fYmJ
