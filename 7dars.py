def sozlar_soni(a:str):
    new={}
    for i in a.split():
        if i not in new:
            new[i]=1
        else:
            new[i]+=1
    print(new)

# sozlar_soni("phyton phyton k phyton k")


# ========================================


def unikal(a:str):
    new=[]
    for i in a.lower():
        if i not in  new and i.isalpha():
            new.append(i)
    # return new
    for i in new:
        if '. ' in i:
            new.remove(i)
    return new

# print(unikal("phyton is great and phyton is fun.Learning Phyton is a great exprerience."))


# ======================================================


def birmarta(a:str):
    print(list(set(a.split())))


# birmarta("phyton is great and phyton is fun.Learning Phyton is a great exprerience.")



def winners(data: list[dict]):
    new={}
    for key,v in data:
        if key in new:
            new[key] += v
        else:
            new[key] = v
    print(new)

    max1=max(new,key=new.get)
    print(max1, new[max1])


# data = [
#     ("Ali", 50),
#     ("Vali", 70),
#     ("Ali", 30),
#     ("Aziza", 90),
#     ("Vali", 40)
# ]
# (winners(data))

def sanash(a:str):
    a=a.split()
    new={}
    for i in a:
        if i not in new:
            new[i]=1
        else:
            new[i]+=1
    return new
    # for i in new:
    #     if new[i] < 2:
    #         return new

# a=input("<<")
# natoja=sanash(a)
# for k,v in natoja.items():
#         if v < 2:    
#             print(natoja)
#             # break
#             print(v)
# print(set(natoja))