#List and its default functions.
#List:-List is an ordered collection of elements enclosed with []
#List are mutuable.
#List allows modification in the previous constructed list.

#1->Modifying a list:-
l=['a','ayush',1,2,3,"sinha"]
for i in l:
  print(i)

#2->Appending a new element:-
l.append("msd")
print(l)
for i in l:
  print(i)

#3->Poping the last element.
l.pop()
print(l)
for i in l:
  print(i)

#4->Reversing elements of a list.
l.reverse()
print(l)

#5->Inserting element at a specified index.
l.insert(1,"msd")
print(l)





#Dictionary and its default function
#Dictionary is an unordered collection of key-values enclosed with {}.
#Dictionary is mutuable.
#Dictionary allows modification before the created dictionary.
d1={'Apple':50,'Mango':100,'Guava':200,'Banana':70}
print(d1)

#Extracting keys and values in created dictionaries.
d1.keys()
d1.values()

#Modifying a dictionary.
# 1-> Adding a new element:-
d1["Grapes"]=80
print(d1)

# 2-> Changing an existing element:-
d1["Apple"]=100
print(d1)

# 3-> Poping an element:-
d1.pop("Apple")
print(d1)

# 4-> Update one dictionary element with another one:-
d2={"Banana":80,"Papaya":50}
d1.update(d2)
print(d1)




#Set and its default function.
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets{}.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# 1->Access items
for i in thisset:
  print(i)

# 2-> Add items.
thisset.add('mango')
print(thisset)

# 3-> Update items.
thisset.update(['grapes','guava'])
print(thisset)

# 4-> Length of set.
a=len(thisset)
print(a)

# 5-> Remove items
thisset.remove('banana')
print(thisset)




#Tuple and explore default methods.
#It is an ordered collection of elements enclosed with()
#Tuples are immutable.

T=(1,True,3.14,5-7j)
print(T)
# 1-> Finding length of tuple
a=len(T)
print(a)

# 2-> Concatenating Tuples.
T1=(2,3,4)
b=T+T1
print(b)

# 3-> Repeating tuple elements.
c=T*3
print(c)

# 4-> Minimum value.
T2=(1,2,3,-1,-11,-10000)
d=min(T2)
print(d)

# 5-> Maximum value.
e=max(T2)
print(e)






#String literals in python are surrounded by either single quotation marks, or double quotation marks.
a="I love my india. I'm the big fan of MSD-07."
print(a)
#String Method

# 1->Slicing
b=a[2:8]
print(b)

# 2->Upper 
print(a.upper())

# 3->Length of string
print(len(a))

# 4-> Strip method
print(a.strip())

# 5->Lower
print(a.lower())

# 6->split
print(a.split(","))
