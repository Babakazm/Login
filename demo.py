# user = {'name':'', 'age': , 'password':'' , 'email': '', 'ID': '' }
import _sqlite3
from random import randint
import uuid

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)

five_digit_number = random_with_N_digits(5)
print(five_digit_number)

conn = _sqlite3.connect("demo.db")
cursor =conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
           
               ID_number INTEGER,
               name TEXT,
               age INTEGER,
               password TEXT,
               email TEXT,
               department TEXT 
    )
''')
user = []
def create_user ():
    name = input ("Please insert your name: ")
    age = int (input ("How old are you? "))
    password = input ("Please set a password: ")
    email = input ("Please insert your email address: ")
    ID_number = five_digit_number
    department = input ("Please select the department you are working at: ")
    user.append({"User ID": ID_number, "Username":name,"Age":age, "Password": password,"Email Address":email})
    cursor.execute ('INSERT INTO users2 (ID_number, name, age, password, email, department) VALUES (?,?,?,?,?,?)', (ID_number, name, age, password, email, department))
    conn.commit()
   
    print(f"User {user} added successfully!\n{user}\n")

create_user()

conn.close()
print (user)

