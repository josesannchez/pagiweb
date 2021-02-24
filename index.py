from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def principal():
	return  render_template('index.html')
 
@app.route('/congruncial')
def Congruncial():
	return  render_template('congruncial.html')


if __name__== '__main__':
        app.run(debug=True, port=5017)

