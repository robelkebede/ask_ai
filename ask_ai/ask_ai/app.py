from flask import Flask, request, render_template
from test import Ask_ai

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    try:
        ask = Ask_ai(text)
        que,ans = ask.run()

    except:
        text="faild to fetch data from wikipedia you are Offline or you are searching unknown wikipedia page"

    return str([que,ans])


if __name__ == '__main__':
    app.run(debug = True,port=5050,host="0.0.0.0")
