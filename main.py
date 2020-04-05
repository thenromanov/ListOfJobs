from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/list_prof/<list>')
def listProf(list):
    with open('data.json', 'rt', encoding='utf-8') as file:
        profsList = json.loads(file.read())
    return render_template('index.html', profs=profsList, list=list, title='Список')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
