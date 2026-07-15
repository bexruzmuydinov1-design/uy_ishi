# masala 1====================================================


# def oyin(odam1:list,odam2:list):
#     tanga1=3
#     tanga2=3
#     if 'share' in odam1 and 'share' in odam2:
#         tanga1+=2
#         tanga2+=2
#     elif 'steal' in odam1 and 'share' in odam2:
#         tanga1+=3
#         tanga2-=1
#     elif 'share' in odam1 and 'steal' in odam2:
#         tanga1-=1
#         tanga2+=3
#     elif 'steal' in odam1 and 'steal' in odam2:
#         tanga1+=0
#         tanga2+=0
#     return tanga1,tanga2


# l1=input("L1; ")
# l2=input("L2; ")
# print(list(oyin(l1,l2)))


# ==============================masala 2


# def qimmat(son, products):
#     products = sorted(products, key=lambda x: x["price"], reverse=True)
#     return products[:son]
    
# a=int(input("neshta eng qimmat tovar chiqsin; "))
# b=[
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]
# print(qimmat(a,b))


# =================masaala 3


def masala3(a, b):
    count = 0
    result = [str(a)]
    while a > b:
        a = a / 2
        result.append(str(a))

        if a > b:
            count += 1

    print(count,"marta bo`lindi")
    return (" -> ".join(result))
 
A=int(input("A; "))
B=int(input("B; "))

print(masala3(A, float(B)))


# THE END)

