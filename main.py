from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def zxc():
    return "Миссия Колонизация Марса"
@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"
@app.route('/username/<name>/<int:number>')
def username(name, number):
    return f'qweasd {name} ntt,t {number}'
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)