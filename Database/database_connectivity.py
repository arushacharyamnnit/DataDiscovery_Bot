import mysql.connector
def DataUpdate(job,execution): 
     mydb = mysql.connector.connect(
          host="localhost",
           user="root",
            passwd="",
            database="user"  
     )
     mycursor = mydb.cursor()
     sql=''
     mycursor.execute(sql)
     
