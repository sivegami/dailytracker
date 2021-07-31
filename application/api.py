from typing import Dict , List , Any

from flask import request

from application.app import app,db

import datetime
from application.models import Food,FoodType
    # Work , Fitness , Goal
#
@app.route("/")
def home():
    return {"Status": "Success"}, 200
#



@app.route("/Food", methods=["POST"])
#sent data in dictionary format
#{data:[{"type":"breakfast"},{"type":"lunch"},{"type":"dinner"},{"type":"snack"}]}
#get the value of dictionary data --- assign it to a variable
#loop through the list of dictionary and assign each dictionary to a variable

def type_Food():
    params = request.params
    print (request.params)
    list_1=params["data"]
    # Let's loop
    for item in list_1:
        # create FoodType.
        # How did you create Food object before? Same way
        food_type = FoodType(type=item["type"])
        db.session.add(food_type)
    db.session.commit()

# Food
#  id (data type Integer)
# foodType (FK)
# calories_intake (int)
# comments (data type String)
#  unit ( string )("calories")
# date (data type date)

@app.route ( "/DailyTracker" , methods=(["POST"]))
def add_food():
  params=request.json

  foodType=params["foodType"]
  unit=params["unit"]
  date=params["date"]
  comments=params["comments"]
  calories=params["calories_intake"]
  result =Food( foodtype=foodType, unit=unit,calories_intake=calories, comments=comments )
  db.session.add(result)
  db.session.commit ()
  print(result)
  return {"breakfast":result.breakfast,"unit":result.unit,"comments":result.comments,"calories":result.calories_intake}


@app.route ( "/DailyTracker" , methods=(["GET"]) )
def daily_Food() :
  res = Food.query.filter(db.cast(Food.date, db.DATE) ==datetime.date.today() ).all()

  return [{"foodType" : row.foodType, "unit" : row.unit , "calories" : row.calories_intake , "comments" :row.comments} for row in res]



# @app.route ( "/DailyTracker" , methods=(["GET"]) )
# def daily_Work() :
#     result = Work.query.filter_by ( date.today () )
#
#     for result in result :
#         result.append ( {"technical" : Work.technical , "work description" : Work.work_description_1 ,
#                          "administrative" : Work.administrative , "work description" : Work.work_description_2 ,
#                          "comments" : Work.comments
#
#                          } )
#     return result
#
#
# @app.route ( "/DailyTracker" , methods=(["GET"]) )
# def daily_Fitness() :
#     result = Fitness.query.filter_by ( date.today () )
#
#     for result in result :
#         result.append ( {"Yoga" : Fitness.activity_type_1 , "Jogging" : Fitness.activity_type_2 ,
#                          "Walking" : Fitness.activity_type_2 ,
#                          "time" : Fitness.fitness_time ,
#                          "comments" : Fitness.comments
#
#                          } )
#     return result
#
#
# @app.route ( "/DailyTracker" , methods=(["GET"]) )
# def daily_Goal() :
#     goal = Goal.query.filter_by( Goal.food_goal )
#     if Food.calories_consumed.filter_by( date.today () )<= goal :
#         return "Welldone, ideal meal intake"
#     elif Food.calories_consumed is None :
#         return "Keep tracking your calories"
#     else :
#         return "Watchout your meal intake"
#
#
