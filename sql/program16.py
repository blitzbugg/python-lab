# 1)  Create a Sqlite 
import sqlite3 
conn=sqlite3.connect('macfast.db') 
print("Opened database") 
sql="create table student(rollno int(3),name varchar(30),mark int(3))" 
conn.execute(sql) 
print("Table created") 
conn.close() 
 
# 2) Insert Data into Sqlite 
import sqlite3 
conn=sqlite3.connect('macfast.db') 
print("Opened database") 
while 1: 
    rollno=input("enter rollno(enter 0 for exit):") 
    if int(rollno)==0: 
        break 
    name=input("Enter name:") 
    mark=input("Enter mark") 
    sql="insert into student values(%s,'%s',%s)\n"%(rollno,name,mark) 
    print(sql) 
    conn.execute(sql) 
    conn.commit() 
    print("\nRecords inserted") 
    conn.close()


# 3) Display Data in Sqlite 
import sqlite3 
conn=sqlite3.connect('macfast.db') 
print('opened database') 
print('displaying data') 
print("\n............") 
result=conn.execute("select * from student") 
print("Rollno|Name|Marks") 
print("\n............") 
for i in result: 
    print("%6s|%-15s|%3s"%(i[0],i[1],i[2])) 
print("\n...........") 
conn.close() 
 
# 4) Delete Data in Sqlite 
import sqlite3 
conn=sqlite3.connect('macfast.db') 
print("opened database") 
print("Deleting data") 
print("\n..........") 
result=conn.execute('''DELETE from student where rollno=3;''') 
print("Rollno|Name|Marks") 
print("\n..........") 
data=conn.execute("select * from student") 
for i in data: 
    print(i) 
print("\n.........") 
conn.commit() 
conn.close() 