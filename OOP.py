class Mohsin():
    def __init__(self , name , age , gender , history ):
        self.name     = name
        self.age      = age
        self.gender   = gender
        self.history  = history
myclass = Mohsin( name = 'mOHSIN' , age = 21 , gender = 'Male' , history = 'Okara' )
print( myclass.name )
print( myclass.age )
print( myclass.gender )


# Classs Attributes and Methods(A function defined inside any class)
# What is difference between function and Method.

class Dog():
    alpha = 'Bravo'
    def __init__(self , name , age ):
        self.name = name
        self.age  = age
    def bark( self , number ):
        print('The quick brown fox jumps over a lazy dog.!')
        print('my name is {} and number is {}'.format( self.name , number))
        
mydog = Dog( 'Mohsin' , 21 )

print( mydog.name )
print( mydog.age )
# Attribute calling when we put  "mydog.bark" without "()" It means we are calling an attribute.
print( mydog.bark )
# Method   calling ( Whenever we call method we need to put " mydog.bark() " )
print( mydog.bark(12) )


# Write a class too calculate area of circle.

class Circle():
    pi = 3.14
    # Function for class object Attribute
    def __init__(self , radius = 1 ):
        self.radius = radius
    # Function for Methods
    def get_circumference(self):
        return self.pi * self.radius ** 2
area = Circle()
print(area.pi)
print(area.radius)
area = Circle(23)
print(area.radius)

print(area.get_circumference)

print( area.get_circumference() )
print( f' The area is {area.get_circumference()} sqare units' )

# Anotyher Approach for same
class Circle():
    pi = 3.14
    # Function for class object Attribute
    def __init__(self , radius  ):
        self.radius = radius
        self.area = self.radius ** 2 * Circle.pi
    # Function for Methods
    def get_circumference(self):
        return self.pi * self.radius ** 2
circle_area = Circle(20)
area = Circle(20)
print( area.pi )
print( area.radius )
print( area.area )

# Inheritance Examples(Way to form new classes using classes  already  been  defined)
# Reuse code and reduce complexity of code
class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print('I am an animal.')
    def eat(self):
        print(" Animal eating.")
main_class = Animal()
print(main_class)

# Child Class

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created.')
    # Redefining
    def who_am_i(self):
        print('I am a dog. ')
    def eat(self):
        print('Dog is eating.')
    # a new method
    def bark(self):
        print(' Dog is barking!  ') 
        

mydog = Dog()
print(mydog)
print(mydog.bark())
print(mydog.who_am_i())
print(mydog.eat())

# Ploymorphism

class Cat():
    def __init__(self , name ):
        self.name = name
    def speak(self):
        return self.name + " speaks Meaaoo'n   "

class Dog():
  
    def __init__(self, name ):
        self.name = name
    def speak(self):
        return self.name + "  speaks Vaao00'f   "

poly = Cat('Billi')
print(poly.speak())
morphism = Dog('Kutta')
print(morphism.speak())

# Implementing Poymorphism using for loop
for i in [ poly , morphism ]:
    print(type(i))
    print(type(i.speak()))
    
# Implementing Poymorphism using for Functions.
def pet_speak( i ):
    print(i.speak())
a = pet_speak( poly ) 
b = pet_speak( morphism )
print( a , b )

# Another Polymorphism Approach
class Animal():
    def  __init__( self , name ):
        self.name  = name
    def speak():
        raise NotImplementedError("Subclass must implement this abstract method.")
    
class Dog(Animal):
    def speak(self,name):
        return self.name + " says Wooo'f "
    
class Cat(Animal):
    def speak(self,name):
        return self.name + " says Meaaooo'n "
    
mycat = Cat('  Billy:  ')
mydog = Dog('  Kutta:  ')

        
print(mycat.speak('Waao'))

print(mydog.speak('Meao'))

# Special Magic Dunder Methods

class Book():
    def __init__( self , name , author , pages ):
        self.name = name 
        self.author = author
        self.pages = pages
    def __str__(self):
        return f' The book {self.name} by author {self.author} has {self.pages} pages. '
    def __del__(self):
        print('Book has been Deleted')
        
    
    
mybook = Book('AI Superpwers' , 'Kai-Fu-Lee' , 300 )
print(mybook)

# del mybook
# print(mybook)

    