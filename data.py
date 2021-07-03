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
def getrandom():
   x=random.randint(1,len(ques))
   return ques[x]

#print(ques[1][ques[1]['correct']])

