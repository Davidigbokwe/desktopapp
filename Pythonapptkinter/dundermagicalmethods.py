class Employee:
	raise_amount = 1.04

	def __init__(self,first, last, pay):
		self.first =first
		self.last =last
		self.pay =pay
		self.email = first[0] + '.'+ last +"@hackmanmfb.com"

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay* self.raise_amount)

	def __repr__(self):
		return "Employee({},{},{})".format(self.first.self.last,self.pay)

	def __str__(self):
		return'{} - {}'.format(self.fullname(),self.email())

	def__Len__(self):
	return len(self, fullname())

emp1 = Employee('david', 'Igbokwe')
emp2 = Employee('dddd', 'Igbsssokwe')
		
print(emp1)