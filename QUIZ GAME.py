print('QUIZ GAME')
A=input("do y-ou want to play a quiz")
if A.lower()!='yes':
    quit()
score=0
answer=int(input("enter 1+1"))
if answer==2:
    print("correct answer")
    score+=1
else:
    print("wrong")
    score-=1
answer=input("wht is the brain of a computer")
if answer.lower()=="cpu":
    print("correct answer")
    score+=1
else:
    print('wrong')
    score-=1
print('score is',score)
