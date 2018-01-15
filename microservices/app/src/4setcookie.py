
from flask import Flask, render_template
from flask import request
from flask import make_response

app=Flask(__name__)

@app.route('/setcookie')
def setcookie():
	resp=make_response('setting cookie')
	resp.set_cookie('myname','sharu')
	resp.set_cookie('age','32')
	return resp


if __name__=="__main__":
	app.run(debug=True)

