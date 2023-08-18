import pymssql
try:
    conn = pymssql.connect(server='localhost1',user='Ravindra',database ='python', password="Ravi@123" )
    print('connection sucess') 
except Exception as e:
    print(e)
else:
    conn.close()
    print("connection closed")
finally:
    print("code executed sucessfully")