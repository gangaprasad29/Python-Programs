####BINARY SEARCH
#list should be sorted

# l=[1,2,3,4,5,6,7,8,9,10]
# ele=4
# start , end = 0 , 9
# found=False
# while(start<=end):
#     mid=(start+end)//2
#     print(start,mid,end)
#     if(l[mid]==ele):
#         found=True
#         break
#     elif(l[mid] >ele):
#         end=mid-1
#     else:
#         start=mid+1
# print(found)        


#Q

# A,B,X,Y=map(int,input().split())
# messi_score=(2*A)+B
# ronaldo_score=(2*X)+Y
# if(messi_score<ronaldo_score):
#     print("ronaldo")
# elif(messi_score>ronaldo_score):
#     print("messi")
# else:
#     print("equal")

#Q

# l=list(map(int,input().split()))
# m=list(map(int,input().split()))

# l.remove(min(l))
# a=sum(l)

# m.remove(min(m))
# b=sum(m)

# if(a>b):
#     print("alice")
# elif(b>a):
#     print("bob")
# else:
#     print("tie")

### OR 
    
# a,b,c,d,e,f=map(int,input().solit())
# alice=a+b+c
# bob=d+e+f
# am=min(a,b,c)
# bm=min(d,e,f)
# alice-=am    
# bob-=bm    



#Q

# n=int(input("size of list"))
# a=list(map(int,input().split(" ")))
# b=list(map(int,input().split(" ")))

# a_count=0
# b_count=0
# for i in range (0,n):
#  if(a[i]>b[i]):
#     a_count+=1
#     if(b[i]>a[i]):
#       b_count+=1
#     else:
#      a_count+=1
#      b_count+=1
# if(a_count>b_count):
#   print("alice")
# elif(b_count>a_count):
#   print("bob")
# else:
#   print("tie")       
      
      
### revision
#tuple sathi , aste pratyek element nanter

# t1=(1,)
# print(t1)
# print(type(t1))
# list are orderd and changable
# dictionary are orderd and changable &no duplicates
# tuple are orderd and unchangable & duplicates
# set are unorderd and unchangable

# l1=[1,2,3,4,5]
# t1=[23,42,54,56,76,6]
# t1.extend(t1)
# print(t1)

# l1=[1,2,3,4,5]
# n=l1.count(1)
# print(n)
# print(l1.index(2))

# l1=['a','b','c','d']
# l2=[11,23,34,56]
# print(l2)
# l2[3]=5
# print(l2)

## list: append clear copy count extend index insert pop remove reverse sort 
## set: add update diskart pop clear del isdisjoint remove
## dictionary: clear copy fromkey get itomes keys popp setdefaults update values
## tuple: 

# t1=(1,2,3,4,5,6)
# t2=(15,24,34,42,52,24)
# t3=t1+t2
# print(t3)

# print(list((12,3,4,5)))
# print(set((1,21,2,4)))
# print(tuple((2,3,4,5,1)))

# l1=[1,2,3,4,5,6]
# l2=[x for x in l1 if x<3]
# print(l2)
# l2=[x if x<3 else 2 for x in l1]
# print(l2)


##2D & 3D list

##2D
# l=[[1,2,33,3,66],[5,6,9,8],[55,6,4,7],[5,9,7,46]]
# print(l[0],l[1],l[2])
# l[0][3]=4
# print(l[0],l[1],l[2])






