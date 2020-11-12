#________________________________________________________________________
import mysql.connector as mc
dbc=mc.connect(host="localhost",user="root",passwd="macintosh",database="covid")
cursor=dbc.cursor()
#________________________________________________________________________

def user_auth():
    email = input("Enter your email to login")
    fetch_query = "select * from reg_users;"
    cursor.execute(fetch_query)
    for i in cursor:
        if i[1] == email:
            print("Login Successful !")
            count = 1
            break
    if count == 0:
        print("Login Error !")

print("Enter 1 to Login or 2 to Register for new users")
inp=int(input())
count=0
if inp==1:
   user_auth()

elif inp==2:
    name = input("Enter your name")
    email = input("Enter your email")
    query = "insert into reg_users values('{}','{}');".format(name, email)
    print(query)
    cursor.execute(query)
    dbc.commit()
    user_auth()
