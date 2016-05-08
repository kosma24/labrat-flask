from lab import db
from models import BlogPost

db.create_all() # creates the whole DB based on the schema in models

db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))

db.session.commit()
