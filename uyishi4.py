# a=[1,2,4,5,6,7,7]
# target  = int(input("TARGETNI KIRITING; "))
# for i in range(len(a)):
#     for x in range(i+1,len(a)):
#         if a[i] + a[x] == target:
#             print(i, x)
# ===============================2
# a=lst = [1, 4, 6, 8]
# new=[]
# for i in a:
#     new.append(i*2)
# print(new)
# =========================3
# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# lst[2]=(70,80,100)
# print(lst)
# =================================4
# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]

# new=[]

# for i in lst:
#     if  i:
#         new.append(i)

# print(new) 
# ===============================5
# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# lst.sort(key=lambda x: float(x[1]), reverse=True)
# print(lst)
# ======================6
# s=input("Matn")

# new= tuple(s)

# print(new)
# =======================7
# lst = [1, 2, 3, 4]
# prefix =input("m; ")
# lst=prefix.join(str(lst))
# print(lst)
# =======================8
# a=input('>>')
# new=[]
# # for i in a:
# new.append(''.join(list(a)))
#     # break

# print(new)
# ==================================9
# lst = [12, 'salom', 4.5, 'dunyo', True]
# new=[]
# for i in lst:
#     if type(i)==str:
#         new.append(i)
# print(new)
# ==============10
# t = (-3, 5, 0, 9, -1, 4)
# new=()
# for i in t:
#     if i>0:
#         new+=(i, )
# print(new)
# ==========================11
# lst = ['salom', 23, 'dunyo', 5, 100, 'python']
# string=[]
# num=[]
# for i in lst:
#     if type(i)==str:
#         string.append(i)
#     elif type(i)==int:
#         num.append(i)
# print(string,num)
# ========================12
# lst = [(3, 10), (1, 20), (2, 30)]
# lst.sort(key=lambda x: x[0])
# print(lst)
# ============================13
# lst = [1, 2, 3, 4]
# new=[]
# for i in lst:
#     i=i**2
#     new.append(i)
# print(new)
# =============14
# lst = ['salom', 'dunyo', 'python']
# for i in range(len(lst)):
#     lst[i]=lst[i][0].upper() + lst[i][1:]
# print(lst)
# ======================15
# t = (1, 2, 3, 4, 6)
# sum=0
# for i in range(len(t)):
#     sum+=t[i]
# print(sum)
