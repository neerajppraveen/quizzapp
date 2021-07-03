from werkzeug.datastructures import CharsetAccept
import data
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def appstart():
   return render_template("app.html")

@app.route('/begin')
def begin():

    name=request.args.get('name')

    if name==None:
        return "<h2>Invalid name</h2>"
    ques=data.ques
    return render_template("quizz.html",name=name,ques=ques)



@app.route('/submit')
def submit():

   score=0
   q1=list(request.args.get( '1'))
   q1.remove(q1[-1])
   b=list(data.ques[1][data.ques[1]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '2'))
   q1.remove(q1[-1])
   b=list(data.ques[2][data.ques[2]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '3'))
   q1.remove(q1[-1])
   b=list(data.ques[3][data.ques[3]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '4'))
   q1.remove(q1[-1])
   b=list(data.ques[4][data.ques[4]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1
   q1=list(request.args.get( '5'))
   q1.remove(q1[-1])
   b=list(data.ques[5][data.ques[5]['correct']])
   if q1==b :
      score=score+1
   print(q1)
   del q1   
   #print(q1 +"=="+str(data.ques[1][data.ques[1]['correct']]))


   return render_template("result.html",score=score)



if __name__ == '__main__':
   app.run(debug=True)