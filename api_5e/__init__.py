from eve import Eve
from flask_bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve()
Bootstrap(app)


app.config["API_NAME"] = '5e-dnd-api'

app.register_blueprint(eve_docs, url_prefix='/docs')

if __name__ == "__main__" :
    app.run(debug=True)
