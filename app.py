#Created by Neeraj P Praveen
from flask import Flask,render_template,request
import random
ques={
  1:{
     "no":1,
"question":"Capital of india",
"a":"Delhi",
"b":"Mumbai",
"c":"Chennai",
"correct":"a"
},
  2:{
        "no":2,
"question":"Capital of russia",
"a":"Delhi",
"b":"Moscow",
"c":"Washington",
"correct":"b"
}
  ,  
  3:{
        "no":3,
"question":"Capital of kerala",
"a":"Delhi",
"b":"Thirvandram",
"c":"Chennai",
"correct":"b"
},
    4:{
        "no":4,
"question":"Hary potter writtern by",
"a":"Rowling",
"b":"RDJ",
"c":"SRK",
"correct":"a"
}
,
    5:{
        "no":5,
"question":"Latest version of windows",
"a":"11",
"b":"10",
"c":"7",
"correct":"a"
}
}
ques2={}
List = [1, 2, 3, 4, 5]
def getrandom():
   x=random.sample(List, 5)
   for i in x:
     ques2[i]=ques[i]
   return  ques2
app = Flask(__name__)
@app.route('/')
def appstart():
   return render_template("app.html")
@app.route('/begin')
def begin():

    name=request.args.get('name')

    if name==None:
        return "<h2>Invalid name</h2>"
    quest=getrandom()
    return render_template("quizz.html",name=name,ques=quest)



@app.route('/submit')
def submit():

   score=0
   q1=list(request.args.get( '1'))
   q1.remove(q1[-1])
   b=list(ques[1][ques[1]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '2'))
   q1.remove(q1[-1])
   b=list(ques[2][ques[2]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '3'))
   q1.remove(q1[-1])
   b=list(ques[3][ques[3]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '4'))
   q1.remove(q1[-1])
   b=list(ques[4][ques[4]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '5'))
   q1.remove(q1[-1])
   b=list(ques[5][ques[5]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1   



   return render_template("result.html",score=score)



if __name__ == '__main__':
   app.run(debug=True)