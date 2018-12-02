import click
from flask import Flask
from bluelog.blueprints.auth import auth_bp
from bluelog.blueprints.admin import admin_bp
from bluelog.blueprints.blog import blog_bp


app = Flask('bluelog')
app.config.from_pyfile('settings.py')

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
# app.register_blueprint(auth_bp, subdomain='auth')
app.register_blueprint(admin_bp)
app.register_blueprint(blog_bp)


if __name__ == '__main__':
    app.run()