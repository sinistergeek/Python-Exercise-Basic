from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def main():
    return '''
    <form action="/echo",methods="POST">
        <input name="text">
        <input type="submit" value="Echo">
    </form>
    '''

@app.route("/echo",methods=['POST'])
def echo():
    if 'text' om request.form:
        return "You said: " + request.form['text']
    else:
        return "Nothing to say?"
