from colorama import Fore,init
init()

print(Fore.LIGHTGREEN_EX)

with open("uy.txt") as f:
    data=f.read().split("\n")

new={}

for i in data:
    key = i.split(",")[4]

    if key not in new:
        new[key] = 1
    else:
        new[key] += 1

print("Eng ko`p qatnashgan model <<< ",max(new,key=new.get)," >>>")

dct={}

for i in data:
    davlat=i.split(",")[-1]
    if davlat == "country":
        continue
    if davlat not in dct:
        dct[davlat]=1
    else:
        dct[davlat]+=1



print("Eng ko`p qatnashgan davlat <<< ",max(dct,key=dct.get)," >>>")
print("Eng kam qatnashgan davlat <<< ",min(dct,key=dct.get)," >>>")





