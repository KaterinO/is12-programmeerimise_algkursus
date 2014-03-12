#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Switch:
	
	def __init__(self, state):
		self.state = state
		
	def on(self):
		self.state=True

	def off(self):
		self.state=False
				
	def state_get(self):
		return self.state
	
class And:
	
	def __init__(self):
		self.inputs = []	
	
	def input_add(self, x):
		self.inputs.append(x)
		
	def state_get(self):
		if len(self.inputs)== 0:
			return False
		for i in self.inputs:
			if i.state.get() == False:
			#if not i:
				return False
		return True
		
sw1 = Switch(True)
sw2 = Switch(True)
#print obj1.state_get()

obj2 = And()
obj2.input_add(sw1)
obj2.input_add(sw2)
#print obj2.state_get()

# and, inputs - massiiv
# Meetodid: input_add(x) ; state_get()
