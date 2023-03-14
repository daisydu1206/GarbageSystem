from exts import db

class GarbageModel(db.Model):
    __tablename__ = "garbage"
    garbage_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    garbage_class = db.Column(db.String(50), nullable=False)
    garbage_name = db.Column(db.String(50), nullable=False)
    search_num = db.Column(db.Integer, default=0)



