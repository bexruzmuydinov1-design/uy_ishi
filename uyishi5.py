data = [
    {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
    {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
    {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
    {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
    {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
    {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
    {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
    {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
    {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
    {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
    {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
    {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
    {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
    {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
    {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
    {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
    {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
    {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
    {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
    {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
    {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
    {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
    {"full_name":"Dyana Crosby","company":"Riffpath","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
    {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
    {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Professor","salary":"$3172.57"},
    {"full_name":"Gaynor Dannohl","company":"Riffpath","position":"Administrative Assistant II","salary":"$3035.89"},
    {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
    {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
    {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
    {"full_name":"Rochelle Andrejevic","company":"Riffpath","position":"VP Product Management","salary":"$1734.61"}
]
# massala 1

# count=0
# for i in data:
#     if i["position"]=="Human Resources Manager":
#         count+=1
# print(count)

# ======masala2=====================================================================

# for i in data:
#     i["salary"] = i ["salary"][1:]

# sum=0
# count=0
# for i in data:
#     if i['company']=="Riffpath":
#         sum+= float(i["salary"])
#         count+=1

# print(count,"Ta  xodim Riffpath companiyda ishlaydi va ularni umumiy maoshi",float(sum))

# =============masala3====================================================================

# for i in data:
#     i["salary"] = i ["salary"][1:]
# sum=0
# count=0
# for i in data:
#     if i["full_name"][0] == 'K':
#         sum+=float(i["salary"])
#         count+=1
# print(count,"ta xodimni ismi k dan boshlanadi",'$'+str(sum*2))

# masala 4===========================================================

# for i in data:
#     i["FIO"]=i.pop("full_name")
# print(data)
# masala 5=========================================================

# for i in data:
#     if "Senior" in i["position"] or  "Junior" in i["position"]:
#         # i.pop("full_name")
#         # i.pop("company")
#         # i.pop("position")
#         # i.pop("salary")
#         i.clear()
# print(data)

# ==================masala6===============

# count=0
# for i in data:
#     if "Assistant" in i["position"]:
#         count+=1
# print(count)

# ==============================masala====7
 
# for i in data:
#     if "Assistant" in i["position"]:
#         i["position"]=i["position"].replace("Assistant","Junior")
        
# print(data)
