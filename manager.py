from flask import Flask

app = Flask(__name__)

@app.route('/')
def idnex():
	print('这是第一个提交文档')
	return 'hahaha'

if __name == '__main__':
	app.run()
