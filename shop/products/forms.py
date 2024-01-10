from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators
from wtforms.form import Form


class Addproducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stok = IntegerField('Stok', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    colors = TextAreaField('colors', [validators.DataRequired()])

    image_1 = FileField('Image 1')
    image_2 = FileField('Image 2')
    image_3 = FileField('Image 3')
    # image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg']),'image only please'])
    