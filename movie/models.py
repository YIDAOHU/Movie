# -*- coding: utf-8 -*-

from exts import db


class Film(db.Model):
    __tablename__ = 'dytt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    translate_name = db.Column(db.String(300), nullable=False)
    year = db.Column(db.String(100), nullable=False)
    product_site = db.Column(db.String(100), nullable=False)
    classify = db.Column(db.String(100), nullable=False)
    actors = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(500), nullable=False)
    cover_url = db.Column(db.String(500), nullable=False)
    screenshot_url = db.Column(db.String(500), nullable=False)
    thunder_url = db.Column(db.String(500), nullable=False)
    magnet_url = db.Column(db.String(500), nullable=False)

