import random
n=random.randint(2,8)
print(n)

m=random.randrange(3,9)
print(m)

l=["apple","mango","banana"]
print(random.choice(l))

r=random.random()
print(r)


l1=[10,45,75,80]
random.shuffle(l1)
print(l1)



u=random.uniform(3,9)
print(u)