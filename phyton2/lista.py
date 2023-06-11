comid=["combo", "sandwich"]
comid.append("gaseosa")
comid.extend(["malteada", "perro caliente"])
print(comid)
print(len(comid))
for i, e in enumerate(comid):
    print (i,e)
comid.insert(2, "Empanada")
for i, e in enumerate(comid):
    print(i,e)
