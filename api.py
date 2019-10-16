from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Flighty(Resource):
	def get(self):
		return {'yo': 'flighty!'}
api.add_resource(Flighty, '/')

if __name__ == '__main':
	app.run(debug=True)
