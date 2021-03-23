from flask import Flask
from flask import render_template

import analysis

app = Flask(__name__)

x = analysis.myfunction()
g = x[1]
b = x[0]
acc= round(x[2],2)*100

@app.route("/")
def hello():
	return render_template('index.html', acc=acc)

@app.route("/good")
def good():
	print(type(g))
	return render_template('goodNews.html', good=g)

@app.route("/bad")
def bad():
	return render_template('badNews.html', bad=b)


if __name__ == "__main__":
    app.run()

