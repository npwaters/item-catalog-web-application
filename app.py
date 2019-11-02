import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    'postgresql://vagrant:{0}@{1}/catalog'.format(
        os.environ.get("VAGRANT_PASSWORD"),
        os.environ.get("DB_IP")
    ),
    echo=True
)
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


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

    # create tables
    Base.metadata.create_all(engine)

    return app
