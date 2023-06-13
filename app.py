from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        try:
            mass = request.form('mass')
            mass = float(mass)
            height = request.form('height')
            height = float(height)
            imc = mass/(height*height)
            return render_template("form.html",imc=imc,mass=mass,height=height)
        except exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)
    if request.method == 'GET':
        return render_template("form.html")
    return "Hello"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
