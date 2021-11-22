# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:12
# @Author : CircleOne_

from httper import HTTP

class YushuBook:
    # 9787802257863
    isbn_url = 'http://t.talelin.com//v2/book/isbn/{}'
    keyword_url = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # 返回结果为json格式
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, satrt=0):
        url = cls.keyword_url.format(keyword, count, satrt)
        result = HTTP.get(url)
        return result


if __name__ == '__main__':
    # yushu_result = YushuBook.search_by_isbn(9787802257863)
    yushu_result = YushuBook.search_by_keyword('好人难寻')
    print(yushu_result)