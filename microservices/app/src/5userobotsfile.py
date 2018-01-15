from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
	return "Hello"

@app.route('/robots.txt/')
def error():
#   return redirect("http://httpbin.org/deny")
	return render_template("error.html")
if __name__ == "__main__":
   app.run()


