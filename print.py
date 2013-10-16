opilane = "Timo"
if opilane == "Mariin":
   print "Eksam:5"
elif opilane == "Timo":
   print ":)"
else:
   print "Eksam:3"

x=0
while x<10:
   print "x=" + str(x)
   x = x + 1
print "valmis.x" + str(x)

masiiv = ["a","b","c"]
for element in masiiv:
   print element

masiiv = ["a","b","b","d","e"]
for element in masiiv:
   print element
   if element == "b":
      break
print "valmis"

x = 0.0
while x<0.8:
   print "x=" + str(x)
   x = x + 0.1
print "x=" + str(x)
