from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

class InputForm(FlaskForm):
    submit = SubmitField('Go!')

def create_app(config=None):
    app = Flask(__name__)
    if config is None:
        app.config.from_mapping({
            'SECRET_KEY': 'barrel-spinster-barrel-smile',
        })
    else:
        app.config.from_mapping(config)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        form = InputForm()
        if form.validate_on_submit():
            return redirect(url_for('output'))
        return(render_template('input.html', form=form))

    @app.route('/output')
    def output():
        return(render_template('output.html'))

    return app
