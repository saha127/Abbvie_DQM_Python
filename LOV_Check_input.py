from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LOV_input_form(FlaskForm):
    source_table_name = StringField('Source Table Name',validators=[DataRequired(), Length(min=2, max=20)])
    source_table_ip_mode = StringField('source_table_ip_mode',validators=[DataRequired(), Length(min=2, max=20)])
    source_table_Col_to_qc = StringField('source_table_Col_to_qc',validators=[DataRequired(), Length(min=2, max=20)])
    ref_table_name = StringField('ref_table_name',validators=[DataRequired(), Length(min=2, max=20)])
    ref_table_ip_mode = StringField('ref_table_ip_mode',validators=[DataRequired(), Length(min=2, max=20)])
    ref_table_Col_to_qc = StringField('ref_table_Col_to_qc',validators=[DataRequired(), Length(min=2, max=20)])
    #case_sensitivity = StringField('case_sensitivity',validators=[DataRequired(), Length(min=2, max=20)])
    case_sensitivity = SelectField('Languages', choices = [('True', 'Yes'), 
      ('False', 'No')])
    submit = SubmitField('Proceed')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(LOV_input_form, self).__init__(*args, **kwargs)