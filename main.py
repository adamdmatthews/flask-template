import flask
app = flask.Flask(__name__)

@app.route("/_hello")
def hello():
        name = flask.request.args.get("name", '0')
        return flask.jsonify("hello " + name)

@app.route('/')
def main():
	return flask.render_template("index.html")

app.run()
