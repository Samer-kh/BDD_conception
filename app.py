from flask import Flask           # import flask
from controllers.publication_controlleur import app_publication
from controllers.author_controlleur import app_publication_author
from controllers.scientific_author_controlleur import app_publication_sci_auth
from controllers.book_author_controlleur import app_publication_book_auth
from controllers.book_category_controlleur import app_publication_book_cat
from controllers.category_controlleur import app_publication_cat
from controllers.cost_controlleurs import app_publication_cost
from controllers.user_controlleur import app_publication_user
app = Flask(__name__)             # create an app instance
app.register_blueprint(app_publication)
app.register_blueprint(app_publication_author)
app.register_blueprint(app_publication_sci_auth)
app.register_blueprint(app_publication_book_auth)
app.register_blueprint(app_publication_book_cat)
app.register_blueprint(app_publication_cat)
app.register_blueprint(app_publication_cost)
app.register_blueprint(app_publication_user)
if __name__ == "__main__":        # on running python app.py
    app.run() 