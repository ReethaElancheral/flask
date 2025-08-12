import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class BugReportForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    description = TextAreaField("Bug Description", validators=[DataRequired()])
    severity = RadioField("Severity", choices=[
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High")
    ], validators=[DataRequired()])
    submit = SubmitField("Submit Report")

@app.route("/", methods=["GET", "POST"])
def report():
    form = BugReportForm()
    if form.validate_on_submit():
        severity = form.severity.data
        if severity == "high":
            flash("Critical bug reported! Our team will address it ASAP.", "error")
        elif severity == "medium":
            flash("Bug reported. We will look into it soon.", "warning")
        else:
            flash("Bug reported. Thank you for your feedback.", "success")
        return redirect(url_for("report"))
    return render_template("report.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
