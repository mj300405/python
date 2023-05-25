import random

x=random.randrange(1,10)
print(x)
print(type(x))

txt="""Test działania mojego pytona
w sumie całekim fajny język ale trzeba się nauczyć składni.
Jest śmiesnzie be średników ale trudno"""

x="test"

if x in txt:
    print(x," jest w txt!")
else:
    print(x,"nie ma w tekscie")

y="działania mojego pytona"
if y not in txt:
    txt=txt+y
else: 
    print("\"",y,"\" -> jest już w tekście")

txt=txt.replace("fajny", "zajebisty")
print(txt)

fruits = ["apple", "banana", "orange","pear"]

for x in fruits:
    print(x)


fruits.append("pear")

for i in range(len(fruits)):
    print(fruits[i])

[print(x) for x in fruits]

newlist=[x for x in fruits if "a" in x]

newerList = [x if x!="pear" else "papaya" for x in fruits]
for x in newerList:
    print(x)

for x in fruits:
    print(x + " smoothie")

secondFruits=("apple", "banana", "orange", "kiwi")

(red, yellow, orange, green)=secondFruits

for x in secondFruits:
    print(x)

for x in secondFruits:
    print(x if "a" in x else "papaya")

i=0
while i < len(secondFruits):
    print(secondFruits[i])
    i+=1

tuple1 = (1,2,3)
tuple2 = ("a","b","c")

tuple3=tuple1+tuple2
tuple4=tuple1*2
print(tuple3)
print(tuple4)

set1={2,1,3,7}
print(set1)

set2=set(tuple3)
print(set2)

print(2 in set2)

set2.add("your mama")
print(set2)

fruits={"apple", "banana", "cherry"}
tropical={"pineapple", "mango", "papaya"}

fruits.update(tropical)
print(fruits)

fruits.remove("pineapple")
print(fruits);

x = fruits.pop()
print(x);

fruits.clear()
print(fruits)

set11={"apple", "samsung", "xiaomi"};
set12={"apple", "orange", "banana"};

set13=set11.symmetric_difference(set12)
print(set13)

set14=set11.intersection(set12)
print(set14);

car = {
    "brand": "Toyota",
    "model": "Aygo",
    "year": 2021
}

print(car.get("model"))
car["color"] ="white"
print(car)


print(car.values());

car.update({"model": "Yaris"})
print(car)
