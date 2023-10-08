from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email,ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your own secret key


# Create a simple WTForms form with email validation

def length(min=-1, max=-1):
    message = 'Must be between %d and %d characters long.' % (min, max)

    def _length(form, field):
        l = field.data and len(field.data) or 0
        if l < min or max != -1 and l > max:
            raise ValidationError(message)

    return _length

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired(),length(5,7)])
    email = StringField('Email', validators=[DataRequired(message="please enter email format"), Email()])
    submit = SubmitField('Submit')

@app.route("/")
def main_route():
    login_form = LoginForm()
    return render_template("login.html",form=login_form)

# Create a route to handle form submission and validation
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)