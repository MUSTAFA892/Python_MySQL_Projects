from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',          # Replace with your MySQL username
    'password': 'mustafasMYSQL#123',      # Replace with your MySQL password
    'host': 'localhost',              # Replace with your MySQL host
    'database': 'student_info'  # Replace with your database name
}

def get_db_connection():
    return mysql.connector.connect(
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        database=db_config['database']
    )

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', students=students)

@app.route('/student/<int:student_id>')
def student_info(student_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    connection.close()
    return render_template('student_info.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
