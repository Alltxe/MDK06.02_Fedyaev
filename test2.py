import pymysql

hostname = '5.183.188.132'

username = 'db_vgu_student'

password = ''

database = 'db_vgu_test'


def query(connection):
    select_query = "SELECT * FROM country LIMIT 5"

    with connection.cursor() as cursor:
        cursor.execute(select_query)

        result = cursor.fetchall()

        for row in result:
            print(row)


myConnection = pymysql.connect(host=hostname, user=username, passwd=password, db=database)

query(myConnection)

myConnection.close()