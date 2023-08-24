from flask import Flask,redirect, request, render_template
import os
import csv
import base64
server = Flask(__name__)

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
            return redirect("login")
        else:
            return redirect("login")
    return render_template("register.html")

       

@server.route('/login' , methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
      name = request.form['username'],
      password = request.form['password']
      if USERS.get(name) == password:
            return redirect('lobby')
      else:
            return redirect('register')
  return render_template('login.html')

  
@server.route('/lobby', methods =["GET", "POST"])
def room():
   if request.method == 'POST':
        new_room = request.form["new_room"] 
        if new_room:
             path = "rooms/" + new_room + ".txt"
             if os.path.isfile(path):
                 return "Error in rhe room name!"
             else:
                 with open(path, 'w') as f:
                     f.write("welcome")  
   rooms = os.listdir('rooms/')         
   return render_template('lobby.html', room_names=rooms)



   
#   @app.route("/chat/<room>", methods=["GET", "POST"])
# def chat(room):
#     if request.method == "POST":
#         message = request.form["msg"]
#         if message:
#             room_path = os.path.join(ROOMS_DIR, f"{room}.txt")
#             with open(room_path, "a") as room_file:
#                 timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#                 room_file.write(f"{timestamp} {session['username']}: {message}\n")
#     with open(os.path.join(ROOMS_DIR, f"{room}.txt"), "r") as room_file:
#         chat_content = room_file.read()
#     return render_template("chat.html", room=room, chat_content=chat_content)



   

if __name__ == "__main__":
   server.run(host='0.0.0.0', debug = True)

