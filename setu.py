x=15
if(x>10):
    print("x is greater")
else:
    print("x is lesser")   

x=5
if(x>10):
    print("x is greater")
else:
    print("x is lesser")   

p=90
if(p>10):
    print("p is greater")
else:
    print("p is lesser")


x=22
if(x%2==0):
    print("x is even number")  
else:
    print("x is odd number")

x=int(input("Enter any number"))

if(x%2==0):
    print("x is even number")
else:
    print("x is odd number")  

z=22
if(z%2!=0):
    print("z is even number")
else:
    print("z is odd number")    


marks=int(input("Enter any marks"))

if(marks>90):
    print("Excellent marks:A+")
elif(marks>80 and marks<=90):
    print("A grade")    
elif(marks>70 and marks<=80):
    print("B+  grade")   
elif(marks>60 and marks<=70):
    print("B grade")   
elif(marks>50 and marks<=60):
    print("C is grade")
else:
    print("D grade")   


for i in [100,200,300,400]:
    print(i)

for i in [100,200,300,400]:
    if(i==300):
        break
    print(i)

for i in [100,200,300,400]:
    if (i==300):
        continue 
    print(i)

for i in ['apple','mango','oranges','pipeline']:
    if(i=='oranges'):
        break
    print(i)

for i in ['apple','mango','oranges','pipeline']:
    if(i=='oranges'):
        continue
    print(i)

    