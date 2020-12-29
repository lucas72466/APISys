# encoding: utf-8

"""
@author : lucas
@contact : lucas72466@gmail.com
"""
from flask import request, jsonify
from sqlalchemy import or_

from app.libs.redprint import RedPrint
from app.models.book import Book
from app.validatos.forms import BookSearchForm

api = RedPrint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = ''.join(['%', form.q.data, '%'])
    books = Book.query.filter(or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)

