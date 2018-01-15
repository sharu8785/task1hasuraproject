
from flask import Flask, request, render_template , make_response
app=Flask(__name__)
@app.route('/getcookie')
def getcookie():
	myname=request.cookies.get('myname')
	age=request.cookies.get('age')
	return render_template('DisplayCookie.html',myname=myname,age=age)
	

if __name__=="__main__":
	app.run(debug=True)


