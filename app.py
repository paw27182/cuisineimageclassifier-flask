from flask import Flask

# import Blueprint
from appmain.appmain_bp import appmain_bp
from topview.topview_bp import topview_bp


def create_app():
    app = Flask(__name__)
    # set context
    with app.app_context():
        app.config.from_object("settings")

    # register Blueprint
    app.register_blueprint(topview_bp)
    app.register_blueprint(appmain_bp)

    return app


app = create_app()  # factory


if __name__ == "__main__":
    host = app.config["HOST"]
    port = app.config["PORT"]
    app.run(host=host, port=port, threaded=False, debug=True)
