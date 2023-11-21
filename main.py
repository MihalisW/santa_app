from http_layer.server import instantiate_app

# set up for local running
if __name__ == "__main__":
    app = instantiate_app()
    app.run(host="localhost", port=8080, debug=True)

# for running the actual gunicorn application need to create the app
app = instantiate_app()
