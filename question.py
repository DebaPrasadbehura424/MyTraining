
def printLoop():
 for i in range(1,11):
    print(i)

def sum():
    a= int(input("Enter the Value:- "))
    b= int(input("Enter the Value:- "))
    print(a+b)

def evenOdd(val):
    if val%2==0:
        print("EVEN")
    else:
        print("ODD") 

def multiTable():
   val= int(input("Enter the Value:- "))
   for i in range(1,11):
    print(val*i)

def largestNumber():
   val1= int(input("Enter the Value:- "))
   val2= int(input("Enter the Value:- "))
   print(val1 if val1>val2 else val2)

def countVowels():
   count=0;
   s=input("Enter the String: - ")
   vowels={'a','i','o','u','e'}
   for i in len(s):
      if s[i].lower() in vowels:
         count=count+1
   print(count) 


def sumOfList():
    list=[1,2,4,10,16];
    sum =0
    for val in list:
     sum+=val;
    print(sum)

def dictPrint():   
   d={1:"A",2:"B",3:"C"}
   for i in d.keys():
    print(f"{d[i]} : {i}") 


def sqaure():
   val= int(input("Enter the Value:- "))
   print(f"Sqaure of {val} is : {val**2}")


while True:
   num=int(input("Choose the option:- "))

   match num:
      case 1:printLoop()
      case 2:sum()
      case 3:evenOdd()
      case 4:multiTable()
      case 5:largestNumber()
      case 6:countVowels()
      case 7:sumOfList()
      case 8:dictPrint()
      case 9:sqaure()
      case 10:break
         
         
   







  





