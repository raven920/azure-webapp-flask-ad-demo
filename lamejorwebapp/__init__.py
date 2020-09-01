from flask import Flask, render_template, session
from flask_session import Session
from lamejorwebapp import app_config
from lamejorwebapp.blueprints.auth import refresh_session
from werkzeug.middleware.proxy_fix import ProxyFix



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(app_config)
    Session(app)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


    from lamejorwebapp.blueprints import auth, nav
    app.register_blueprint(auth.bp)
    app.register_blueprint(nav.bp)

    @app.route("/")
    @refresh_session
    def index():
        return render_template("index.html" )


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('403.html'), 403

    return app