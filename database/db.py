import pymysql

db_host = 'aws-mysql-instance.c9keuuk6q78a.us-east-2.rds.amazonaws.com'
db_user = 'admin'
db_password = 'AWSNicolas99!'
db_db = ''

def connectionSQL():
   try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password
        )
        
        print("Successfull connection to database")
    except:
        print("Error connecting to database")