from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('welcome.html')

if __name__ == "__main__":
	app.run(debug=True)


