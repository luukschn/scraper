import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    #g can store data during application context - aka during a request, command etc. rather than referring to the running app directly, a proxy is used
    if 'db' not in g:
        #db setup
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

#runs SQL commands to the db.py file
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized db')

def init_app(app):
    app.teardown_appcontext(close_db)       #cleanup after returning a response
    app.cli.add_command(init_db_command)    #adds a command which can be called with flask