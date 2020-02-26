class Argument:
	'''
	Attributes:
	arg_id
	Premise 
	Conclusion
	Methods:
	edit_premise()
	add_premise()
	set_conclusion()
	display_arg()
	'''
	premises = []
	conclusion = ''
	
	def __init__(self):
		pass

	def add_premise(self, p):
		self.premises.append(p)

	def set_conclusion(self, c):
		self.conclusion = c

	def edit_premise(self, index, p):
		self.premises[index] = p

	def display_arg(self):
		pass




### Testing ###
arg1 = Argument()

arg1.set_conclusion('Water is Blue')
print(arg1.conclusion)