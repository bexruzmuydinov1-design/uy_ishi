# JSON
import json
# with open("sinf.json","w") as f:
#     lst=[
#         {"nomi":"olma","narxi":15000,"soni":3},
#         {"nomi":"non","narxi":500,"soni":10},
#         {"nomi":"cola","narxi":5000,"soni":30},
#         {"nomi":"tarvuz","narxi":15000,"soni":5}
#     ]
#     json.dump(lst,f,indent=4)
# with open("sinf.json") as f:
#     data=json.load(f)
#     sum=0
#     for i in data:
#         sum+=i["narxi"]
    
#     print(sum)
# =========================================
# with open("shaxar.json",'w') as f:
#     lst=[
#         {"shaxar":"Farg`ona","axoli":1500000},
#         {"shaxar":"Toshkent","axoli":2500000},
#         {"shaxar":"Samarqand","axoli":1000000},
#         {"shaxar":"Jizzax","axoli":7500000},
#         {"shaxar":"Andijon","axoli":5000000}
#     ]
#     json.dump(lst,f,indent=4)

# with open("shaxar.json") as f:
#     data=json.load(f)
    
#     for i in data:
#         max=0
#         if i['axoli']>max:
#             max=i['axoli']
#     print(max)
# =============================================
# with open("market.json","w") as f:
#     lst=[{"id": 1, "product": "P001", "material": "plastik", "price": 750, "is_available": 'true'},
#   {"id": 2, "product": "P002", "material": "metall", "price": 1200, "is_available": 'false'},
#   {"id": 3, "product": "P003", "material": "shisha", "price": 950, "is_available": 'true'},
#   {"id": 4, "product": "P004", "material": "yog'och", "price": 450, "is_available": 'false'},
#   {"id": 5, "product": "P005", "material": "plastik", "price": 600, "is_available": 'true'},
#   {"id": 6, "product": "P006", "material": "temir", "price": 300, "is_available": 'false'},
#   {"id": 7, "product": "P007", "material": "alyuminiy", "price": 700, "is_available": 'true'},
#   {"id": 8, "product": "P008", "material": "metall", "price": 850, "is_available": 'true'},
#   {"id": 9, "product": "P009", "material": "shisha", "price": 1500, "is_available": 'true'},
#   {"id": 10, "product": "P010", "material": "plastik", "price": 999, "is_available": 'true'},
#   {"id": 11, "product": "P011", "material": "temir", "price": 980, "is_available": 'false'},
#   {"id": 12, "product": "P012", "material": "yog'och", "price": 520, "is_available": 'true'},
#   {"id": 13, "product": "P013", "material": "alyuminiy", "price": 890, "is_available": 'false'},
#   {"id": 14, "product": "P014", "material": "plastik", "price": 670, "is_available": 'true'},
#   {"id": 15, "product": "P015", "material": "metall", "price": 450, "is_available": 'false'},
#   {"id": 16, "product": "P016", "material": "shisha", "price": 730, "is_available": 'true'},
#   {"id": 17, "product": "P017", "material": "yog'och", "price": 980, "is_available": 'false'},
#   {"id": 18, "product": "P018", "material": "alyuminiy", "price": 510, "is_available": 'true'},
#   {"id": 19, "product": "P019", "material": "plastik", "price": 1100, "is_available": 'false'},
#   {"id": 20, "product": "P020", "material": "temir", "price": 640, "is_available": 'true'}
# ]
#     json.dump(lst,f,indent=4)

# with open("market.json") as f:
#     data=json.load(f)
#     for i in data:
#         if i['price']>=500 and i['price']<=1000:
#             if i['is_available']=='true':
#                 print(i["id"])
#                 print(i['material'])


# with open("market.json") as f:
#     data=json.load(f)
#     for i in range(int(input("necta"))):
#         mat=input(">>>>")
#     narx={}
#     for i in data:
#         if i['material']==mat and i["is_available"]=='true':
#             narx=i['price']
#             print(narx)


# with open("market.json") as f:
#     data=json.load(f)
#     for i in data:
#         if i["is_available"]=='false' and i['price']<1000:
#             print(i['material'])

                


# with open("student.json") as f:
#     data=json.load(f)
#     for key,v in data.items():
#         print(key)
#         for x in v.items():
#             print(sum(x[1])/len(x[1]))



# with open("zakaz.json") as f:
#     data=json.load(f)
#     new={}
#     for k,v in data.items():
#         for i in range(len(v)):
#             if v[i]['customer'] not in new:
#                 new[v[i]['customer']]=v[i]['amount']
#             else:
#                 new[v[i]['customer']]+=v[i]['amount']

#     print(new)


# with open("sinf.json") as f:
#     data=json.load(f)
#     new={}
#     htdml={}
#     for k1,v1 in data.items():
#         for k,v in v1.items():
#             sum=0
#             for i in range(len(v)):
#                 sum += v[i]['grade']
#             print(f"{k}: {sum / len(v)}")
 
# with open("market.json") as f:
#     data=json.load(f)
#     for k,v in data.items():
#         for i in range(len(v)): 

#             exp=(max(v,key=lambda x:x['price'])) 
#     print(k,exp)              


# with open("sinf.json") as f:
#     data=json.load(f)
#     new={}
#     for k,v in data.items():
#         for i in range(len(v)):
#             if v[i]['month'] not in new:
#                 new[v[i]['month']]=v[i]['amount']
#             else:
#                 new[v[i]['month']]+=v[i]['amount']
#     print(new)



# with open("social.json") as f:
#     data=json.load(f)
#     new=[]
#     for k,v in data.items():
#         for i in range(len(v)):
#             if len(v[i]['social']) >= 2:
#                 new.append(v[i]['name'])
#     print(new)


with open("odam.json") as f:
    data=json.load(f)
    for k,v in data.items():
        for i in v:
            print(f"{i['name']}\t{sum(i['grades'])/len(i['grades'])}")
        
    







            
            







        
        


