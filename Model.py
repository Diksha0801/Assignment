from datetime import datetime
from config import db
from sqlalchemy.dialects.postgresql import UUID


class Student(db.Model):
    __tablename__ = "Student"
    student_id = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
    student_name = db.Column(db.String)
    class_id = db.Column(db.ForeignKey('Class.class_id'),nullable=False)
    created_on = db.Column(db.DateTime)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, student_name, class_id, created_on):
            self.student_name = student_name
            self.class_id = class_id
            self.created_on = created_on


class Class(db.Model):
    __tablename__ = 'Class'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String)
    class_leader = db.Column(db.Integer, db.ForeignKey('Student.student_id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, name, class_leader, created_on):
            self.class_name =  name
            self.class_leader = class_leader
            self.created_on = created_on
