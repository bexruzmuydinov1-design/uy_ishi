# JSON
import json
# with open("loyha.json") as f:
#     data=json.load(f)
#     b=data['branches']
#     for i in b:
#         print(i['name'])


# with open("loyha.json") as f:
#     data=json.load(f)
#     a=data['branches']
#     for i in  a:
#         t=i['teachers']
#         for x in t:
#             if 'Python' in x['subject']:
#                 print(f"{x}")



# with open("loyha.json") as f:
#     data=json.load(f)
#     count=0
#     a=data['branches']
#     for i in a:
#         print(i['name'])
#         s=i['students']
#         for x in s:
#             if 'id' in x:
#                 print(1)


# with open("loyha.json") as f:
#     data=json.load(f)
#     a=data['branches']
#     for i in a:
#         print(i['name'])
#         s=i['students']
#         for x in s:
#             print(x['payment'])
#             max_student = max(i["students"], key=lambda x: x["payment"])
#     print(max_student)



# with open("loyha.json") as f:
#     data=json.load(f)
#     a=data['branches']
#     sum=0
#     for i in a:
#         # print(i['name'])
#         s=i['students']
#         for x in s:
#                 sum+=x['payment']
#     print(sum) 
# 



# with open("loyha.json") as f:
#     data=json.load(f)
#     a=data['branches']
#     for i in  a:
#         t=i['teachers']
#         for x in t:
#             if x['experience'] >= 5:
#                 print(x['name'])




with open("loyha.json") as f:
    data=json.load(f)
    a=data['branches']
    for i in  range(len(a)):
        t=a[i]['teachers']
        flag = False
        for x in t:
            if x['subject'] != "Python":
                flag = True
        if flag:
            a[i] = a[i+1]
    else:
        print(a[i]['name'])
                




                
    

            

            
            

        

            
                