import os 

from flask import (Flask, 
                   render_template, 
                   request, 
                   make_response, 
                   Response)
import json
from services.present_service import *
from database.queries import *

template_dir = os.path.abspath('../santa_app/templates')

def instantiate_app():
    app = Flask(__name__, template_folder=template_dir)
    queries = Queries()

    def create_response(data, code) -> Response:
        response = make_response('Response')
        response.data = data 
        response.status_code = code    
        return response

    @app.route('/')
    def home_page_route():
        return render_template('index.html')
    
    @app.route('/health', methods = ['GET'])
    def health_route() -> Response:
        response_data = {"app_working": False}
        try:
            result = queries.check_health()
            print(result)
            response_data["app_working"] = result
            data = json.dumps(response_data)
            if result:
                return create_response(data, 200)
            return create_response(data, 500)            
        except Exception as e:
            return create_response("{\"app_working\":, false}", 200)


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

