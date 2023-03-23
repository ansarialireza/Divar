import mysql.connector
mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='8569')
mycursor=mydb.cursor()

mycursor.execute("USE DIVAR;")
a=input()
b=input()
sql="SELECT * FROM advertising WHERE Price BETWEEN %s AND %s" % (a,b)


#name=input("Please enter car name : ")
#sql = "SELECT * FROM advertising WHERE name LIKE %s"%('\'%'+name+'%\'') 
#mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
