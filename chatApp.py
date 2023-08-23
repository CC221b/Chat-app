from flask import Flask, render_template
server = Flask(__name__)

# @server.route('/register' , methods=['GET', 'POST'])
# def register():
#    name = request.form('name')
#    user = {
#         "name": request.form.get('name'),
#         "password": request.form.get('password'),
#    }


# @server.route('/register' , methods=['GET', 'POST'])
# def login():

#    username = request.args.get('username')
#    password = request.args.get('password')

@server.route('/register')
def homePage():
   return render_template('register.html')

@server.route('/login')
def loginPage():
   return render_template('login.html')

# @server.route('/logout')
# def homePage():
#    return render_template('register.html')

@server.route('/lobby')
def room():
   return render_template('lobby.html')

if __name__ == "__main__":
   server.run(host='0.0.0.0')
