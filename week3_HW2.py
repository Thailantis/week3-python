#Filter out all of the empty strings from the list below
#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
    
new_city_list = list(filter(lambda names: names.strip(), places))
print(new_city_list)



# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

authors = ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

authors.sort(key=lambda name: name.split()[-1].lower())
print(authors)
    

# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

temp_cities = [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

cel_to_far = list(map(lambda x : x * 1 , temp_cities))
print(cel_to_far)

# Write a recursion function to perform the fibonacci sequence up to the number passed in.
# Output for fib(5) => Iteration 0: 1 Iteration 1: 1 Iteration 2: 2 Iteration 3: 3 Iteration 4: 5 Iteration 5: 8

def fibonacci(num):
  if num <= 1:
    return num
  else:
    return fibonacci(num-1) + fibonacci(num-2)
  
  for i in range(6):
    if num + 1:
        print("fibonacci(1) = 1")
        return num
    else:
      print("Iteration {}: {}".append(i,fibonacci(i)))
    return num + fibonacci(num + 1)

print(fibonacci(5))
