# a=20
# b=10

# # arithmatic 
# print(a+b);
# print(a-b);
# print(a*b);
# print(a/b);
# print(a//b);
# print(a%b);
# print(a**b);

# # relational

# print(a<b);
# print(a>b);
# # print(a>=b);
# print(a==b);
# print(a!=b);

# # Logical
# print(a and b)
# print(a or b)
# print(not a)


# # Assignment
# a+=1;
# print(a)
# a-=1;
# print(a)
# a*=1;
# print(a)
# a/=1;
# print(a)

# str= "Hello Buddy!"
# print(str)

# print(str[0:6])
# print(str[6:])
# print(str.endswith('x')) # false
# print(str.endswith('!')) # true
# print("manas sir".capitalize())
# print("manas sir".lower())
# print("manas sir".upper())

# print("manas sir".replace("s","v"))
# print("manas sir".find("s"))
# print("manass sir".count("s"))


# age = 20;

# if age>18:
#     print("adult")
# elif age <18:
#     print("minor")
# else:    
#     print("age is equal to 18")


# def check_status(code):
#     match code:
#         case 200:
#             return "success"
#         case 400:
#             return "Bad Request"
#         case 404:
#             return "Not Found"
#         case _:
#             return "Unknown Status"

# print(check_status(405))        



# list=[1,2,3,4,"Ram",True,2.0]
# list=[1,2,3,4,0,77,43]

# # help(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# list.append(10);
# print(list)
# # print(list[0:5])

# list.reverse()
# print(list)

# list.insert(0,12)
# print(list)
# list.remove(2)
# print(list)
# list.pop()
# print(list)


# t=(1,3,4,5,10,12)

# t.index(4)

# print(t.index(4))
# print(t.count(4))



# set1={1,2,3,4,5,6,6}
# set2={6,6,7,8,9,10}

# print(set1)
# print(set2)

# set1.add(7)
# print(set1)
# set2.remove(6)
# print(set2)


# set1.pop()
# print(set1)
# set1.union(set2)
# print(set1)
# set1.intersection(set2)

# print(set1)

# set2.clear()
# print(set2)

# seq=range(5)

# for val in seq:
#     print(val)

# for i in range(0,10):
#     if i==3:
#        continue
#     if i==5:
#         break
#     print(i) 


# i=1

# while i<100:
#     print(i)
#     if i==34:
#         break
#     i+=1

# fs=open("manas.txt",'x')
# # file= open("manas.txt",'w')

# file= open("titu.txt",'w')
# file.write("Hi I am manas")

# # a=file.read()
# print(file)


# file= open("titu.txt",'a')
# file.write("Hi I am titu")
# print(file)

# file= open("note.txt",'a')
# file.write("Hi I am titu")



# list=[12,34,67,99,105,11,5,5,34]

# seen={}
# res=[]

# for num in list:
#     if num not in seen:
#         seen[num]=True
#         res.append(num)


# print(res)


# max_num=0;

for i in range(len(list)):
    if list[i]>max_num:
        max_num=list[i]

print(max_num)  



s=set()
for i in range(len(list)):
     if list[i] not  in s:
         s.add(list[i])


# print(s)


















  
















