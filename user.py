import csv

def loaduser(name,email,username,password):
    user = {
    'name':name,
    'email':email,
    'username':username,
    'password':password }

    with open('users.csv', 'a') as f:
        fieldnames = ['name', 'email', 'username', 'password']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(user)

def getuser(username,password):
    users = {}
    with open('users.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users[row['username']] = row['password']


    if username in users and users[username]==password :
        return True
    else:
        return False

def usercheck(username):
    users = []
    with open('users.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row['username'])
    #print (users)

    if username in users:
        return True
    else:
        return False

def display(username,password):
    print(username,password)

#loaduser('Manoj Ochaney','manoj@gmail.com','manoj.o','pass')
#loaduser('Mohit Makhija','mohit@gmail.com','mohit.m','psw')
#print (usercheck('manoj.o'))
