from flask import Flask


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load the config
    app.config.from_pyfile('settings.py')

    # apply any config overrides e.g. for tests
    app.config.update(config_overrides)

    # import blueprints
    from home.views import home_app

    # register blueprints
    app.register_blueprint(home_app)

    return app
