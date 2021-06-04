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
     sql1='SELECT root_job_name FROM matching_table where other_job_name="{0}";'.format(job['JOB_NAME']) 
     mycursor.execute(sql1)
     ans1=mycursor.fetchall()
     # print(ans1[0][0])
     sql='SELECT * from job where JOB_NAME="{0}";'.format(ans1[0][0])
     mycursor.execute(sql)
     ans=mycursor.fetchall()
     
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
     
