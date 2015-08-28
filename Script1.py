#!/usr/bin/env python
import os
import random
import re
newpath = r'C:\Python' 
if not os.path.exists(newpath): os.mkdir(newpath)
for i in range(30):
    randname = str(random.randrange(10, 51))
    ext = ("txt", "dat", "src")
    randext = random.choice(ext)
    file = open("C:\Python\\" + randname + "." + randext, "w")
    file.close()

for i in range(30):
    randname = str(random.randrange(10, 51))
    ext = ("txt", "dat", "src")
    randext = random.choice(ext)
    if os.path.exists("C:\Python\\" + randname + "." + randext):
        file = open("C:\Python\\" + randname + "." + randext, "w")
        file.write("old")
        file.close()
    else:
        file = open("C:\Python\\" + randname + "." + randext, "w")
        file.write("new")
        file.close()
        
for filename in os.listdir("C:\Python"):
    result = re.search(r'[1]{1}[0-9]{1}.txt', filename)
    if result != None:
         src_name = re.sub(r"^(\d+)\.txt$", r"\1.src", filename)
         file = open("C:\Python\\" + filename,"r")
         s = file.readline()
         file.close()
         src_name = ("C:\Python\\" + src_name)
         os.remove("C:\Python\\" + filename)
         file = open(src_name, "w")
         file.write(s)
         file.close()

o = []
n = []
e = []
for filename in os.listdir("C:\Python"):
    file = open("C:\Python\\" + filename,"r")
    s = file.readline()
    file.close()   
    if s == "old":
        o.append(filename)
    elif s == "new":
        n.append(filename)
    else:
        e.append(filename)

files = {"old ": o, "new" : n, "" : e}
print files