import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

# Newsletter Form
class NewsletterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    frequency = SelectField("Frequency", choices=[
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly")
    ], validators=[DataRequired()])
    submit = SubmitField("Subscribe")

@app.route("/", methods=["GET", "POST"])
def subscribe():
    form = NewsletterForm()
    if form.validate_on_submit():
        flash("Subscribed successfully!", "success")
        return redirect(url_for("subscribe"))
    return render_template("subscribe.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
