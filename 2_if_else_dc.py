# in this exercise we do ,if key is odd the value will be odd else even 
odd_even ={i:('even' if i %2==0 else 'odd')for i in range(11)}
print(odd_even)

for i,k in odd_even.items():
    print({f"{i}:{k}"})