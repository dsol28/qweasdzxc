from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def zxc():
    return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/image_mars')
def image_mars():
    return render_template("index.html")
@app.route('/promotion')
def promotion():
    return "Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!"
@app.route('/promotion_image')
def promotion_image():
    return render_template("index2.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)