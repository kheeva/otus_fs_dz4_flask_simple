from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config.Development')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

Bootstrap(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    img_url = db.Column(db.String(100))

    specs = db.relationship('Spec', backref=db.backref('product', lazy=True))
    
    def __repr__(self):
        return '<Product %r>' % self.name


class ProductType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Spec(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('spec_type.id'))
    value = db.Column(db.String(50))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    spec_type = db.relationship('SpecType',
                                backref=db.backref('spec', lazy=True))

    def __repr__(self):
        return '<Spec %r %r>' % (self.type_id, self.value)


class SpecType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


if __name__ == "__main__":
    manager.run()
