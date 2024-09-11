import mysql.connector

hostname = '5.183.188.132'

username = 'db_vgu_student'

password = ''

database = 'db_vgu_test'


def query(connection):
    select_query = "SELECT * FROM category LIMIT 5"

    cursor = connection.cursor()
    cursor.execute(select_query)

    result = cursor.fetchall()

    for row in result:
        print(row)


myConnection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)

query(myConnection)

myConnection.close()