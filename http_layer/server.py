from flask import Flask, jsonify, request, Response
from services.present_service import *

def instantiate_app():
    app = Flask(__name__)
    
    @app.route('/health', methods = ['GET'])
    def health_route() -> Response:
        #TODO actually check the database's health
        return "Ho ho ho", 200

    @app.route('/best-behaviour', methods = ['POST']) 
    def morality_check_route() -> Response:
        pass

    @app.route('/presents', methods = ['GET', 'POST']) 
    def presents_route() -> Response:
        presents = Presents(request.form("input"))
        if request.method == 'GET':
            try:
                result = presents.find_present()
                return result, 200
            except Exception as e:
                return "error", 400
        if request.method == 'POST':
            try:
                presents.ask_for_present()
                return result, 200
            except Exception as e:
                return "error", 400
    
    return app

