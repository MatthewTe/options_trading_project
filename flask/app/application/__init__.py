from flask import Flask

def init_app():
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('config.Config')

    with app.app_context():
        
        # Blueprint Imports:
        from .investment_accounts import routes as investment_accounts_blueprint

        # Blueprint registraction:

        app.register_blueprint(investment_accounts_blueprint.investment_accounts_bp)

        return app