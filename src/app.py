from flask import Flask

from .config import app_config

from .views.DefectView import defect_api as defect_blueprint


def create_app(env_name):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    app.register_blueprint(defect_blueprint, url_prefix='/api/v1/defects')

    @app.route('/', methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is working'

    return app
