class EmployeeHierarchy():
	
	def __init__(self, capacity=2):
		self.hierarchy_list = []
		self.employee_count = 0
#		self.capacity = capacity
#		self.search_list = [] #stores indexes of levels with slots for employees

	def add_employee_pair(self, employee_pair):
		names = employee_pair.split(' ')

		if self.employee_count == 0:
			self.hierarchy_list.append(names[0])
			self.hierarchy_list.append([names[1]])
			self.employee_count += 2
		
		else:
			for current_level, managers_list in enumerate(self.hierarchy_list):
				next_level = current_level + 1

				if current_level == 0:
					if managers_list == names[0]:
						self.hierarchy_list[next_level].append(names[1])
						self.employee_count += 1;
						break;
				else:
					for manager in managers_list:
						if names[0] in managers_list:
							
							if len(self.hierarchy_list)-1 < next_level:
								self.hierarchy_list.append([])
							
							self.hierarchy_list[next_level].append(names[1])
							self.employee_count += 1
							break;

	def print_hierarchy(self):
		print self.hierarchy_list[0]
		
		for employee_list in self.hierarchy_list[1:]:
			employees_str = ""
			
			for employee in employee_list:
				employees_str += employee + " "

			print employees_str
		



def read_input(employee_count, managers):

	levels = 0;

	while (managers.employee_count < employee_count):
		print managers.employee_count
		print employee_count
		print managers.hierarchy_list
		names = raw_input("Enter employee details <Employee name> <Employee name>")
		managers.add_employee_pair(names)


num_employers = input("Please enter the number of employees")

managers = EmployeeHierarchy()
read_input(num_employers, managers)

managers.print_hierarchy()

import pdb
pdb.set_trace()