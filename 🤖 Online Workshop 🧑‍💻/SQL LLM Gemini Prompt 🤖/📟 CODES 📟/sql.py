# pip install db-sqlite3
# pip install sqlite3
import sqlite3

#Connectt to SQlite
#Our database name: Naresh_it_student
connection=sqlite3.connect("Naresh_it_employee1.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

#create the table
#Our table name student
#Columns names are: name, course
table_info="""
Create table Naresh_it_employee1(employee_name varchar(30),
                    employee_role varchar(30),
                    employee_salary FLOAT);
"""
cursor.execute(table_info)

#Insert the records

cursor.execute('''Insert Into Naresh_it_employee1 values('Omkar Nallagoni','Data Science',75000)''')
cursor.execute('''Insert Into Naresh_it_employee1 values('Naresh','Data Science',90000)''')
cursor.execute('''Insert Into Naresh_it_employee1 values('Phani','Data Science',88000)''')
cursor.execute('''Insert Into Naresh_it_employee1 values('Naga babu','Data Engineer',50000)''')
cursor.execute('''Insert Into Naresh_it_employee1 values('Ajay','Data Engineer',35000)''')
cursor.execute('''Insert Into Naresh_it_employee1 values('Pawan','Data Engineer',60000)''')

#Disspaly ALl the records

print("The inserted records are")
data=cursor.execute('''Select * from Naresh_it_employee1''')
for row in data:
    print(row)

#Commit your changes int he databse
connection.commit()
connection.close()