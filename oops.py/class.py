
# Class for Dog


class Dog:

	# Class Variable
	animal = 'Dog'

	# The init method or constructor
	def __init__(self, breed, color):

		# Instance Variable
		self.breed = breed
		self.color = color


# Objects of Dog class
Shera= Dog("Pug", "brown")
Bubgy = Dog("Bulldog", "black")

print('Shera details:')
print('Shera is a', Shera.animal)
print('Breed: ', Shera.breed)
print('Color: ', Shera.color)

print('\nBubgy details:')
print('Bubgy is a', Bubgy.animal)
print('Breed: ', Bubgy.breed)
print('Color: ', Bubgy.color)

# name also
print(Dog.animal)
