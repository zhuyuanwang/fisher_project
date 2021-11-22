# -*- coding: utf-8 -*-
# @Time : 2021/11/20 15:12
# @Author : CircleOne_

def is_isbn_or_key(word):
    """
    isbn isbn13 13个0到9的数字组成
    isbn10 10个0到9数字组成，含有一些'-'
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shor_word = word.replace('-', '')
    if '-' in word and len(shor_word) == 10 and shor_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key