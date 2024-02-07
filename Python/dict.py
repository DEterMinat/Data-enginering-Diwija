customer = {"Name":"Diw","Address":"123","city":"Chon"}
Game ={"FPS":"PUBG","OPW":"genshin"}
user = dict(name="Diw",address="123 city",phone="00000")
user.update(hobbie ="Exercise")

print(customer["Name"])
print(Game["FPS"])
print(user)

for item in user.items():
    print(item)