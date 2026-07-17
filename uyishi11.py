
# ===============================================masala1
# a=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# b=[]
# for i in a:
#     if i not  in b:
#         b.append(i)
# print(b)
# =========================masala2
# a = [ 
#     [1, 2], 
#     [3, 4] 
# ] 
 
# b = [ 
#     [5, 6], 
#     [7, 8] 
# ] 
# new=[]
# new.append(a[0][0]+b[0][0])
# new.append(a[0][1]+b[0][1])
# new.append(a[1][0]+b[1][0])
# new.append(a[1][1]+b[1][1])
# print(new)
# ===============================masala3
# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     cou=0 
#     for i in grades:
#         if i>=passingGrade:
#             cou+=1
#     return cou,'Otish bali',passingGrade


# lst=[80, 90, 66, 61, 60]
# bal=int(input("O`tish bali; "))
# print(count_passing_students(lst,bal))
# =========================================masala4
def ends_with_gram(a:str):
    new=[]
    for i in a:
        if i[-4:].lower()=='gram':
            new.append(i)
    return new
a = [
    "Telegram",
    "proGram",
    "Instagram",
    "WhatsApp",
    "YouTube",
    "Facebook",
    "TikTok",
    "Python",
    "JavaScript",
    "Visual Studio Code",
    "Discord",
    "Spotify",
    "Google Chrome",
    "Microsoft Word",
    "ChatGPT"
]
print(ends_with_gram(a))