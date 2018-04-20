from flask import Flask,render_template,request,redirect,url_for
import user
import data


app = Flask(__name__)

uname = None
months = data.get_months()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signin',methods=['POST'])
def signin():
	global uname
	username = request.form['username']
	password = request.form['psw']
	#user.display(username,password)
	if(user.getuser(username,password)):
		#userdata = data.kuchtohfunc
		uname = username
		return redirect(url_for('dashboard',username=username))
	else:
		return 'Invalid username or password'

@app.route('/<username>')
def dashboard(username):
	name = user.getname(username)
	incdata = data.table_income_data(uname)
	expdata = data.table_expense_data(uname)
	chtdata = data.chart_data(uname)
	piedata = data.pie_data(uname)
	finalamt = data.final_amt(uname)
	return render_template('dashboard.html',name=name,incdata=incdata,expdata=expdata,months=months,chtdata=chtdata,piedata=piedata,finalamt=finalamt)

@app.route('/signup',methods=['POST'])
def signup():
	global uname
	name = request.form['name']
	email = request.form['email']
	username = request.form['username']
	password = request.form['psw']
	if user.usercheck(username):
		return 'Username already exists'
	else:
		user.register_user(name,email,username,password)
		data.createSheet(username)
		uname = username
		#userdata = data.kuchtohfunc
		return redirect(url_for('dashboard',username=username))

@app.route('/addExpense/<category>/<type_>',methods=['POST'])
@app.route('/addExpense/<category>',methods=['POST'])
def add_expense(category=None,type_=None):
	category = category
	amt = int(request.form['price'])
	month = request.form['month']
	#type_ = type_
	#if(type_==None):
	if(category == 'Income'):
		type_ = type_
	else:
		type_ = request.form['expense']

	# print(uname)
	# print(category)
	# print(type_)
	# print(month)
	# print(amt)
	data.addExpense(uname,category,type_,month,amt)
	return redirect(url_for('dashboard',username=uname))

@app.route('/signout')
def signout():
	global uname
	uname = None
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)

