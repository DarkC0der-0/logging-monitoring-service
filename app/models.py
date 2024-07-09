from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=db.func.current_timestamp())
