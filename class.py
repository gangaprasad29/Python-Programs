
# var=1
# add=var+1
# print(add)

# l=[1,2,3,4,5,6,8,7,9]
# tup=(2,3,5)
# s={1,2,4}
# dic={5,6,7}
# for i in range(5):
#     for j in range(9):
#      print(i+j)
###time complexity    
# addition=O(1)
#O(n) where n is size of list
#O(n**2) 
#O(n**n) for 3 loops O(n**3)
#O(2^n)
#O(log(n)) #binary search
#O(nlog(n)) 

##space complexity
#O(1)
#O(n)
#O(n**2)



# l=[1,2,3,4,5,6,8,7,9]
# num=1
# for i in range(len(l)):
#     if(l[i]==num):
#         print("YES")
#         break



# l=[1,4,5,6,8,3,2,7,9]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)



###Q
# a=int(input("speed of alice"))
# if (a<=40):
#     print("no fined")
# elif(a>40):
#     print("fined")

#Q
##a,b=map(int,input().split())   OR
# a=int(input("enter attendance"))
# b=int(input("enter marks"))
# if(a<50):
#     print("grade:Z")
# elif(a>=50 and b<50):
#     print("grade:F")
# else:
#     print("grade:A")

#Q
# Ai=list(map(int,input().split()))
# l=Ai.remove(min(Ai))
# a=sum(Ai)
# print(a)

#Q
# a,b,c=map(int,input().split())
# for k in range(2,100):
#  if(a%k!=0 and b%k!=0 and c%k!=0):
#   print(k)
#   break
  

# l=[1,2,3,4,5]
# # prefix=[1,3,6,10,15]
# prefix=[]
# for i in range(len(l)):
#     total=0
#     for j in range(i+1):
#         total+=l[j]
#     prefix.append(total) 
# print(prefix)       

##OR

# l=[1,2,3,4,5]
# suffix=[1]
# for i in range(1,len(l)):
#     prefix.append(l[i]+prefix[-1])
# print(prefix)



# l=[1,2,3,4,5]
# suffix=[5]
# for i in range(len(l)-2,-1,-1):
#     suffix.append(suffix[-1]+l[i])
# print(suffix)








