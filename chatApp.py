from flask import Flask,redirect, request, render_template
import os.path
server = Flask(__name__)
import csv


def write_to_file(data):
   header = ['username' , 'password']
   filename = 'users.csv'
   with open(filename, 'w') as file:
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('\n')

def read_to_file(data, if_login):
   with open('users.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row[0] == data.name:
            if if_login:
               if row[0] == data.password:
                  return True
            else:
               return True
      return False

@server.route('/register' , methods=["GET", "POST"])
def homePage():
   if request.method == "POST":
      name = request.form['username']
      password = request.form['password']
      data=[name, password]
      if read_to_file(data,False):
         return render_template("login.html")
      else:
         write_to_file(data)
       



@server.route('/login' , methods=['GET', 'POST'])
def loginPage():
  if request.method == 'POST':
      name = request.form['username'],
      password = request.form['password']
      data=[name, password]
      if read_to_file(data,True):
         return render_template('lobbe.html')
      else:
         return render_template('register.html')
  


@server.route('/lobby', methods =["GET", "POST"])
def room():
   if request.method == 'POST':
        name = request.form["new_room"] 
        path = './rooms/example.txt'
        check_file = os.path.isfile(path)  
        file1 = open(path, "w")
        return name
   return render_template('lobby.html')

   

if __name__ == "__main__":
   server.run(host='0.0.0.0')

