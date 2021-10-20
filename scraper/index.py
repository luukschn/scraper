from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from db import get_db

bp = Blueprint('main_page', __name__)

@bp.route('/')
def index():
    db = get_db()

    woningen = db.execute(
        'SELECT prijs, kamer, size, source, link, locatie, wijk' #need to add date added aswell
        ' FROM huurwoningen'
    ).fetchall()
    return render_template('main_page/index.html', woningen=woningen)