
# print("Hello,world")

# a,b,c=4,3.4,"hello"
# print(a)
# print(b)
# print(c)

# a=[4,'h',2.3]
# print(a)
# print(a[0:2])
# print(a[2])


#tuple
# a=(10,4,0,"hello")
# print(a)
# print(a[2])
# a[2]=10  #error wrong


#dictionary
# dic={
#     1:"abdo",
#     2:"omar",
#     3:"sad"
# }
# print(dic)

# print(dic[1])


#convert
# a=float(5)
# print(a)
# a=dict([
#     [1,2],
#     [2,3]]
# )
# print(a)

# print("abd",end='')



#input
# age=input("enter your age:")
# print(age)


#if statement
# gpa=3.4
# if gpa>2.3:
#  print("throw")


#if/else
# gpa=4
# if gpa>3:
#     print("throw")
# else:
#     print("no throw")

#  if condition:
# 	        statements
# 	elif condition:
# 	        statements
# 	else:
# 	        statements

"""
multi line comments
"""

#loops

# for x in range(1,6):
#     print(x)

# for x in range(5,0,-1):
#     print(x)


#function
def abs(num):
    if num>=0:
        return num
    else:
        return -num
    
print(abs(5))
