import random
requirements=['EnglishNine,HistNine,Bio,PE,MathNine','EnglishTen,HistTen,Chem,PE,MathTen','EnglishEleven,HistEleven,Phys,,MathEleven','EnglishTwelve,Econ,,,MathTwelve']
x=1
while x<5:
    f=open('students'+str(x)+'.txt','w+')
    newline='\n'
    x+=1
    for i in range(2000):
        grade = random.randint(1,4)
        f.write(str(i+1))
        f.write(',')
        f.write(str(grade))
        f.write(',')
        f.write(requirements[grade-1])
        f.write(newline)