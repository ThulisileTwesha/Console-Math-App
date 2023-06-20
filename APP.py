def multiply(d, e):
    return d * e

def add(d, e):
    return d + e

def subtract(d, e):
    return d - e

def divide(d,e):
    return d / e
print("selection operation")
print("1. multiply")
print("2. add")
print("3. subtract")
print("4. divide")

question = input("What do you want to do?")
choice = input("Enter choice(1/2/3/4): ")

d = int(input('Enter 1st number'))
e = int(input('Enter 2nd number'))

if(choice == '1'):
    print(d, "*",  e,  "=", multiply(d, e))


if(choice == '2'):

    print(d, "+",  e,  "=", add(d, e))

if(choice == '3'):

    print(d, "-",  e,  "=", subtract(d, e))

if (choice == '4'):

    print(d, "/",  e,  "=", divide(d, e))






