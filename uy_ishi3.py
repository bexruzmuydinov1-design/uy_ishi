# a=['salom',1,5,9,2,'a',True,2]
# count=0
# for i in a:
#     if type(i)==int:
#         count+=1
# print(count)
# uy ishi 2=======================2
# a=['salom',1,5,9,2,'a',True,2]
# b=[]
# for i in a:
#     if type(i)==int:
#         b.append(i)
# print(max(b))
#  ===========================3
# a=['ada',212,211,'amma']
# count=0
# for i,v in enumerate(a):
#     if len(a)>=2:
#         if str(v)==str(v)[:: -1]:
#             count+=1
# print(count)
# =======================4
# a=[1,'salom',True,1.34]
# for i in range(len(a)):
#     a[i] = type(a[i])

# print(a)
# ===============5
# a=[7,8,1,3,4,6,7,5]
# new=[]
# for i,v in enumerate(a):
#     if i%2==0:
#         new.append(v**2)
#     else:
#         new.append(v*v*v)
# print(new)       
# ======================6
#  
# a=[2,3,46,71,9,42,2]
# a.sort()
# b=a.pop(-2)
# print(b)
# ==============7
# a=[1,2,34,56,7]
# b=[3,5,1,8,21]
# a.extend(b)
# a=sum(a)/len(a)
# print(a)
# =======================8
# a=['ada',212,211,'amma','aziza']
# for i,v in enumerate(a):
#     if str(v)==str(v)[:: -1]:
#         print(v,"Polindrom")
#     else:
#         print(v,"Polindrom emas")
# ==================================9
# import random
# a=[1,3]
# b=int(input("Necta qoshilsin"))
# for i in range(b):
#     a.append(random.randint(1, 10))

# print(a)
# ======================10
# a=[5,3,8,1]
# for i, v in enumerate(a):
#     if i == 0:
#         continue 
#     if i > 0 and a[i - 1] > v:
#         print("tartibsiz")
#         break
#     elif v > a[i-1]:
#         print("kamayish")
#         break
#     else:
#         print("osish")
#         break
# ===============================11
# a=[1,0,0,0,2,0,5,9,6,0,90,0,9,0,0,0,0,0,0]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(0)
# print(a)
# ==================================12
# a = [[2, 15, 4], [19, 24, 11], [7, 9, 5], [10, 3, 1]]
# new = []
# for i, v in enumerate(a):
#     b = []
#     for x in v:
#         if i % 2 == 0:
#             b.append(x ** 2)
#         else:
#             b.append(x ** 3)
#     new.append(b)
# print(new)
# ===========================13
a = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
a[2][2] = [6000, 7000]
print(a)