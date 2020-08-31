import uuid
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

from lamejorwebapp.utils import _build_auth_url, _load_cache, _build_msal_app, _save_cache

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/login")
def login():
    session["state"] = str(uuid.uuid4())
    auth_url = _build_auth_url(scopes=current_app.config["SCOPE"], state=session["state"])
    return redirect(auth_url)

@bp.route("/logout")
def logout():
    session.clear()  # Wipe out user and its token cache from session
    return redirect(  # Also logout from your tenant's web session
        current_app.config["AUTHORITY"] + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))


@bp.route("/getAToken")  # Its absolute URL must match your app's redirect_uri set in AAD
def authorized():
    if request.args.get('state') != session.get("state"):
        return redirect(url_for("index"))  # No-OP. Goes back to Index page
    if "error" in request.args:  # Authentication/Authorization failure
        return render_template("auth_error.html", result=request.args)
    if request.args.get('code'):
        cache = _load_cache()
        result = _build_msal_app(cache=cache).acquire_token_by_authorization_code(
            request.args['code'],
            scopes=current_app.config["SCOPE"],  # Misspelled scope would cause an HTTP 400 error here
            redirect_uri=url_for("auth.authorized", _external=True))
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        _save_cache(cache)
    return redirect(url_for("index"))