# Testing Flask Applications that use Flask-WTForms
2024-05-03

Flask WTForms have a `validate_on_submit` method that checks whether a
form has been submitted and whether is passes validation. It also
implements CSRF protection. This means that when testing a POST request,
`validate_on_submit` returns False. To avoid this, WTF_CSRF_ENABLED
needs to be set to False in the test config.

For example, if we have an app like this:

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

which has 2 templates (see below), one with a simple form with just a
submit button and one which is redirected to when the form is submitted.
This uses `validate_on_submit` to test if the request is a POST one and
if the form validates.

The two templates look like this

`input.html`

    <!doctype html>
    <html class="no-js" lang="en-gb">
    <head>
      <meta charset="utf-8">
      <title>Testing Flask WTForms</title>
    </head>
    <body>
    <h1>Test Page with form</h1>
    <form action="{{ url_for('index') }}" method="post" novalidate>
        {{ form.hidden_tag() }}
    <p>{{ form.submit() }}</p>
    </form>
    </body>
    </html>

`output.html`

    <!doctype html>
    <html class="no-js" lang="en-gb">
    <head>
      <meta charset="utf-8">
      <title>Testing Flask WTForms</title>
    </head>
    <body>
    <h1>Test Output Page</h1>
    </body>
    </html>

If we try and test this as below, we get the `input.html` template in
the response to both GET and POST requests. This is because CRSF
protection is enabled by default and that stops the test POST request
from validating.

    import pytest

    from app import create_app

    @pytest.fixture
    def test_app_csrf():
        app = create_app({
            'SECRET_KEY': 'barrel-spinster-barrel-smile',
            'TESTING': True
        })
        return app

    @pytest.fixture
    def client_csrf(test_app_csrf):
        return test_app_csrf.test_client()

    # create a client with CSRF protection enabled
    def test_with_csrf(client_csrf):
        # get returns input template
        response = client_csrf.get('/')
        assert b'<h1>Test Page with form</h1>' in response.data
        # but so does post
        response = client_csrf.post('/', data = {}, follow_redirects=True)
        assert b'<h1>Test Page with form</h1>' in response.data

In order to test this properly, we need to set `WTF_CSRF_ENABLED` to
False in the app config.

    import pytest

    from app import create_app

    # create a client with CSRF protection disabled
    @pytest.fixture
    def test_app():
        app = create_app({
            'TESTING': True,
            'WTF_CSRF_ENABLED': False
        })
        return app

    @pytest.fixture
    def client(test_app):
        return test_app.test_client()

    # now when can test the form submission
    def test_without_csrf(client):
        # get returns input template
        response = client.get('/')
        assert b'<h1>Test Page with form</h1>' in response.data
        # but now post follows the redirect and returns the output template
        response = client.post('/', data = {}, follow_redirects=True)
        assert b'<h1>Test Output Page</h1>' in response.data
