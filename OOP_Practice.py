class Line:
    def __init__(self , coor1 , coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1 , y1 = self.coor1 
        x2 , y2 = self.coor2
        return ((x2-x1)**2 + (y2 - y1)**2)*0.5
    def slope(self):
        x1 , y1 = self.coor1
        x2 , y2 = self.coor2
        return (y2 - y1) / (x2 - x1)
coor1 = ( 3 , 2)
coor2 = (39 , 43)
result = Line( coor1 , coor2 )
print(result)

a = result.distance()
print(a)
b = result.slope()
print(b)

# Example 2: Write a class to define Cylinder
class Cylinder:
    def __init__(self , height = 1 , radius = 1 ):
        self.radius = radius 
        self.height = height
    def volume(self):
        return self.height * 3.14 * ( self.radius ) ** 2
    def surface_area(self):
        top = 3.14 * ( self.radius **2 )
        return ( 2* top ) + ( 2 * 3.14 *self.radius * self.height )

mycyl =   Cylinder( 2 ,3)   
a = mycyl.volume() 
print( a )
b = mycyl.surface_area()
print(b)


# Test classes
class Account:
    def __init__( self , owner , balance = 0 ):
        self.owner = owner
        self.balance = balance
    def deoposit(self , dep_amt):
        self.balance = self.balance + dep_amt
        print(f' Added { dep_amt } to the balance.')
    def withdrawl( self , wd_amt ):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawl Accepted")
        else:
            print(  "Sorry not enough Funds!" )
    def __str__(self): 
         return f'Owner: {self.owner} \n Balanace: {self.balance}'
            
# Checking Result
a = Account( 'Sam' , 4000)
print(a)

print(a.withdrawl(40000))

print(a.withdrawl(4))
