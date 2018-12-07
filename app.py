import os
from flask import Flask, render_template, url_for
# import dash
# import flask
# import dash_core_components as dcc
# import dash_html_components as html
# from werkzeug.serving import run_simple
# from werkzeug.wsgi import DispatcherMiddleware

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
flask_app = Flask(__name__)

posts_data = [
    {
        'bug': 'Red Mite',
        'predator': 'Birdy Bird',
        'crops_affected': "really can't say",
        'ei_val': '-999999'
    }#,
    # {
    #     'author': 'Jane Doe',
    #     'title': 'Blog Post 2',
    #     'content': 'Second post content',
    #     'date_posted': 'April 21, 2018'
    # }
]
app_title="AGTHON 2018"
## Home page Route
@flask_app.route('/')
@flask_app.route('/home')
def home():
    return render_template('home.html',posts=posts_data, app_title=app_title)

## About Page Route
@flask_app.route('/about')
def about():
    return render_template('about.html',title="About", app_title=app_title)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))



if __name__=="__main__":
    # run_simple('localhost', 5000, application,
    #            use_reloader=True, use_debugger=True, use_evalex=True)
    flask_app.run(host='0.0.0.0', port=port, debug=True)