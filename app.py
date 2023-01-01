from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    # Process the message and store it in a database or file
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
