from . import db

class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender = db.Column(db.String(1))
    age = db.Column(db.Integer)
    biography = db.Column(db.Text)
    created_on = db.Column(db.String(80))
    image = db.Column(db.String(255))
    
    def __init__(self, userid, firstname, lastname, username, age, sex, bio, imageFile, createdOn):
        self.userid = userid
        self.username = username
        self.first_name = firstname
        self.last_name = lastname
        self.gender = sex
        self.age = age
        self.biography = bio
        self.created_on = createdOn
        self.image = imageFile
        
    
    def is_authenticated(self):
        return True
        
    def is_active(self): 
        return True
        
    def is_anonymous(self): 
        return False
        
    def get_id(self):
        try:
            return unicode(self.userid)  
        except NameError:
            return str(self.userid) 

    def __repr__(self):
        return '<User %r>' % (self.username)