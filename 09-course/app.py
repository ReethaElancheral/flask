import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class EnrollmentForm(FlaskForm):
    student_name = StringField("Student Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    course = SelectField("Course", choices=[
        ("python", "Python"),
        ("javascript", "JavaScript"),
        ("data_science", "Data Science"),
        ("web_dev", "Web Development"),
    ], validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=18, max=60, message="Age must be between 18 and 60")])
    submit = SubmitField("Enroll")

@app.route("/", methods=["GET", "POST"])
def enroll():
    form = EnrollmentForm()
    if form.validate_on_submit():
        name = form.student_name.data
        course = dict(form.course.choices).get(form.course.data)
        flash(f"Hi {name}, you enrolled in {course}.", "success")
        return redirect(url_for("enroll"))
    return render_template("enroll.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
