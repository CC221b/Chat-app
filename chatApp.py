from flask import Flask,redirect, request, render_template, session
from flask_session import Session
import os
import csv
import base64
import datetime
server = Flask(__name__)
server.config["SESSION_PERMANENT"] = False
server.config["SESSION_TYPE"] = "filesystem"
Session(server)

ROOMS_DIR = os.getenv("ROOMS_DIR", "rooms")

def decode_password(encoded_password):
    decoded_b = base64.b64decode(encoded_password.encode('utf-8'))
    return decoded_b.decode('utf-8')

def encode_password(decoded_password):
    encoded_b = base64.b64encode(decoded_password.encode('utf-8'))
    return encoded_b.decode('utf-8')

USERS = {}
with open("users.csv", "r") as users_file:
    for line in users_file:
        parts = line.strip().split(",", 1)
        if len(parts) == 2:
            username, encoded_password = parts
            password = encoded_password
            #password = decode_password(encoded_password)
            USERS[username] = password

@server.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username not in USERS:
            #encoded_password = encode_password(password)
            encoded_password = password
            USERS[username] = encoded_password
            with open("users.csv", "a") as users_file:
                users_file.write(f"{username},{encoded_password}\n")
            session["username"] = request.form.get("username")
            return redirect("lobby")
        else:
            return redirect("login")
    return render_template("register.html")

       

@server.route('/login' , methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      name = request.form['username'],
      password = request.form['password']
      if USERS.get(name) == password:
            session["username"] = request.form.get("username")
            return redirect('lobby')
      else:
            return redirect('register')
  return render_template('login.html')

  
@server.route('/lobby', methods =["GET", "POST"])
def room():
   if request.method == 'POST':
        new_room = request.form["new_room"] 
        if new_room:
             room_path = os.path.join(ROOMS_DIR, f"{new_room}.txt")
             if os.path.isfile(room_path):
                 return "Error in rhe room name!"
             else:
                 with open(room_path, 'w') as f:
                     f.write("welcome")  
   rooms = os.listdir('rooms/')         
   return render_template('lobby.html', room_names=rooms)
 
@server.route("/chat/<room>", methods=["GET", "POST"])
def chat(room):
    return render_template("chat.html", room=room)


@server.route("/api/chat/<room>", methods=["GET", "POST"])
def chat_room(room):
   chat_content = ""
   if request.method == "POST":
        message = request.form["msg"]
        if message:
            room_path = os.path.join(ROOMS_DIR, f"{room}")
            with open(room_path, "a") as room_file:
                timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                room_file.write(f"{timestamp} {session.get('username')}: {message}\n")
   with open(os.path.join(ROOMS_DIR, f"{room}"), "r") as room_file:
      room_file.seek(0)
      chat_content = room_file.read()
   return chat_content

# @server.route('/api/chat/<room>', methods=['GET','POST'])
# def update_chat(room):
#     room_files_path = "rooms/"
#     if request.method == 'POST':
#         message = request.form['msg']
#         username = session['username']

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # Append the message to the room's unique .txt file
#         with open(f'{room_files_path}{room}.txt', 'a', newline='') as file:
#             file.write(f'[{timestamp}] {username}: {message}\n')
            
#     with open(f'{room_files_path}{room}.txt', 'r' ) as file:
#         file.seek(0)
#         messages = file.read()  
#     return messages.split('\n')


if __name__ == "__main__":
   server.run(host='0.0.0.0', debug = True)

