#######a.Setup the mysql database - Create the table (E.g Student) and fields (E.g. Student details: Name, Roll No, Department, ...)
#######b. Create the xml file (E.g. Student details: Name, Roll No, Department,...)
#######c. Convert to json format
#######d. Insert the data into the database
#######e. Query the database and export the data into excel

################### connecting to database and Creating table

################## Converting xml file to json file
import xmltodict
import json
import mysql.connector

with open("students.xml", "r") as xml_file:
    xml_data = xml_file.read()
xml_dict = xmltodict.parse(xml_data)

json_data = json.dumps(xml_dict)

with open('students.json', 'w') as json_file:
    json_file.write(json_data)

################### Insert the json data to MYSQLdatabase
import mysql.connector
import json

with open("students.json", "r") as json_file:
    json_data = json_file.read()
data = json.loads(json_data)

for student in data['students']['student']:
    sql = "INSERT INTO students (name, rollno, department, college, Grade) VALUES (%s, %s, %s, %s, %s)"
    val = (student["name"], student["rollno"], student["department"], student["college"], student["Grade"])
    cur.execute(sql,val)
cnct.commit()

################### querying the database
cur.execute('SELECT * FROM students')
result = cur.fetchall()
  # Printing all records or rows from the table. 
for all in result:
  print(all)

################## Export the Data to Excel
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Root@localhost/db2')
df = pd.read_sql('SELECT * FROM students', con=engine)
df.to_excel("students.xlsx",index=False)
