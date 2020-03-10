from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	names = {1: "Mark", 2: "Liping", 3: "Jordan", 4: "Michael"}
	name = names[random.randint(1,4)]
	return "Hello, " + name + "!!!!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
