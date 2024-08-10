from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="10.128.0.7",
        user="test",
        password="Test@123",
        database="sample_db"
    )

form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Data Entry</title>
</head>
<body>
    <h1>Enter Student Data</h1>
    <form method="POST">
        <label for="name">Student Name:</label><br>
        <input type="text" id="name" name="student_name" required><br><br>
        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required><br><br>
        <label for="grade">Grade:</label><br>
        <input type="text" id="grade" name="grade" required><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_name = request.form['student_name']
        age = request.form['age']
        grade = request.form['grade']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO student_data (student_name, age, grade) VALUES (%s, %s, %s)",
            (student_name, age, grade)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return "Student data submitted successfully!"

    return render_template_string(form_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
