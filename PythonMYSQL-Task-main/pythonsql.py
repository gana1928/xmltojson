#######a.Setup the mysql database - Create the table (E.g Student) and fields (E.g. Student details: Name, Roll No, Department, ...)
#######b. Create the xml file (E.g. Student details: Name, Roll No, Department,...)
#######c. Convert to json format
#######d. Insert the data into the database
#######e. Query the database and export the data into excel

################### connecting to database and Creating table
import mysql.connector
cnct = mysql.connector.connect(host='localhost',user='root',password='Root',database='db2')
cur=cnct.cursor()
s="CREATE TABLE students(name varchar(15),rollno varchar(5),department varchar(20), college varchar(20), Grade varchar(20))"
cur.execute(s)
cnct.commit()

################### writing xml file
import xml.etree.ElementTree as ET
# Create the root element
root = ET.Element("students")
# Create the child elements
student1 = ET.SubElement(root, "student")
name1 = ET.SubElement(student1, "name")
name1.text = "snehith"
rollno1 = ET.SubElement(student1, "rollno")
rollno1.text = "13"
dept1 = ET.SubElement(student1, "department")
dept1.text = "Electronics"
coll1 = ET.SubElement(student1, "college")
coll1.text = "BIET"
Grad1 = ET.SubElement(student1, "Grade")
Grad1.text = "A+"

student2 = ET.SubElement(root, "student")
name2 = ET.SubElement(student2, "name")
name2.text = "Shreya"
rollno2 = ET.SubElement(student2, "rollno")
rollno2.text = "15"
dept2 = ET.SubElement(student2, "department")
dept2.text = "Civil"
coll2 = ET.SubElement(student2, "college")
coll2.text = "BITM"
Grad2 = ET.SubElement(student2, "Grade")
Grad2.text = "A+"

student3 = ET.SubElement(root, "student")
name3 = ET.SubElement(student3, "name")
name3.text = "Sai"
rollno3 = ET.SubElement(student3, "rollno")
rollno3.text = "19"
dept3 = ET.SubElement(student3, "department")
dept3.text = "Computer Science"
coll3 = ET.SubElement(student3, "college")
coll3.text = "JSS College"
Grad3 = ET.SubElement(student3, "Grade")
Grad3.text = "B"

student4 = ET.SubElement(root, "student")
name4 = ET.SubElement(student4, "name")
name4.text = "Manu"
rollno4 = ET.SubElement(student4, "rollno")
rollno4.text = "28"
dept4 = ET.SubElement(student4, "department")
dept4.text = "Textile"
coll4 = ET.SubElement(student4, "college")
coll4.text = "CMR College"
Grad4 = ET.SubElement(student4, "Grade")
Grad4.text = "D"

student5 = ET.SubElement(root, "student")
name5 = ET.SubElement(student5, "name")
name5.text = "Pooja"
rollno5 = ET.SubElement(student5, "rollno")
rollno5.text = "18"
dept5 = ET.SubElement(student5, "department")
dept5.text = "EEE"
coll5 = ET.SubElement(student5, "college")
coll5.text = "RV College"
Grad5 = ET.SubElement(student5, "Grade")
Grad5.text = "C+"

student6 = ET.SubElement(root, "student")
name6 = ET.SubElement(student6, "name")
name6.text = "Rachana"
rollno6 = ET.SubElement(student6, "rollno")
rollno6.text = "19"
dept6 = ET.SubElement(student6, "department")
dept6.text = "Electronics"
coll6 = ET.SubElement(student6, "college")
coll6.text = "Dayanand Sagar"
Grad6 = ET.SubElement(student6, "Grade")
Grad6.text = "A"

student7 = ET.SubElement(root, "student")
name7 = ET.SubElement(student7, "name")
name7.text = "Suchitha"
rollno7 = ET.SubElement(student7, "rollno")
rollno7.text = "19"
dept7 = ET.SubElement(student7, "department")
dept7.text = "Computer Science"
coll7 = ET.SubElement(student7, "college")
coll7.text = "AMC College"
Grad7 = ET.SubElement(student7, "Grade")
Grad7.text = "B+"
# Creates the XML file
tree = ET.ElementTree(root)
tree.write("students.xml")

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
