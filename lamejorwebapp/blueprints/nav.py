from flask import (
    Blueprint, abort, session, render_template, url_for, current_app
)
import requests
from lamejorwebapp.utils import _get_token_from_cache


bp = Blueprint('nav', __name__, url_prefix='/nav')

@bp.route("/admin")
def admin():
    if session['user'] and 'Superduperadministrador' in session['user']['roles']:
        token = _get_token_from_cache(current_app.config["SCOPE"])
        graph_data = requests.get(  # Use token to call downstream service
            current_app.config["ENDPOINT"],
            headers={'Authorization': 'Bearer ' + token['access_token']},
            ).json()
        return render_template('admin.html', result=graph_data.get("value"))

    else:
        abort(403)

@bp.route("/shop")
def shop():
    if session['user'] and 'ElMejorCliente' in session['user']['roles']:
        return render_template('shop.html')
    else:
        abort(403)

@bp.route("/recycle")
def recycle():
    if session['user'] and 'Reciclador' in session['user']['roles']:
        return render_template('recycle.html')
    else:
        abort(403)