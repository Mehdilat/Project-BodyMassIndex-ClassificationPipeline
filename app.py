from flask import Flask, render_template, redirect, url_for
from form import MetricForm
import joblib
import os

from data import status, description, advice

#implement validation for one or two decimal places
#add kaggle dataset and link
#add gender
#fix in version 2

models_dir = 'models'

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    metric_form = MetricForm()
    if metric_form.validate_on_submit():

        scaler_name = os.path.join(models_dir, "scaler.sav")
        scaler = joblib.load(scaler_name)
        model_name = os.path.join(models_dir, "svm_model.sav")
        model = joblib.load(model_name)
        
        formgender = metric_form.gender.data
        formheight = metric_form.height.data
        formweight = metric_form.weight.data

        scaled_form = scaler.transform([[formgender, formheight, formweight]])
        pred_bmi = model.predict(scaled_form).item()
        
        return redirect(url_for('result', bmi = pred_bmi, _external=True))
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