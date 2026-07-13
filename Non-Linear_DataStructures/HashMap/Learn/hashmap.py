fruit = {
    "apple": 10,
    "banana": 20,
    "orange": 8
}

number = {
    1: True
}

#### Add new data
fruit["watermelon"] = 100
print(fruit["watermelon"])

#### remove data
del fruit["watermelon"]

### check data
if "apple" in fruit:
    print(True)