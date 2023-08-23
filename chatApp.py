from flask import Flask,redirect, request, render_template
import os
server = Flask(__name__)
import csv


def write_to_file(data):
   header = ['username' , 'password']
   filename = 'users.csv'
   with open(filename, 'w') as file:
    for header in header:
        file.write(str(header)+', ')
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('\n')

def read_to_file(data):
   with open('users.csv', 'r') as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row.username == data:
            return False 
      return True

@server.route('/register' , methods=['GET', 'POST'])
def homePage():
    if request.method == "POST":
      name = request.form['username'],
      password = request.form['password']
      if read_to_file(name):
         data=[name, password]
         write_to_file(data)
      else:
         return render_template("login.html")
    return render_template('register.html')



@server.route('/login' , methods=['GET', 'POST'])
def loginPage():
  if request.method == 'POST':
       name = request.form['username'],
       password = request.form['password']
  return render_template('login.html')


@server.route('/lobby', methods =["GET", "POST"])
def room():
   if request.method == 'POST':
        new_room = request.form["new_room"] 
        path = "rooms/" + new_room + ".txt"
        if os.path.isfile(path):
           return "Error in rhe room name!"
        else:
           with open(path, 'w') as f:
              f.write("welcome")  
           rooms = os.listdir('rooms/')
               
   return render_template('lobby.html', room_names=rooms)



   

if __name__ == "__main__":
   server.run(host='0.0.0.0')

