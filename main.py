import random
import string
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"


@app.route("/admin")
def hello_world_admin():
    return "<p>Hello, Admin!!</p>"



@app.route("/password")
def generate_password():
    password_lenght = random.randint(10,20)
    pass_symbols = string.digits + string.ascii_lowercase + string.ascii_lowercase + "!#$%&/()>=?_+-"
    password = ''.join(random.choice(pass_symbols) for _ in range(password_lenght))
    return password



if __name__ =='__main__':
    app.run(
        'localhost', debug = True
    )

