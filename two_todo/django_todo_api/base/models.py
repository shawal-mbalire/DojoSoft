from django.db import models

# Create your models here.

class User(models.Model):
    # id = db.Column(db.Integer,primary_key=True)
    username = models.CharField(max_length=100,unique=True,blank=False)
    password_hash = models.TextField(blank=False)
    # todos = db.relationship('Todo')

    def __repr__(self) -> str:
        return super().__repr__()

class Todo(models.Model):
    # id = db.Column(db.Integer,primary_key=True)
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __repr__(self) -> str:
        return super().__repr__()
