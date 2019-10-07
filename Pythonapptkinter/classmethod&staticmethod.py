class Employee:
	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self,first, last, pay):
		self.first =first
		self.last =last
		self.pay =pay
		self.email = first[0] + '.'+ last +"@hackmanmfb.com"

		Employee.num_of_emps +=1
#create a method with our class

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay* self.raise_amount)


	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amount =amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)


	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:
			return False
		return True



emp1 =Employee('david','igbokwe',50000)
emp2 = Employee('Emeka', 'Victor',60000)

empstr1  ='John-doe-70000'
empstr2 = 'steve-smith-773738'
empstr3 = 'jane-doe-89999'

new_emp_1 = Employee.from_string(empstr1)

import datetime
my_date = datetime.date(2016,7,19)

print (Employee.is_workday(my_date))



print(new_emp_1.email)
print(new_emp_1.pay)


#Employee.set_raise_amt(1.05)

#print(Employee.raise_amount)
#print(emp1.raise_amount)
#print(emp2.raise_amount)

# instance variable allows you edit instances ina class .