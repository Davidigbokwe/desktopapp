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

class Developer(Employee):
	raise_amount = 1.10

	def __init__(self,first, last, pay, pro_lang):
		super().__init__(first,last, pay)
		self.pro_lang =pro_lang


class Manager(Employee):
	def __init__(self,first, last, pay, employees = None):
		super().__init__(first,last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emps(self):
		for emp in self.employees:
			print('--->',emp.fullname())
			

dev1 = Developer('David','Igbokwe', 555550000, 'python')
dev2 = Developer('cory','Idgys', 50000, 'java')

mgr_1 = Manager('Sue','Smith', 90000, [dev1])
print(mgr_1.email)
mgr_1.add_emp(dev2)
mgr_1.remove_emp(dev1)
mgr_1.print_emps()








#print(dev1.email)
#print(dev2.pro_lang)

	