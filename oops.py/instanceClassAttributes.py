class Employee:
    compony = "google"
    salary = 100
    
    
harry = Employee()   
radha = Employee()

# creating instance Attribute salary for both the objects    
# harry.salary = 400
# radha.salary = 500
harry.salary = 598
print (harry.salary)
print (radha.salary)

# below lines throws an error as address is not present in the instance/class
 # print (harry.adsress)
