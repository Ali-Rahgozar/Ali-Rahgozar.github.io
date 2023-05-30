import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'name' in request.args:
        name = str(request.args['name'])
        return f'''<h1>3 Pahlavan</h1>
<p>Hello to you Mr.{name} From MoTaRa</p>'''
    else:
        return "No name specified"



#app.run()