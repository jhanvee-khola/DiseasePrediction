from users import db,login_manager
from users import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    password_hash=db.Column(db.String(60),nullable=False)
    
    @property 
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)