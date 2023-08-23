from flask import Flask,redirect, request, render_template
from flask import Flask, request, render_template
import os.path
server = Flask(__name__)
import csv


def write_to_file(data):
   header = ['username' , 'password']
   filename = 'users.csv'
   with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('n')

def read_to_file(data):
   with open('users.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row.username == data:
            return False 
      return True

@server.route('/register' , methods=['GET', 'POST'])
def homePage():
   name = request.form['username'],
   password = request.form['password']
   if request.method == "POST":
         if read_to_file(name):
            data=[name, password]
            write_to_file(data)
         else:
            return render_template("login.html")



@server.route('/register' , methods=['GET', 'POST'])
def login():
  name = request.form['username'],
  password = request.form['password']


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

