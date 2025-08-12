import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class LeaveForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])
    reason = TextAreaField("Reason", validators=[DataRequired()])
    start_date = DateField("Start Date", format="%Y-%m-%d", validators=[DataRequired()])
    end_date = DateField("End Date", format="%Y-%m-%d", validators=[DataRequired()])
    submit = SubmitField("Apply Leave")

    def validate_end_date(form, field):
        if field.data < form.start_date.data:
            raise ValidationError("End Date cannot be before Start Date.")

@app.route("/", methods=["GET", "POST"])
def leave():
    form = LeaveForm()
    if form.validate_on_submit():
        duration = (form.end_date.data - form.start_date.data).days + 1
        flash(f"Leave applied successfully for {duration} day(s).", "success")
        return redirect(url_for("leave"))
    return render_template("leave.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
