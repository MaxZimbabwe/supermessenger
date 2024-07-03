import pytest
from app import create_app
from app.services.microservices.comum_api_service import ComumApiServices

@pytest.fixture(scope='module')
def api_comum():
    app = create_app()
    with app.app_context():
        api = ComumApiServices()
        yield api

# other fixtures as needed...
