import pymysql

db_host = 'aws-mysql-instance.c9keuuk6q78a.us-east-2.rds.amazonaws.com'
db_user = 'admin'
db_password = 'AWSNicolas99!'
db_database = 'test_rds_database'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        
        print("Successfull connection to database")
        return connection_sql
        
    except:
        print("Error connecting to database")
        return None
        
def add_user(id, name, lastname, birthday):
    query_sql  = "INSERT INTO " + db_table + " (id, name, lastname, birthday) VALUES ("+id+ ", '"+name+ "', '"+lastname+"', '"+birthday+"')"
    #Obtener return de la función
    connection_sql = connectionSQL()

    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(query_sql)
            connection_sql.commit()
            connection_sql.close()
            print("User added")
        else:
            print("Error to connecting to database")
    except Exception as err:
        print(err)

def consult_user(id):
    query_sql = "SELECT * FROM " + db_table + " WHERE id = " + id
    #Obtener return de la función
    connection_sql = connectionSQL()
    
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(query_sql)
            user_data = cursor.fetchall()
            connection_sql.close()
            
            return user_data
        else:
            print("Error to connecting to database")
    except Exception as err:
        print(err)