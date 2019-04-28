from eve import Eve
from flask_bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve()
Bootstrap(app)

hostname = "localhost:5000"

app.config["API_NAME"] = '5e-dnd-api'
app.config["SERVER_NAME"] = hostname

app.register_blueprint(eve_docs, url_prefix='/docs')


if __name__ == '__main__':
    app.run(debug=True)
