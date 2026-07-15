# def Malumot (a:str):
#     new={}
#     for i in a:
#         if i not in new:
#             new[i] = 1
#         else:
#             new[i] += 1
#     return new



# b=input("Satr; ")
# print(Malumot(b))
# ========================================
# def yoniga(a:str,b:int):
#     m=a+str(b)
#     return m


# s=yoniga('k',123)
# print(s)

# =============================


# /=========================
# def Bosh (a:str):
#     for i in a:
        

        
        
        

        

# chala




# b=input("Satr; ")
# print(Bosh(b))



# def dcct(a:dict,b:dict):
#     for i in b:
#         if i in a:
#             a[i] += b[i]
#         else:
#             a[i] = b[i]
#     print(a)

# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'d':300}            
# dcct(d1,d2)
# =============================
def gmail(a:str):
    a=a[-9:]




def xisob (a:str):
    new={}
    for i in a.split():
        if i not in new:
            new[i] = 1
        else:
            new[i] += 1
    return new


# b=input("Satr; ")
# print(xisob(b))
# ==
# def dokoon(a:list[int]):
#     for i in a:
#         i=float(i)*1.12
#         return i


# a=input("")
# print(dokoon(a))

# ========================
# def gmail(a:list[str]):
#     new=set()
#     for i in a:
#         new.add(i.split(" ")[1])
#     return(new)

# print(gmail(["Ali, ali@gmail.com", "Vali, vali123@mail.ru", "Aziza, aziza@outlook.com"]))
# ==============================
# def smart(status:str,maxsulot:list):
#     ss=sum(maxsulot)
#     if 'VIP' in status:
#         ss=float(ss)*0.15
#         print("VIP mijozimizga 15"'%' "skidka",ss)
#     elif 'Premium' in status:
#         ss=float(ss)*0.10
#         print("Premium mijozimizga 10"'%' "skidka",ss)
#     elif 'oddiy' in status:
#         print("Skidka yoq",ss)

# smart('oddiy',[12000,45000,80000,15000])
# =====================================
# def parol(a:list):
#     new=[]
#     for i in a:
#         if len(i)>8 and '!@#$%^&*()' in a:
#             new.append(i)
#         print(new)
        


# ================================
# def bal (a:list[int]):
#     new=[]
#     for i in a:
#         # print(i)
#         if i>60:
#             new.append(i)
#         # new.sort()
#     return new


# a=[55, 60, 75, 90, 45]
# print(bal(a))



# a={'banan','olma','nok'}
# b={'olma','nok','molina'}
# print(a.difference(b))
# print(a.intersection(b))
# print(a | b)
# print( a ^ b)
# print(a - b)
# print(a & b)
# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a,b)

# a = [1, 2, 3]

# print(a * 2 + [4])
# a=700
# print(a//100)


# a = [1, 2, 3, 4]

# for i in range(len(a)):
#     print(a[i])
# 





# a = [1, 2, 3]

# for i in a:
#     i += 10

# print(a)



# a = [1, 2, 3, 4, 5]

# print(a[1:4:2])



# a = [1, 2, 3, 4]

# for i in range(len(a)):
#     a[i] = a[i] + a[i - 1]

# print(a)




# def second_max ( a  : list):
#     a=list(set(a))
#     a=sorted(a)
#     return a[-2]

# b=[5, 3, 8, 8,6, 2, 5]
# print(second_max(b))



# def katta(a,b,c,d):
#     return max(katta)


# print(katta(1,2,3,4))



