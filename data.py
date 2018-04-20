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

    t = total(incdata)
    incdata.append(t)
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

    for i in expdata:
        t = total(expdata[i])
        expdata[i].append(t)

    return expdata

def get_months():
    m = []
    for i in months:
        m.append(i)
    return m

def total(d):
    t = ['Total']
    for i in range(1,13):
        sum = 0
        for j in d:
            sum += j[i]
        t.append(sum)

    return t

def chart_data(uname):
    chtdata = {
        'Income':[],
        'Savings':[],
        'Home':[],
        'Health':[],
        'Transportation':[],
        'Entertainment':[],
        'Daily-living':[]
    }
    incdata = table_income_data(uname)
    expdata = table_expense_data(uname)

    incdata[-1].remove('Total')
    chtdata['Income'] = incdata[-1]
    for i in expdata:
        temp = expdata[i]
        temp[-1].remove('Total')
        chtdata[i] = temp[-1]

    return chtdata

def pie_data(uname):
    piedata = []
    chtdata = chart_data(uname)
    for i in chtdata:
        piedata.append(sum(chtdata[i])/12)

    return piedata

def final_amt(uname):
    piedata = pie_data(uname)
    temp1 = piedata[0]
    temp1 = float("%3.f" % temp1)
    piedata.pop(0)
    temp2 = sum(piedata)
    temp2 = float("%3.f" % temp2)
    temp = temp1-temp2
    return (temp1,temp2,temp)








#addExpense('manoj.o','Savings','Other','May',5000)
#print('Expense added')



#wb.save('data.xlsx')
