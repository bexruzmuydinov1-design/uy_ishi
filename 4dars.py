# tpl=(1,2,3), (2,2), (3,0,0)
# lst=list(tpl)
# print(lst[::-1])
# /=================
# tpl=[(123,4,2,6)]
# new=[]
# if tpl==type(tpl):
#     new.append(list(tpl))
# print(new)
# [[==================]]
# tpl=('salom','amma',12,212)
# for i,v in enumerate(tpl):
#     if str(v)==str(v)[:: -1]:
#         print(v,"Polindrom")
#     else:
#         print(v,"Polindrom emas")
# ==================
# tpl=[(1,2), (3,4), (8,9)]
# nol=[]
# bir=[]
# for i,v in enumerate(tpl):
#     # for i,v in enumerate(tpl):
        # if i==0:                #notogri
#             nol.append(v)
#         elif i==1:
#             bir.append(v)
# print(nol,bir)




# a = [(1, 2), (3, 4), (8, 9)]

# new = []

# for i in range(len(a[0])):
#     natija = []
#     for j in range(len(a)):
#         natija.append(a[j][i])
#     new.append(tuple(natija))

# print(new)

# lst=[(1,2),(2,3),(3,4)]
# new=[]
# for i in lst:
#     new.append(list(lst))
#     break
# print(new)

# =================

# a=[(1,2,3), (2,2), (3,0,0)]
# print(a[::-1])



# ===================
# a=[]
# for i in range(int(input("ism familiya"))):
#     a.append(int(input()))  


# =[========]
# ism =   ["Oybek Nuriddinov", "Azizbek Karimov", "Jamshid Tursunov"]
# print(sorted(ism))
# =================
# a=[3,5,7,9]
# new=[]
# for i in a:
#     i+=1
#     new.append(i)
# print(new)
# ===================

# a=[1,2,4,5,6,7,7]
# target  = int(input(""))
# for i in range(len(a)):
#     for x in range(i+1,len(a)):
#         if a[i] + a[x] == target:
#             print(i, x)
            
# ====================
# a=[1,1,2,2,3,4,4,5]
# new=[]
# for i in a:
#     if a.count(i)==1:
#         print(i)
#         break
# a=[12,23,34,45,56]
# new=[]
# # a=''.join(key=lambda x: (x[1])%2==0)
# # print(a)
# for i in range(len(a)):
#     if a[i]%2==0:
#         print(a[i])


# ========================
# a=[1,2,2,3,3,4,5]
# new=[]
# for i in range(len(a)):
#     if a[i]!=a[i-1]:
#         new.append(a[i])
# print(new)
    
# Royxat=[ 3, 5, 6, 34, 78, 33, 23]
# user=input("search son; ")
# for i,v in enumerate(Royxat):
#     s=str(v)
#     if user in s and len(s)>= 2 and s [0]==s [1] :
#         print(s,user)
# ==============
# n=int(input())
# new=[]
# for i in range(1,n+1):
#     new.append(1)
#     for x in range(i-1):
#         new.append(0)
# print(new)
# a=[1,1,2,3,4,3,0,0]
# new=[]
# for i in a:
#         if i not in new:
#                 new.append(i)
# print(new)
# a=[3, 4, 0, 0, 6, 2, 0]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(0)
# print(a)
# a=[
#  [2, 15, 4],
#  [19, 24, 11],
#  [7, 9, 5],
#  [10, 3, 1]
# ]
# b=[]
# for i in range(len(a)):
#     for x in range(len(a)):
#         b.append(x**2)
# print(b)


    