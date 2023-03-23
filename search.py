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

def menu():
      print("Hi welcome to search menu!")
      print("Please select the desired option by entering the number :")
      print("1 : search by name ")
      print("2 : search by price ")
      print("3 : Exit")
while(True):
    menu()
    state=input()
    if state=='3':
          print("God Bye")
          break
    elif state=='1':
          search_by_name()
    elif state=='2':
          search_by_price()

