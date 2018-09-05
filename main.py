from flask_wtf import FlaskForm
from flask import Flask, render_template, request, url_for, flash, redirect
#import json
from wtforms import Form,StringField, TextField, validators, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired, Length
from LOV_Check_input import LOV_input_form

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/')
def index():
   return render_template('abbvie_dashboard.html')

@app.route('/layout')
def layout():
   return render_template('Layout.html')

@app.route('/LOV', methods=['POST','GET'])
def LOV():
    #flash("flash test!")
    if request.method=='POST' :
        if request.form.get('submit'):
            val=request.form['txt_age']
            # return "Your age is " + val
            return render_template('lov.html', age=val, )
    return render_template('lov.html')

@app.route('/ControlTotal')
def ControlTotal():
    return render_template('Control_Total.html')

@app.route('/Reference')
def Reference():
    return render_template('Reference.html')

@app.route('/submit_LOV',methods=['POST','GET'])
def submit_LOV():
     dict_LOV_checks =[]
     if request.method=='POST' :
        source_table_name=request.form['source_table_name']
        source_table_ip_mode=request.form['source_table_ip_mode']
        source_table_Col_to_qc=request.form['source_table_Col_to_qc']
        ref_table_name=request.form['ref_table_name']
        ref_table_nref_table_ip_modeame=request.form['ref_table_ip_mode']
        ref_table_Col_to_qc=request.form['ref_table_Col_to_qc']
        case_sensitivity=request.form['case_sensitivity']


        write_to_csv('test.csv',[
            source_table_name,
            source_table_ip_mode,
            source_table_Col_to_qc,
            ref_table_name,
            ref_table_nref_table_ip_modeame,
            ref_table_Col_to_qc,
            case_sensitivity
        ],append= True)


        #  # fetch data from UI and store that in a dictionary
        # dict_LOV_checks ={ "LOV_checks" : [{
        #         "source_table_name" : source_table_name,
        #         "source_table_ip_mode" : source_table_ip_mode, 
        #         "source_table_Col_to_qc" : source_table_Col_to_qc,
        #         "ref_table_name" : ref_table_name,
        #         "ref_table_nref_table_ip_modeame" : ref_table_nref_table_ip_modeame,
        #         "ref_table_Col_to_qc" : ref_table_Col_to_qc,
        #         "case_sensitivity" : case_sensitivity}
        #         ]
        #     }

        # try:
        #     with open("C:\Python Project\Abbvie/Json/test.json","r") as f:
        #         data = json.load(f)
        #         f.close()
        #         newDictName = "LOV_checks_" + str(len(data))
        #         #updating the key name
        #         dict_LOV_checks[newDictName]=dict_LOV_checks.pop('LOV_checks')
        #         #concating old data with new dict
        #         data[newDictName]=dict_LOV_checks
        # except FileNotFoundError:
        #         newDictName = "LOV_checks_0"
        #         dict_LOV_checks[newDictName]=dict_LOV_checks.pop('LOV_checks')
        #         data=dict_LOV_checks

        # with open("C:\Python Project\Abbvie/Json/test.json","w") as f:
        #     # print(len(data))
        #     json_file= json.dumps(data)
        #     f.write(json_file)
        #     f.close()

        return render_template('Test.html',source_table_name=source_table_name, source_table_ip_mode=source_table_ip_mode,source_table_Col_to_qc=source_table_Col_to_qc, dict_LOV_checks = dict_LOV_checks)


#using model [souvik_s 9/4]
# @app.route('/LOV_model', methods=['POST','GET'])
# def LOV_model():
#     form= Create_LOV_Input_Form()
#     #if request.method=='GET' :
#     # if form.validate_on_submit():
#     #     return "Yes"
#     return render_template('lov_model.html', form=form)


# class Create_LOV_Input_Form(FlaskForm):
#     source_table_name = StringField('Source Table Name',validators=[DataRequired(), Length(min=2,max=5)])
#     source_table_ip_mode = StringField('Source Table Column Input mode',validators=[DataRequired(), Email()])
    
#     submit = SubmitField('Proceed')


@app.route('/LOV2',methods=['POST','GET'])
def lov2():
    form=LOV_input_form()
    if not form.validate_on_submit():
        return render_template('lov2.html',form=form)

@app.route('/LOV_Model',methods=['POST','GET'])
def LOV_Model():
    form=LOV_input_form(request.form)
    if request.method == "POST" and form.validate_on_submit():
        source_table_name=form.source_table_name.data
        case_sensitivity=form.case_sensitivity.data
        return render_template('Test.html',source_table_name=source_table_name,case_sensitivity=case_sensitivity)
    else:
        return render_template('lov_model.html',form=form, flag="no")


def write_to_csv(filePath,params,delimeter = ',',append = False):

    if append:
        file = open(filePath,'a')
    else:
        file = open(filePath,'w')

    string = delimeter.join(params)

    file.write(str(string) + "\n")
    file.close()



if __name__=="__main__" :
    app.run(debug=True)