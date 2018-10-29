from flask import Flask

app = Flask(__name__)

@app.route('/')
def idnex():
	return 'hahaha'

if __name == '__main__':
	app.run()
