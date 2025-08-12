import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired(), Length(min=20, message="Message must be at least 20 characters")])
    submit = SubmitField("Send Message")

@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Thank you for contacting us! We will get back to you soon.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
