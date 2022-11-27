from flask import Blueprint, Markup
from flask import current_app as app

investment_accounts_bp = Blueprint(
    "investment_accounts_bp", __name__,
    template_folder="templates",
    static_folder="static"
)

@investment_accounts_bp.route("/", methods=["GET"])
def account_homepage():
    return Markup("<h1>Hello World!</h1>")