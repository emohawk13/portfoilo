import csv
import mysql.connector

# Configuration values
SECRET_KEY = '648b858b3f3aec238f7e7c26eb824e487b52cefd8279369e'
MYSQL_HOST = '192.168.1.234'  # Replace with your MySQL host
MYSQL_PORT = 3306  # Replace with your MySQL port
MYSQL_USER = 'emohawk13'
MYSQL_PASSWORD = 'Dcap1203+'
MYSQL_DB = 'Portfolio'

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)
cursor = cnx.cursor()

# Specify the path to your CSV file
csv_file = 'CourseData.csv'

# Open the CSV file
with open(csv_file, 'r') as file:
    # Create a CSV reader
    csv_data = csv.reader(file)
    
    # Get the column titles
    header = next(csv_data)
    course_id_idx = header.index('Course_Id')
    devry_course_id_idx = header.index('Devry_Course_ID')
    course_class_idx = header.index('Course_Class')
    course_title_idx = header.index('Couse_Title')
    course_type_idx = header.index('Course_Type')
    course_progress_idx = header.index('Course_Progress')
    course_dis_idx = header.index('Couse_Dis')
    
    # Iterate over the CSV data and insert it into the database
    for row in csv_data:
        # Retrieve the values from the corresponding columns
        course_id = row[course_id_idx]
        devry_course_id = row[devry_course_id_idx]
        course_class = row[course_class_idx]
        course_title = row[course_title_idx]
        course_type = row[course_type_idx]
        course_progress = row[course_progress_idx]
        course_dis = row[course_dis_idx]
        
        # Write your INSERT statement with placeholders
        insert_query = "INSERT INTO EduContent (Course_Id, Devry_Course_ID, Course_Class, Couse_Title, Course_Type, Course_Progress, Couse_Dis) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        # Execute the INSERT statement
        cursor.execute(insert_query, (course_id, devry_course_id, course_class, course_title, course_type, course_progress, course_dis))
        
        # Commit the changes to the database
        cnx.commit()

# Close the database connection
cursor.close()
cnx.close()
