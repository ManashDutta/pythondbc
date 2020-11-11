import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="macintosh",database="covid")
mycursor=mydb.cursor()
print("USE THE FOLLOWING OPTIONS TO PROCEED")
print("1 TO REGISTER( FOR NEW USERS) | 2 TO LOGIN")
op=int(input())
def inp():
    print("iaminp")
    email = input("Enter your mail_id to login")
    print(email)
    login_auth(email)

def login_auth(email):
    for i in mycursor:
        if i[1] == email:
            print("Login Successful !")
        else:
            print("Login Failed !")
            inp()
if op==1:
    u_name=input("Enter your name")
    email=input("Enter your mail_id")
    sql="insert into reg_users(u_name,email) values (%s,%s)"
    val=(u_name,email)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute("select * from reg_users")
    inp()
elif op==2:
    mycursor.execute("select * from reg_users")
    inp()
