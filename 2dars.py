# a=int(input())
# b=int(input())
# c=int(input())
# if b>a and b<c:
#     print("Xa ortasida")
# else:
#     print("Yoq")
# ==============
# a=int(input())
# b=int(input())
# c=int(input())
# count=0
# if a>0:
#     count+=1
# if b>0:
#     count+=1
# if c>0:
#     count+=1        
# print(count,"Ta musbat")   
# ============= 
# a=int(input())
# b=int(input())
# c=int(input())
# natija=0
# if a>b and a>c:
#     pass
# elif b>a and b>c:
#     natija=a+b
#     print(natija)
# if b>a and b>c:
#     pass
# elif c>a:
#     natija=b+c  
#     print(natija) 
# =======================
# a=int(input())
# b=int(input())
# if a%2==1 and b%2==1:
#     print("toq")
# else:
#     print("toq emas")
# ===========
# a=int(input())
# b=int(input())
# if a%2==1 or b%2==1:
#     print("ikallasidan bittasi toq")
# else:
#     print("umuman toq yoq")
# ================

# a=int(input())
# if a>=10 and a%2==0:
#     print(" ikki xonali",a)
     
# ==================
# a=int(input())
# if a>99 and a%2==1:
#     print(a)
# =======
# a=input()
# if int(a[0]) == int(a[1]) and int(a[0]) == int(a[2]) and int(a[1]) == int(a[2]):
#     print("TENG")
# else:
#     print("TENG EMAS")

# film=input("Film nomi")
# yosh=int(input("Yosh"))
# if yosh<12:
#     print(yosh,"yosh li mijozimizga" " " "Animatsiya yoki Oila janrini tavsiya qilaman")
# elif yosh>12 or yosh<=18:
#     print(yosh,"yosh li mijozimizga" " " "Action yoki Sarguzasht janrini tavsiya qilaman")
# elif yosh==18 or yosh>60:
#     print(yosh,"yosh li mijozimizga" " " "Drama yoki Komediya janrini tavsiya qilaman")
# else:
#     print(yosh,"yosh li mijozimizga" " " "Dokumental yoki Klassik janrini tavsiya qilaman")
# =========================
# t1=int(input("1tovar"))
# t2=int(input("2tovar"))
# t3=int(input("3tovar"))
# summa=t1+t2+t3
# if summa>100 or summa<=199:
#     print("Jami",summa)
#     print("Chegirma 10%")
#     print(float(summa*0.9))
# elif summa>200 or summa<-499:
#     print("Jami",summa)
#     print("Chegirma 15%")
#     print(float(summa*0.85))
# elif summa>500:
#     print("Jami",summa)
#     print("Chegirma 20%")
#     print(float(summa*0.8))
# ===================================
# while 1:
#     a=(input("Xaroratni kirit; "))
#     if a=="exit":
#         print("Dastur tugadi ")
#         break
#     elif int(a)<5:
#         print(a,"°F Muzlash")
#     elif int(a)>35:
#         print(a,"°F Issiq")
#     elif int(a)>=15 or int(a)<=30:
#         print(a,"°F Yaxshi kun")
# ================ SINF ISHI OXIRGISI======================================
# for i in range(1,4):
#     a=input('kompaniya nomi; ')
#     narx=(input("Narx; "))
#     if int(narx)>100:
#         print(a,int(narx),"$----_QIMMMAT_----")
#     elif int(narx)<50:
#         print(a,int(narx),"$----_ARZON_----")
#     elif int(narx)>=50 and int(narx)<=100:
#         print(a,int(narx),"$----_ORTACHA_----")
# ===============
# parol = input("Parol: ")
# for i in parol:
#     if len(parol) < 8:
#         print("Kamida 8 ta belgi kerak")
#         break
#     elif parol.isdigit():
#         print("Parol faqat raqamlardan iborat")
#         break
#     elif parol.isupper() :
#         print("Katta harf yoq")
#         break
#     elif '!@#$%^&*' in parol:
#         print("Belgi yoq")
#         break
#     else:
#         print("ZOR PAROL")
#         break

# a = []
# a.insert[1,2,56]
# a.pop(0)
# a.remove(2)
# a.insert(2,9)
# b=int(input('Nechigacha bolsin'))
# for i in range(b):
#     x = int(input())
#     a.append(x)
# a.append(101)    
# a.sort()
# print(a)
# a=[1,3,5,6,8]
# a.sort(reverse=True)
# print(a)


def isPalindrome(a:str):
    if a==a[::-1]:
        print("Polindrom")

a=(input(""))
isPalindrome(a)







