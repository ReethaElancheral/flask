import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange, Length

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "mysecret")

class ReviewForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    rating = IntegerField("Rating (1-5)", validators=[DataRequired(), NumberRange(min=1, max=5, message="Rating must be between 1 and 5")])
    review = TextAreaField("Review Message", validators=[DataRequired(), Length(min=10, message="Review must be at least 10 characters")])
    submit = SubmitField("Submit Review")

@app.route("/", methods=["GET", "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash("Thank you for your review!", "success")
        return redirect(url_for("review"))
    return render_template("review.html", form=form)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
