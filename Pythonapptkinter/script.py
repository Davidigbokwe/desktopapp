#python classes and object oriented programming 
#corey schafer
#methods are functions associated with class


class Employee:
	def __init__(self,first, last, pay):
		self.first =first
		self.last =last
		self.pay =pay
		self.email = first[0] + '.'+ last +"@hackmanmfb.com"

	def fullname(self):
		return '{} {}'.format(self.first, self.last)
emp1 =Employee('david','igbokwe',50000)
emp2 = Employee('Emeka', 'Victor',60000)

#create a method with our class




print(emp2.fullname())