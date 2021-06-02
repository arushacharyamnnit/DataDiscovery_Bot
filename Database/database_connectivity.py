import mysql.connector
def DataUpdate(job,execution):
     # print(job) 
     mydb = mysql.connector.connect(
          host="localhost",
           user="root",
            passwd="",
            database="user"
     )
     
     mycursor = mydb.cursor()
     sql='SELECT * from job where JID="{0}";'.format(job['JID'])
     mycursor.execute(sql)
     ans=mycursor.fetchall()
     # print(ans[0])
     Dict={}
     cnt=0
     for i,j in job.items():
          if j!=0:
               Dict[i]=ans[0][cnt]
          cnt=cnt+1     
     # sql='SELECT * from execution_details where JOB_NAME="{0}";'.format(execution['JOB_NAME'])
     # mycursor.execute(sql)
     # mycursor.fetchall()
     # for i,j in execution.items():
     #      if j!=0:
     #           Dict[i]=j
     print(Dict)          

     return  Dict
     
