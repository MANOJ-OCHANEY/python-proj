# import csv

# def getuser(username,password):
#     users = {}
#     with open('users.csv') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             users[row['username']] = row['password']
#     print (users)
#     if username in users and users[username]==password :
#         return True
#     else:
#         return False

# print(getuser('manoj.o','pass'))
import data

data.addExpense('manoj.o','Savings','Other','May',5000)
print('Expense added')
