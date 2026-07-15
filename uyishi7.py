def kalendar(a:str):
   kun=a[:2]
   oy=a[:5]
   yil=a[6:]
   if '01' in oy:
      print(f"{kun[1]}Yanvar{yil}yil")
   elif '02' in oy:
    #   print(kun[1],'Fevral',yil,"yil")
      print(f"{kun[1]}Fevral{yil}yil")
   elif '03' in oy:
    #   print(kun[1],'Mart',yil,"yil")
      print(f"{kun[1]}Mart{yil}yil")
   elif '04' in oy:
    #   print(kun[1],'Aprel',yil,"yil")
      print(f"{kun[1]}Aprel{yil}yil")
   elif '05' in oy:
    #   print(kun[1],'May',yil,"yil")
      print(f"{kun[1]}May{yil}yil")
   elif '06' in oy:
    #   print(kun[1],'Iyun',yil,"yil")
      print(f"{kun[1]}Iyun{yil}yil")
   elif '07' in oy:
    #   print(kun[1],'Iyul',yil,"yil")
      print(f"{kun[1]}Iyul{yil}yil")
   elif '08' in oy:
    #   print(kun[1],'Avgust',yil,"yil")
      print(f"{kun[1]}Avgust{yil}yil")
   elif '09' in oy:
    #   print(kun[1],'Sentyabr',yil,"yil")
      print(f"{kun[1]}Sentyabr{yil}yil")
   elif '10' in oy:
    #   print(kun,'Oktyabr',yil,"yil")
      print(f"{kun[1]}Oktyabr{yil}yil")
   elif '11' in oy:
    #   print(kun,'Noyabr',yil,"yil")
      print(f"{kun[1]}Noyabr{yil}yil")
   elif '12' in oy:
    #   print(kun,'Dekabr',yil,"yil")
      print(f"{kun[1]}Dekabr{yil}yil")

u=input('datani dd.oy.yil "01.02.2022 PRIMER"\n ')
print(kalendar(u))
        
# =======================================================
# def bal(a:list[dict]):
#     new={}
#     for key, v in data:
#         if len(data)<=1:
#             print("User bitta")
#             # break
#         if key in new:
#             new[key] += v
#         else:
#             new[key] = v

#     max1 = max(new, key=new.get)
#     print(max1, new[max1])


# data = [
#     ("user1", 50),
#     ("user2", 60),
#     ("user1", 40),
#     ("user3", 30)
# ]
# bal(data)















