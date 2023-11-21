from server import *

def create_test_app():
    test_app = instantiate_app()
    test_app.config.update({"TESTING":True, "DEBUG":True})
    return test_app

flask_app = create_test_app()

class TestServer:
    def test_check_health(self):
        with flask_app.test_client() as test_client:
            res = test_client.post('/health')
            assert res.status_code == 200



