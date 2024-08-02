# this is not useful but we have to do 
# it is similar to list comprehension but we use curly bracket here
# this set method give unordered print 
# this method give unique result means no duplicate data
square  = {i**2 for i in range(11)}
print(square)

names = ['merhaj' , 'sharat' , 'khan']
first = {name[0] for name in names}
print(first)