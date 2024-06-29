print(70 // 20)

print((30 / 2))

print( 8 // 4 )

print(9/4)

def mohsin():
    print("Hellow World")
    def alpha():
        print("Mera Pakistan hai ye Piyara Pakistan hai")
    def bravo():
        print("Is pe dil qurban is pe jaan bhi qurbaan hai")
    alpha()
    bravo()
    


a = mohsin()
print(a)



# @new_decorator
def moshin():
    print("Mohsin is an engineerng Graduate! ")
a = mohsin()
print(a)

tuple(range(0,23,3))

def cubes(x):
    result = []
    for i in range(x):
        result.append(i**3)
    return result

for iq in cubes(10):
    print(set,{iq})

from collections import Counter

mylist = [1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9, 10 ,10 ,9,8,7,6,5,4,3,2,1]
Counter(mylist)

mylist = ['a' , 'v','a','v',23,23,10,10]

Counter(mylist)

Sentence = 'The quick brown fox jumps over a lazy dog.'

Counter(Sentence.lower().split())


