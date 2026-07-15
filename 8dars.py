# FILE
# f=open("test.txt")
# BIRINCHI  MSASLA
# dct={}
# data=f.read().split("\n")
# for i in data:
#     if i.split(",")[-1] not in dct:
#         dct[i]=1
#     else:
#         dct[i]+=1
#     print(dct)


# VIZA MASALASI
# vise=[]
# for i in data:
#     if i.split(",")[1].lower() == 'visa':
#         vise.append(i.split(",")[-1])
        
# print(sorted(vise))
# karta=[]
# for i in data:
#     for x in range(10):
#          if str(x) in i.split(",")[0]:
#             print(f"""{karta[i.split(",")[-1]]}{karta[i].split(",")[2]}{karta[i].split(",")[3]}""")


# # print(karta)


# f.close()




# MASALA @+++++++++++++++++++++++++++++++++++++++++++++++++++++++==
# f=open("sinf.txt")
# data=f.read().split("\n")
# new=[]
# for i in data:
#     for x in i.split(",")[-2].split("-"):
#         # print(i.split(",")[-2].split("-"))
        
#             new.append(i[0])
#             print(i)
# print(new)


# # for i in data:
# #     if'Q'in i.split(",")[-2].split("-"):
# #         new.append(i[0])
# #     print(new)

# dct={}
# count=0
# for i in data:
#     if i.split(",")[0].split(".")[-1] not in dct:
#         dct[i.split(",")[0].split(".")[-1]]=1
#     else:
#         dct[i.split(",")[0].split(".")[-1]]+=1
# print(dct)

# f.close()
# ========================================================
f=open("sinf.txt")
data=f.read().split("\n")
# new=[]
# for i in data:
#     yosh=0
#     yosh=2026-int(i.split(",")[-2].split("-")[-1])
#     if yosh > 50:
#         print(i.split(",")[0])
new={}

for i in data:
    k=i.split(",")[2]
    yil=k.split("-")[-1]
    if int(yil)>= 1950 and int(yil) <=2005:
        if yil not in new:
            new[yil]=1
        else:
            new[yil]+=1
print(new)



f.close()
