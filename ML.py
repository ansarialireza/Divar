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
    x.append(result[i][0:2])
    y.append(result[i][3])

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
new_data=[['pjw 206 typ 2, mdl 1399']]
#answer=clf.predict(new_data)
print(result)

