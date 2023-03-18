import mysql.connector
from sklearn import tree
mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='8569')
mycursor=mydb.cursor()

mycursor.execute("USE DIVAR;")
mycursor.execute("SELECT * FROM advertising;")
result=(mycursor.fetchall())

x=[]#input
y=[]#output

for i in range(0,len(result)):
    x.append(result[i][1:])
    y.append(result[i][0])
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
print("ok")