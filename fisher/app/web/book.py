# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:11
# @Author : CircleOne_

from flask import jsonify,request
from app.forms.book import SearchForm
from . import web

from helper import is_isbn_or_key
from yushu_book import YushuBook

# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search():
    # 9787507524044

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        # 正整数，最大值限制
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
        else:
            result = YushuBook.search_by_keyword(q)

        print(result)
        return jsonify(result)

    else:
        return jsonify(form.errors)
