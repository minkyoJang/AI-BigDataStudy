# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
#
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"  # 지가 알아서 엔진 만든다.
# db = SQLAlchemy(app)  # 확장할 때 항상 이 코드 쓴다.
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String, unique=True, nullable=False)
#
#
# @app.route('/')
# def index():
#     db.create_all()
#     return 'a'
#
#
# @app.route('/add/<name>/<email>')
# def add(name, email):
#     user = User(username=name, email=email)
#     db.session.add(user)
#     db.session.commit()
#     return 'OK'
#
#
# @app.route('/list')
# def list():
#     t = User.query.all()
#     return str(t)
#
#
# if __name__ == '__main__':
#     app.run()
