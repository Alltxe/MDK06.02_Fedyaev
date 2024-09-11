from getpass import getpass

from mysql.connector import connect, Error

hostname = '5.183.188.132'

username = 'db_vgu_student '

password = ''

database = 'db_vgu_test'

try:
    connection = connect(

            host=hostname,

            user=username,

            password=password,
    )

    if connection.is_connected():
        print('ok')

except Error as e:

    print(e)

if connection.is_connected():
        connection.close()
        print("Closed")