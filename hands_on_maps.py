number1=[1,2,3]
number2=[4,5,6]
result=map(lambda x,y:x+y,number1,number2)  
print(list(result))
nums=[1,2,3,4,5,6]
def square(n):
    return n*n
squared=list(map(square,nums))
print("square of numbers:",squared)
print(square)