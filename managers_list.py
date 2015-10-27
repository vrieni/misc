#we can implement this using a binary tree structure since
#it deals with heirarchical data, but I think using a manager
#class in a list would suffice to communicate the intent
#and it is also easier to read.

#A lot of edge cases have been ignored, considered that the
#input is assumed to be always correct

class Employee():

	def __init__(self, name=''):
		self.name = name
		self._first_emp = None
		self._second_emp = None

	def set_first_emp(self, employee):
		self._first_emp = employee

	def set_second_emp(self, employee):
		self._second_emp = employee

	def set_subordinate(self, employee):
		#check if full capacity
		if not self.get_first_emp():
			print 'setting subordinate 1'
			self.set_first_emp(employee)
		else:
			print 'setting subordinate 2'
			self.set_second_emp(employee)

	def get_first_emp(self):
		return self._first_emp

	def get_second_emp(self):
		return self._second_emp

	def is_full_capacity(self):
		return bool(self.get_first_emp() and self.get_second_emp())


class EmployeeHeirarchy():

	def __init__(self, top_manager = None):
		self.employee_count = 0
		self._top_manager = top_manager
		self.current_manager = top_manager
		
		if top_manager != None:
			self.employee_count += 1


	def set_top_manager(self, top_manager):
		self._top_manager = top_manager

	def add_employee_pair(self, employee_string):
		names = employee_detail.split(' ')
		if self.top_manager == None:
			pass

#	def get_employee(self, name):
#		if self.name == name:
#			return self
#		else:




	def print_heirarchy():
		pass


def read_input(employee_count):

	current_manager = None
	last_entry = None
	ctr = 0
	organization = EmployeeHeirarchy()

	while (ctr < employee_count):
		employee_detail = raw_input("Enter employee details <Employee name> <Employee name>")
		
		
		#temporary index for the manager
		#check if manager is full capacity
		if ctr == 0:
			employee_m = Employee(names[0])
			ctr += 1
			current_manager = employee_m
			current_manager.set_subordinate(Employee(names[1]))
			ctr += 1
			organization.set_top_manager(current_manager)
		else:
			#organization.add_employee_pair(employee_detail);
			if current_manager.name == names[0]:
				current_manager.set_subordinate(Employee(names[1]))
			else:
				if current_manager.get_first_emp() == names[0]:
					employee = Employee(names[0])
					e = current_manager.get_first_emp()
					e.set_subordinate(employee)
					employee.set_subordinate(Employee(name[1]))
				elif current_manager.get_second_emp() == names[0]:
					e = current_manager.get_second_emp()
					e.set_subordinate(Employee[1]);





num_employees = input("Please enter the number of employees")

employees = []
read_input(num_employees)

import pdb
pdb.set_trace()