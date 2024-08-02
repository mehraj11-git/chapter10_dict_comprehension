# it is similar to the list but it contains key and values as a pair 
# in this exercise we will do the square of the every keys
# for ex: square = {1:1,2:4,3:9}

square = {num:num**2 for num in range(11)}
print(square)

# simple method 

sq ={0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
for i,j in sq.items():
    print({f"{i} : {j}"})

square1 = {f"square of {num} is" :num**2 for num in range(1,11)}
print(square1)

for i,k in square1.items():
    print({f"{i}:{k}"})
# with this method we print one by one 
# we use items() to print both key and value

# next ex:counting the character
string =  "merhaj khan"
word_count = {char:string.count(char) for char in string}
print(word_count)

# in this exercise
# firstly,we write the character and we have to count the string in that we have to write the charcter 
# and do for loop 
word_count = {char:string.count(char) for char in string}
for i,j in word_count.items():
     print({f"{i}:{j}"})

