import datetime
from datetime import date

from application.app import app , db
# FoodType	DataType
# id	int
# Type	string

class FoodType (db.Model) :
    id = db.Column ( db.Integer , primary_key=True )
    type = db.Column ( db.String ( 50 ), nullable=False )

# Food
#  id (data type Integer)
# foodType (FK)
# calories_intake (int)
# comments (data type String)
#  unit ( string )("calories")
# date (data type date)

class Food():
    id = db.Column ( db.Integer , primary_key=True )
    foodType = db.Column ( db.String ( 50 ) ,db.ForeignKey('FoodType.type'), nullable=False )
    calories_intake=db.Column(db.Integer)
    comments=db.Column ( db.String ( 50 ))
    unit=db.Column ( db.String ( 50 ))
    date=db.Column ( db.DateTime , default=datetime.datetime.utcnow , nullable=False )






# class FoodType (db.Model) :
#     id = db.Column ( db.Integer , primary_key=True )
#     food_list = db.Column ( db.String ( 50 ) )
#
#     created_by = db.Column ( db.Integer , db.ForeignKey ( 'FoodID.id' ) , nullable=False )
#     shared_with = db.relationship ( 'FoodID' ,secondary=shared_with , lazy='subquery',
#                                     backref=db.backref ( 'FoodID' , lazy=True ) )
# shared_with = db.Table ( 'shared_with' ,
#               db.Column ( 'id' , db.Integer , db.ForeignKey ( 'FoodType.id' ) , primary_key=True ) ,
#               db.Column ( 'id' , db.Integer , db.ForeignKey ( 'FoodID.id' ) , primary_key=True ) )
#
#
# class Food ( db.Model ) :
#     id = db.Column ( db.Integer , primary_key=True )
#     foodtype= db.Column ( db.String(40) )
#     date = db.Column ( db.DateTime , default=datetime.datetime.utcnow , nullable=False )
#     unit = db.Column ( db.String ( 80 ) )
#     comments = db.Column ( db.String ( 200 ) )
#     created_by = db.Column ( db.Integer , db.ForeignKey ( 'FoodType.food_list' ) , nullable=False )
#     shared_with = db.relationship ( 'FoodType' ,secondary=shared_with , lazy='subquery',
#                                     backref=db.backref ( 'FoodType' , lazy=True ) )
# shared_with = db.Table ( 'shared_with' ,
#               db.Column ( 'id' , db.Integer , db.ForeignKey ( 'Food.food_list' ) , primary_key=True ) ,
#               db.Column ( 'id' , db.Integer , db.ForeignKey ( 'Food.foodtype' ) , primary_key=True ) )

#
# class Work(db.Model) :
#     id= db.Column(db.Integer, primary_key=True)
#     technical= db.Column(db.String(80))
#     administrative = db.Column ( db.String ( 80 ) ,  )
#     work_description_1 = db.Column ( db.String (150))
#     work_description_2= db.Column(db.String(150))
#     date = db.Column (db.DateTime, default=datetime.datetime.utcnow, unique=True , nullable=False )
#     unit = db.Column( db.String ( 80 ))
#     comments = db.Column ( db.String ( 200 ) )
#
# class Goal(db.Model) :
#     id= db.Column(db.Integer, primary_key=True)
#     fitness_goal=db.Column ( db.String( 15 ) )
#     food_goal = db.Column ( db.String( 15 ) )
#     # date= db.Column(db.Column(datetime.date('today'), unique=True, nullable=False)
#     unit=db.Column(db.String(80))
#     comments=db.Column(db.String(200))
#
# class Fitness(db.Model) :
#     id= db.Column(db.Integer, primary_key=True)
#     activity_type_1= db.Column(db.String(80))
#     activity_type_2 = db.Column ( db.String ( 80 )  )
#     activity_type_3 = db.Column ( db.String ( 80 )  )
#     fitness_time= db.Column ( db.Integer )
#     date= db.Column(db.DateTime, default=datetime.datetime.utcnow, unique=True, nullable=False)
#     unit=db.Column(db.String(80))
#     comments=db.Column(db.String(200))
#

db.create_all()
db.init_app ( app )
# #     created_by = db.Column(db.Activity, db.ForeignKey('Activity.id'), nullable=False)
# #     shared_with = db.relationship('Activity', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))
#
# # shared_with = db.Table('shared_with',
# #     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
# #     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# # )

# Using the above sample write the DB models here


# create all tables and initialize app

# db.create_all()
print ( "hello" )
