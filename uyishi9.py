import json 

with open("uy.json") as f:
    data=json.load(f)
    data = sorted(data, key=lambda x: x["score"], reverse=True)
    print("\txamma o`yinchilar")
    for i in data:
        print("  ",i)
    data.pop()
    print("\t>>>Top 3 o`yinchilar<<<")
    print(f"  {data[0]}\n  {data[1]}\n  {data[2]}")


        
        
        