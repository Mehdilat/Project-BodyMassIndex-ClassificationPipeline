from flask import Flask, render_template, redirect, url_for
from form import MetricForm
import joblib

from data import status, description, advice

#implement validation for one or two decimal places
#add kaggle dataset and link
#add gender
#fix in version 2

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    metric_form = MetricForm()
    if metric_form.validate_on_submit():
        filename = "svm_model.sav"
        model = joblib.load(filename)
        
        formgender = metric_form.gender.data
        formheight = metric_form.height.data
        formweight = metric_form.weight.data
        
        std_formheight = (formheight - 140)/(199 - 140)
        std_formweight = (formweight - 50)/(160 - 50)
        pred_bmi = model.predict([[formgender, std_formheight, std_formweight]]).item()
        
        return redirect(url_for('result', bmi = min(max(int(pred_bmi), 1), 5), _external=True))
    return render_template("home.html", form = metric_form)

@app.route("/result/<bmi>", methods=["GET", "POST"])
def result(bmi):
    bmi_status = status[int(bmi)]
    bmi_description = description[int(bmi)]
    bmi_advice = advice[int(bmi)]
    return render_template("result.html", bmi = bmi, status = bmi_status, description = bmi_description, advice = bmi_advice)

@app.route("/project") 
def project():
    return render_template("project.html")

@app.route("/about") 
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)