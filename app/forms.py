from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Email


# ToDo: Добавить нужные формы для сайта, пример с ВБ

# class NewQuery(FlaskForm):
#     user = StringField(
#         'Название',
#         validators=[DataRequired(message="Поле не должно быть пустым")]
#     )
#     email = EmailField(
#         'Введите email',
#         validators=[DataRequired(message="Поле не должно быть пустым"),
#                     Email(message='Введите email')]
#     )
#     query = StringField(
#         'Запрос поиска',
#         validators=[DataRequired(message="Поле не должно быть пустым")]
#     )
#     percent = IntegerField(
#         'Процент скидки',
#         validators=[DataRequired(message="Поле не должно быть пустым")]
#     )


# class EmailSearch(FlaskForm):
#     email = EmailField(
#         'Введите email',
#         validators=[DataRequired(message="Поле не должно быть пустым"),
#                     Email(message='Введите email')]
#     )
