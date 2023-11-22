# Santa App

A RESTful API for folk to: 

* Check the status of their behaviour
* Search for presents
* Ask for presents 



# Refactoring http_layer

### setup
* `$ pip install -r requirements.txt`
* `$ flask run`

### Notes
- Initial commit was a bit brutal! Reworked things to keep exisitng files
- Adding flask-y extras like `.flaskenv` and using `python-dotenv` for managing environment variables via `config.py`

- http_layer now treated as a package and can be run with `flask run`
- `flask run`

- moved static assets to static folder
- moved template folder to the http_layer package as Flask will find this auto-magically, along with the static folder
- moved routes defined in `server.py` to `routes.py`
- added `santa.py` as the entrypoint to the application, bearing in mind we can use `.flaskenv` to build various flavours 🍦

- haven't integrated the latest changes to `server.py`
