import openpyxl

wb = openpyxl.load_workbook('data.xlsx')
ws = wb['base']

rows = ws.rows
rows = tuple(rows)
months = {
    'January':3,
    'February':4,
    'March':5,
    'April':6,
    'May':7,
    'June':8,
    'July':9,
    'August':10,
    'September':11,
    'October':12,
    'November':13,
    'December':14 }

#print(months['May'])

def createSheet(uname):
    user = wb.copy_worksheet(ws)
    user.title = uname
    wb.save('data.xlsx')

def getRow(category,type_):
    for row in rows:
        if row[0].value==type_ and row[1].value==category:
            return row[0].row

#print(getRow('Savings','Saving'))

def addExpense(uname,category,type_,month,amt):
    ws = wb[uname]
    r = getRow(category,type_)
    c = months[month]
    cell = ws.cell(row=r,column=c)
    cell.value = amt
    wb.save('data.xlsx')

def table_income_data(uname):
    ws = wb[uname]
    rows = ws.rows
    rows = list(rows)
    incdata = []
    for row in rows:
        if row[1].value=='Income':
            temp = []
            temp.append(row[0].value)
            for i in range(2,14):
                temp.append(row[i].value)
            incdata.append(temp)

    return incdata

def table_expense_data(uname):
    ws = wb[uname]
    rows = ws.rows
    rows = list(rows)
    expdata = {
        'Savings':[],
        'Home':[],
        'Transportation':[],
        'Health':[],
        'Daily-living':[],
        'Entertainment':[] }
    for row in rows:
        if row[1].value in expdata:
            temp = []
            temp.append(row[0].value)
            for i in range(2,14):
                temp.append(row[i].value)
            expdata[row[1].value].append(temp)

    return expdata

def get_months():
    m = []
    for i in months:
        m.append(i)
    return m

#addExpense('manoj.o','Savings','Other','May',5000)
#print('Expense added')



#wb.save('data.xlsx')
