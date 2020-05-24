from flask import Flask,request, render_template
from jinja2 import Template

f = open("good_prox.old",'r')
prox = f.read().split('\n')
f.close()

app = Flask(__name__,template_folder="jinja_templates")

@app.route('/')
def requestdata():
    return render_template('index.html', user_list=prox)

if __name__ == "__main__":
    app.run()