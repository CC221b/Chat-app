from flask import Flask, render_template
server = Flask(__name__)

@server.route('/templates/register', '/register')
def register():

   return "register"


if __name__ == "__main__":
   server.run(host='0.0.0.0')

