l=[("Priyanshu","Singer"),("Pritam","Singer"),("Pritam","Dancer"),("Ronit","Singer"),("Ronit","Dancer"),("Harsh","Dancer"),("Ayush","Singer")]
singer={ i[0] for i in l if i[1]=="Singer"}
dancer={ i[0] for i in l if i[1]=="Dancer"}
print(f"artist={singer.union(dancer)}")
print(f"allrounders={singer.intersection(dancer)}")
print(f"onlydance={dancer-singer.intersection(dancer)}")
print(f"onlysing={singer-singer.intersection(dancer)}")
print(f"onlydanceorsing={(singer-singer.intersection(dancer)).union(dancer-singer.intersection(dancer))}")