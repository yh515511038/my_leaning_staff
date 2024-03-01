import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    

    app.config.from_mapping(
        SECRET_KEY='0ba857871f387b5a5239b3b15b0f3f0365d0ef7fb1958cdd89431ce298e75d82',
        # SQLALCHEMY_DATABASE_URI='sqlite:///site.sqlite',
        DATABASE=os.path.join(app.instance_path, 'site.sqlite')
    )
    
    # if not test_config:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)
        
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except:
        pass
        
    from . import db
    db.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
    return app


app = create_app()
