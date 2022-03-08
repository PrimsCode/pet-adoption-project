from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DEFAULT_IMAGE_URL ="https://media.istockphoto.com/vectors/paw_print-vector-id931785704?k=20&m=931785704&s=612x612&w=0&h=wpnhxlh6HW0tRBxVIWynZMuJ-Lpp5rDRWjlVL2y_nt8="

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """pet database"""
    
    __tablename__ = "pet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    notes = db.Column(db.Text)
    avaliable = db.Column(db.Boolean, nullable = False)


    
 