# Note : A reference to objects is also deleted when the object goes out of reference or when the program ends. 
# Example 1 : Here is the simple example of destructor. By using del keyword we deleted the all references of 
# object ‘obj’, therefore destructor invoked automatically.

# Python program to illustrate destructor
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created.')

	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj
