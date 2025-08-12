import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class RSVPForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    will_attend = BooleanField("Will Attend?")
    submit = SubmitField("Submit RSVP")

@app.route("/", methods=["GET", "POST"])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if form.will_attend.data:
            flash(f"Thank you, {form.name.data}! Looking forward to seeing you.", "success")
        else:
            flash("Sorry to miss you.", "info")
        return redirect(url_for("rsvp"))
    return render_template("rsvp.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
