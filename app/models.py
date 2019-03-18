from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    upload = db.Column(db.String(150))
    profile_creation =db.Column(db.String(255))
    
    def __init__(self, first_name, last_name,gender,email,location,biography,upload):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email=email
        self.location=location
        self.biography=biography
        self.upload=upload
       
       

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
