# DCT===============DCT=====================DCT================DCT========================DCT==========================DCT
# dct ={
#     'ten' : 10,
#     'twenty' : 20,
#     'thritty' : 30
# }
# print(dct)
# dct ={}
# key = {
#     'ten',
#     'twenty',
#     'thorty'
# }
# v={
#     10,
#     20,
#     30
# }
# ====================chala
# dct={
#     'a' : 10,
#     'b' : 200,
#     'c' : 200
# }
# for i in dct:
#     if dct[i] == 200:
#         print('bor')
# ===============================
# dct ={
#     1:10,
#     2:20,
#     3:45,
#     4:40
# }
# dct.pop((max(dct)))
# dct.pop((min(dct)))
# print(dct)
# chala
# ==========================
# d1={
#     1:10,2:20
# }
# d2={
#     3:30,4:40
# }
# d3={
#     5:50,6:60
# }
# new={}
# new.update(d1)
# new.update(d2)
# new.update(d3)
# print(new)
# ========================
# # ======================
# dct ={
#     1:100,
#     2:-54,
#     3:247
# }
# sum=0
# for i in dct.values():
#     sum+=i
# print(sum)
# =========================
# d={
#     'salom' : 12,
#     'ali' : 13,
#     'elbek' : 29,
#     'oy' : 101
# }
# d.keys()
# print()



# dct = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# } 

# for i in dct:
#     key = input("ism ")
#     a=int(input("ball"))
#     if key in dct :
#         dct[i] = a
#         print(dct)
#         break
#     else:
#         print('unaqasi yoq')
#         break


# ===========================
# dct = {
#     "olma": 5000,
#     "banan": 7000
# }
# for i in dct:
#     key = input("nomi ")
#     a=int(input("narx"))
#     if key in dct :
#         print("Allaqachon bor")
#         break
#     else:
#         dct[key] = a
#         break
# print(dct)
# =================================
# dct = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }
# for i in dct:
#     a=input("id; ")
#     if a in i:
#         dct.pop(a)
#         print("Ochirildi")
#         break
#     else:
#         print("topilmadi")
#         print(dct)
#         break
# ====================================
# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }


# a=(max(prices.values()))
# b=(max(prices, key=prices.get))
# print(b,a)
# ===============
# cart = {
#     "olma": 3,
#     "banan": 5,
#     "uzum": 2
# }
# sum=0
# for i in cart:
#     sum+=cart[i]
# print(sum)
# =================================
# student = {
#     "name": "Aziz",
#     "age": 20,
#     "contact": {
#         "phone": "+998971234567",
#         "email": "aziz@mail.com"
#     }
# }    

# if 'contact' in student:
#     print(student["contact"]["phone"])



# /========================
# d1 = {"olma": 5000, "banan": 7000}
# d2 = {"shaftoli": 8000, "olcha": 10000}
# new={}
# new.update(d1)
# new.update(d2)
# print(new)
# /======================
### 🧩 Vazifa ### 🧩 Vazifa
# dct= [
#     {"customer": "Ali", "amount": 15000},
#     {"customer": "Vali", "amount": 22000},
#     {"customer": "Ali", "amount": 8000}
# ]

# new={}
# v={}
# sum=0
# # for i in dct:
# #     if i['customer'] in i['customer']:
# #         sum+= i["amount"]
# # print(sum)     




# for i in range(len(dct)):
#     for j in range(i + 1, len(dct)):
#         if dct[i]["customer"] == dct[j]["customer"]:
#             sum+=dct[i]["amount"]
#             sum+=dct[j]["amount"]
#             new=dct[i]["customer"]
#             v=dct[j]["customer"]

# print(new,sum)
# print(dct[i]["customer"])
# ]=============================================][]][]
# a=input('sATR')
# # a=dict(a)
# for i,v in enumerate(a):
#     if v==v:
#         print('salom')
# ===========================last one
# products = {
#     "Laptop": 700,
#     "Mouse": 25,
#     "Phone": 350,
#     "Camera": 500,
#     "Keyboard": 45
# }
# new={}

# for i in products:
#     if products[i]<100:
#         new[i]=products[i]
# print(new)



# dct={'a':100,
#      'c':10,
#      'd':11,
#      'k':13,
#      'i':19,
#      'b':99}
# print(sorted(dct.items(),key=dct.get))






