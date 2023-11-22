from http_layer.server import instantiate_app
from database.model import *

create_all_tables()

if __name__ == "__main__":
    app = instantiate_app()
    app.run(host="localhost", port=8080, debug=True)

app = instantiate_app()

