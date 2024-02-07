customer={
    "user1":{
        "name":"Diw",
        "address":"123 city",
        "city":"bankok",
        "phone":"00000"       
        },
    "user2":{
        "name":"Wave",
        "address":"321 city",
        "city":"Siracha",
        "phone":"11111"
    },
    "user3":{
        "name":"Win",
        "address":"1321 city",
        "city":"Chonburi",
        "phone":"22222"
    }
}

print(customer["user1"])
for item in customer["user1"]:
    print(item)