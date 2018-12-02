from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif
                border-radius: 10px;
            }}
            textarea {{
                margin 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/rotate" method="post">
            <label for="rot">Rotate by:
                <input type="text" id="rot" name="rot" value="0" />
            </label>
            <textarea name="text"> {0} </textarea>
            <input type="submit" name="submit" value="Submit Query"/> 
        </form>
    </body>
</html>
"""

### Does it matter how I use <label>?
### ex) <label>Rotate by:</label>
### Do i need rest of stuff after type="submit"??

@app.route("/rotate", methods=['POST'])
def encrypt():
    rotate = int(request.form['rot'])
    text = request.form['text']
    encrypted = rotate_string(text, rotate)     #Is it correct format to use rotate_string function?
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()