#!/usr/bin/env python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"] 
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print("my ", challenge[2][1]," ! The ", challenge[2][0]," do ",challenge[3],"!")
print("\n")
a=trial[2]
print("My ",a["goggles"]," ! The ", a["eyes"], " do ",trial[3],"!")
print("\n")
b=nightmare[0]
c=b["user"]
d=c["name"]
e=d["first"]

print("My ",e, "! The",b["kumquat"]," do ",b["d"],"!")
