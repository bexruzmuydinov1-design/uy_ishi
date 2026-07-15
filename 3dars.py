# a=[1,'salom',True,1.34]
# for i in range(len(a)):
#     a[i] = type(a[i])

# print(a)
      
# =======
# lst1=[7,8,1,3,4,6,7,5]
# kvad=[]
# kub=[]
# for value in range (lst1):
#     if value %2==0:
#         kvad.append(value*value)
#     else:
#         kub.append(value*value*value)

# print(lst1)
# print("kvad",kvad)
# print("kub",kub)
# ====================
# a=[1,23,4,0,6,0,7,1,0,0,0,6,3]
# for i in a:
#     if i==0:
#         a.remove(i)
#         a.append(0)
# print(a)
# ==============
# a=[]
# b=[]
# for i in range(int(input("nechigacha"))):
#     a.append(int(input()))

# a.sort()
# print(a[-2])
# ==============
# a=[]
# for i in range(int(input("nechigacha"))):
#     a.append(int(input()))

# # a.sort()
# new=[]
# for index,value in enumerate(a):
#     if index-1==index:
#         a.remove(value)
# #   print(a)
# ===============================================
# a = []
# for i in range(int(input("Nechta son: "))):
#     a.append(int(input()))

# new = []

# for i in a:
#     if i not in new:
#         new.append(i)

# print(new)
# ==================================================
# a = []
# for i in range(int(input("Nechta son: "))):
#     a.append(int(input()))
# new=[]
# for i in a:
#     type(i) 
#     new.append(i)
#     print(i,new)    


# ================================
# a = []
# for i in range(int(input("Nechta son: "))):
#     a.append(int(input()))

# new = ""

# for i in a:
#     new += str(i)

# print(new)
# ======================================
# a=[]
# b=[]
# for i in range(int(input("Nechta son: "))):
#     a.append(int(input()))

# for i in range(int(input("Nechta son: "))):
#     b.append(int(input()))

# a.extend(b)
# natija = sum(a) / len(a)
# print("O'rta qiymat:", natija)
# ==========================
# a=['ada',212,211,'amma']
# for i,v in enumerate(a):
#     if str(v)==str(v)[:: -1]:
#         print(v,"Polindrom")
#     else:
#         print(v,"Polindrom emas")
# ======================
# a=['abc','xyz','aba','1221']
# co=0
# for i,v in enumerate(a):
#     if str(v[0])==str(v[-1]):
#         co+=1
# print(co)
# =====================
# a=[11,22,20,31,49,3,10]
# for i in a.copy():
#     if i%2==0:
#         a.remove(i)
# print(a) 
# ====================
# a=[[1,2,3],[2,2,2],[9,45],[9,10]]
# b = max(a, key=sum)

# print(b)
# ============
# a=[1,2,3]
# a[-1] += 1
# print(a)
    # ===================
# a=[1,2,3,5,7,12,13,15,4,5,6]
# b=[2,4,10,23,21,12,15,7,6,8,9]
# new=[]
# for i in a:
#     for ii in b:

#         if i==ii:
#             new.append(i)
# print(new)  

# ========================
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

# =============================
# a=[]
# for i in range(int(input("nechigacha"))):
#     a.append(int(input()))
# print(sum(a))
# =======================
# a=[]
# for i in range(int(input("nechigacha"))):
#     a.append(int(input()))
# print(max(a))
# ==================
# a=[]
# c=0
# for i in range(int(input("nechigacha"))):
#     a.append(int(input()))

# for i in a:
#     if i%2==1:
#         c+=1
# print(c)
# =======================
# a=[]
# for i in range(int(input("Nechigacha"))):
#     a.append(int(input()))

# for i,v in enumerate(a):
#     if v<0:
#         a.remove(v)
#         a.insert(i,0)
# print(a)
# ==========================
# a=[]
# for i in range(int(input("Nechigacha"))):
#     a.append(int(input()))
# print(a[::-1])
#===================
# a=[]
# for i in range(int(input("Nechigacha"))):
#     a.append(int(input()))
# a.sort()
# print(a[-2])
# ========================
# a=[]
# b=[]
# for i in range(int(input("Nechigacha"))):
#     a.append(int(input()))

# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# ======================
# a=[1,2,3,4]
# a[0],a[-1]=a[-1],a[0]
# print(a)
# ]===================
# a = [10, [20, 30], [40, [50, 60]], 70]
# a[2][1]=100
# print(a)
# ===================
# a=[]
# new=[]
# for i in range(int(input("Nechigacha"))):
#     a.append(int(input()))   

# for i in a:
#     if i not in new:
#         new.append(i)
# print("before",a)
# print("After",new)
# =====================
# a=[1,2,3,4,4,4,4,2]
# for i in a:
#     print(a.index(2))
# a=int(input("Yosh"))
# b=input("Ism")
# if a==3 and b=='Ali':
#     print("KOT BALA")
# else:
#     print("Yhashi bola")

