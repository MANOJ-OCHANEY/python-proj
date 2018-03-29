from flask import Flask,render_template,request
import user


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signin',methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['psw']
	#user.display(username,password)
	if(user.getuser(username,password)):
		return 'Welcome '
	else:
		return 'User not registered'


@app.route('/signup',methods=['POST'])
def signup():
	name = request.form['name']
	email = request.form['email']
	username = request.form['username']
	password = request.form['psw']
	if user.usercheck(username):
		return 'Username already exists'
	else:
		user.loaduser(name,email,username,password)
		return 'Successfully registered'


@app.route('/wc')
def wc():
	return 'Welcome'

if __name__ == '__main__':
	app.run(debug=True)

