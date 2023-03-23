import mysql.connector
import data_cleaner
def insert_to_database(val_list):
    mydb=mysql.connector.connect(host='127.0.0.1',user='root',password='8569')
    mycursor=mydb.cursor()


    mycursor.execute("DROP DATABASE Divar")
    mycursor.execute("create database Divar")
    mycursor.execute("USE Divar")
    # database crated and use
    # database craALTER DATABASE dbname CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_cise
    mycursor.execute("CREATE TABLE Advertising (name text,mileage text,price text,location text)")
    SQL="INSERT INTO Advertising (name,mileage,price,location) VALUES (%s,%s,%s,%s)"

    # table and column was crated
    #val_list=data_cleaner.convert_list(val_list)
    end_list=[x for x in val_list if len(x)==4]# just lenth 4
    for i in end_list:
        mycursor.execute(SQL,i)
    mydb.commit()
    print("Your Divar information has been saved in the database")
    mydb.close()


