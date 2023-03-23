import mysql.connector
mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='8569')
mycursor=mydb.cursor()

mycursor.execute("USE DIVAR;")

def print_data(sql):
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x) 

def search_by_name():
  name=input("Please enter car name : ")
  sql = "SELECT * FROM advertising WHERE name LIKE %s"%('\'%'+name+'%\'')
  print_data(sql)

def search_by_price():
  a=int(input("Please enter Minimum Price : "))
  b=int(input("Please enter Maximum Price : "))
  print(a,b)
  sql="SELECT * FROM advertising WHERE Price BETWEEN %d AND %d" % (a,b)
  print_data(sql)

#search_by_name()
search_by_price()

