from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/africa"
app.config['SECRET_KEY'] = 'super-secret'

db = SQLAlchemy(app)

roles_users = db.Table('user',
                       db.Column('username', db.String()),
                       db.Column('email', db.String()))


class Role(db.Model, RoleMixin):
    name = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(80), unique=True)


class user2(db.Model, UserMixin):
    name = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String(80), unique=True)


user_datastore = SQLAlchemyUserDatastore(db, user2, Role)
security = Security(app, user_datastore)


@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='matt@bobien.net', name='matt')
    db.session.commit()


@app.route('/')
@login_required
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
