from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_ckeditor import CKEditorField


class SendForm(FlaskForm):
    name = StringField(label='Name',
                       validators=[DataRequired(),
                                   Length(min=5, max=64, message='Name length must be between %(min)d and %('
                                                                 'max)dcharacters')])
    email = StringField('Your email: ',
                        validators=[DataRequired(), Email(), Length(max=120)])
    subject = StringField(label='Subject')
    body = CKEditorField(label='Text', validators=[DataRequired()])
    submit = SubmitField('Send')
