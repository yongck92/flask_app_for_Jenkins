import pandas as pd
from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	df = pd.read_csv("Names.csv")
	name = df.query('ID==' + str(random.randint(1,4)))['Name'].to_string(index=False)
	return "Hello, " + name + "!"

if __name == '__main__':
    app.run(debug=True, host='0.0.0.0')
