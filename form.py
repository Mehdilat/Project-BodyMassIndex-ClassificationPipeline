from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, DecimalField, RadioField
from wtforms.validators import InputRequired, NumberRange

min_height = 120
max_height = 220
min_weight = 40
max_weight = 200

class MetricForm(FlaskForm):
    gender = RadioField("Gender", choices = [(0, 'Male'), (1, 'Female')], validators=[InputRequired("Please choose an option")])
    height =  DecimalField("Height", places = 2, validators=[InputRequired("This field is required"), NumberRange(min = min_height, max = max_height, message="Value must be between 100 and 200")])
    weight =  DecimalField("Weight", places = 1, validators=[InputRequired("This field is required"), NumberRange(min = min_weight, max = max_weight, message="Value must be between 100 and 200")])
    submit = SubmitField("Compute BMI")