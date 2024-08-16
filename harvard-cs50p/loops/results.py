results = ["Mario","Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser","Donkey Kong Jr."]) #lista dentro da lista
results.remove(["Bowser","Donkey Kong Jr."])
results.extend(["Bowser","Donkey Kong Jr."]) #estende a lista (bom para não usar append)

results.remove("Bowser")
results.insert(0,"Bowser")#index e valor
results.reverse()
print(results)