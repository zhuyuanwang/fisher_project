# -*- coding: utf-8 -*-
# @Time : 2021/11/22 19:32
# @Author : CircleOne_

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)