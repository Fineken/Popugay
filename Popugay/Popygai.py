from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>ПО-ПУ-ГАЙ</title>
    <style>
        body {
            background-color: orange;
            text-align: center;
            font-family: Arial, sans-serif;
            color: black;
        }
        h1 {
            color: black;
        }
        form {
            margin-top: 20px;
        }
        input[type="text"] {
            margin-top: 10px;
        }
        input[type="submit"] {
            margin-top: 10px;
        }
        .parrot {
            font-family: "Courier New", Courier, monospace;
            text-align: left;
        }
        ul {
            text-align: left;
            display: inline-block;
            margin: 0;
            padding: 0;
        }
        li {
            list-style: none;
        }
    </style>
</head>
<body>
    <div class="parrot">
        <pre>
________________________________________$$$$$$$$$___$$$
____________________________________$$$$$$$$_____(&)_$$$$
________________________________$$$$$$$$$$____________$$$$
_____________________________$$$$$$$$$$$$$$$____§§§§_____$
___________________________$$$$$$$$$$$$$$$$$$§§§§_§§§_____$
_________________________$$$$$$$$$$$$$$$$$$$$$§§§§§_§____$
______________________$$$$$$$$$$$$$$$$$$_$$$$___§§§__§_$
____________________$$$$$$$$$$$$$_$$$$$$$$_$________§
___________________$$$$$$$$$$$$$$$$$$$$$$$$_$
_________________$$$$$$$$$_$$$$$$$$$$$$$$$$_$
_______________$$$$$$$$_§http://risuns.ru$$$$$_$
_____________$$$$$$$_$$§§§$$$§$$§§$$$$§§$_$$$
____________$$$$$$_§§§$$§§$$§§§$$§§$$§§$_$$$
___________$$$$$_$§§§$$$$§§§$$$§§§§§$$_$$$$$
__________$$$$$_§§§§§§$$§§§$$§§§§§§§_$$$$$$
_________$$$$_§§0§§§§§§§§§§§§§§§§_$$$$$$$
________$$$_000§§§00§§§§§000§00§_$$$$$$
________$$_0000§§0000§§§00§0§_$$$$$$
_______$_0000§§00000§0000_$$$$$$$
_____§§00000§000§0000_$$$$$$$$
___§00000§0000000_$$$$$$$$$$
___000§00000§_§§§§$$$$$$$$$$$$$___......
__0000§00§§§§§§$$$$$$$$__$$$$$$$$§§§§§
_000§0_§§§§§§$$$$$$$_§000_$$$§§§_0000000000000000000
00____§§§§§$$$$$$$_§§00000_$§§§_00000000000000000000
______§§§§$$$$$$$_§§§_’’______§§§__’’
_____§§§$$$$$$
____§§$$$$$$$
___$$$$$$$$
__$$$$$$$$
_$$$$$$$$
$$$$$$$$
$$$$$$$
$$$$$$
$$$$
$$$
        </pre>
    </div>
    <h1>5 КУРС, ПОПУГАЙ--ПРОЕКТ </h1>
    <form method="POST">
        <input type="text" name="text_input" placeholder="Введите текст"/>
        <input type="submit" value="Отправить"/>
        <h1></h1>
        <h1></h1>
        <h1></h1>
        <h1></h1>
    </form>
    {% if text_output %}
        <ul>
        {% for word in text_output %}
            <li>{{ word }}</li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    text_output = []
    if 'text_output' in request.form:
        text_output = request.form['text_output'].split(',')
    if request.method == 'POST':
        text_input = request.form['text_input']
        if text_input:
            text_output.append(text_input + ' ' + text_input)
    return render_template_string(HTML_TEMPLATE, text_output=text_output)

if __name__ == '__main__':
    app.run(debug=True)
