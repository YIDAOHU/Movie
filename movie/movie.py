# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import config
from models import Film
from exts import db


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/detail/<film_id>/')
def detail(film_id):
    film = Film.query.filter(Film.id == film_id).first()
    return render_template('detail.html', film=film)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    kw = request.form.get('kw')
    films = Film.query.filter(Film.title.contains(kw))
    return render_template('list.html', films=films)


if __name__ == '__main__':
    app.run(debug=True)
