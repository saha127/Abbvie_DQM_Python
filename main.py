from flask import Flask, render_template, request, url_for, flash, redirect
import json
app=Flask(__name__)

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


        

        # fetch data from UI and store that in a dictionary
        dict_LOV_checks ={ "LOV_checks" : [{
                "source_table_name" : source_table_name,
                "source_table_ip_mode" : source_table_ip_mode, 
                "source_table_Col_to_qc" : source_table_Col_to_qc,
                "ref_table_name" : ref_table_name,
                "ref_table_nref_table_ip_modeame" : ref_table_nref_table_ip_modeame,
                "ref_table_Col_to_qc" : ref_table_Col_to_qc,
                "case_sensitivity" : case_sensitivity}
                ]
            }

        try:
            with open("C:\Python Project\Abbvie/Json/test.json","r") as f:
                data = json.load(f)
                f.close()
                newDictName = "LOV_checks_" + str(len(data))
                #updating the key name
                dict_LOV_checks[newDictName]=dict_LOV_checks.pop('LOV_checks')
                #concating old data with new dict
                data[newDictName]=dict_LOV_checks
        except FileNotFoundError:
                newDictName = "LOV_checks_0"
                dict_LOV_checks[newDictName]=dict_LOV_checks.pop('LOV_checks')
                data=dict_LOV_checks

        with open("C:\Python Project\Abbvie/Json/test.json","w") as f:
            # print(len(data))
            json_file= json.dumps(data)
            f.write(json_file)
            f.close()

        return render_template('Test.html',source_table_name=source_table_name, source_table_ip_mode=source_table_ip_mode,source_table_Col_to_qc=source_table_Col_to_qc, dict_LOV_checks = dict_LOV_checks,json_file=json_file)

if __name__=="__main__" :
    app.run(debug=True)