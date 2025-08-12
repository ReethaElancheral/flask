import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

# Dummy credentials for auth
DUMMY_EMAIL = "nisha.reetha30@gmail.com"
DUMMY_PASSWORD = "secret123"

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")

@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == DUMMY_EMAIL and password == DUMMY_PASSWORD:
            flash("Login successful", "success")
            return redirect(url_for("login"))
        else:
            flash("Invalid credentials", "error")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
