#!/usr/bin/env python
# -*- coding: utf-8 -*-

Kontaktid = {}

Kontaktid_maxID = 1

class Kontakt:
	
	def __init__(self):
		self.id = 0
		
	def save(self):
		global Kontaktid_maxID
		global Kontaktid
		if self.id = 0:
			self.id = Kontaktid_maxID
			Kontaktid_maxID = Kontaktid_maxID + 1
		voti = self.id
		vaartus = {"number": self.nr, "omanik": self.omanik}
		Kontaktid[voti] = vaartus
		
	def id_get(self):
		return self.id
		
	def number_get(self):
		return self.nr
	
	def omanik_get(self):
		return self.omanik
		
	def number_set(self, number):
		self.nr = number_class
		
	def omanik_set(self, omanik):
		self.omanik = omanik
		
		

class Inimene:
	
	#def __init__(self):
		#self.id = "1"
		#self.nimi = raw_input("Inimese nimi: ")
		
	def id_get(self):
		return self.id
		
	def nimi_get(self):
		return self.nimi
		
	def nimi_set(self, nimi):
		self.nimi = nimi

		
obj1 = Kontakt()
obj1.number_set("5")
obj1.omanik_set(3)

obj1.save()

obj2 = Kontakt()
obj2.number_set("7")
obj2.omanik_set(5)

obj2.save()

print Kontaktid

#obj2 = Inimene()

#print "ID" + obj2.id_get() + ": " + "Inimesele nimega " + obj2.name_get() + " " + "vastab number " +  obj1.number_get()

#print obj1.id_get()
#print obj2.id_get()

#print obj1.omanik_get()

