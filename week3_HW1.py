# Use python to read the file regex_test.txt and print the last name on each line using regular expressions and groups 
# (return None for names with no first and last name, or names that aren't properly capitalized)
# Hint: use with open() and readlines()
# """
# Expected Output
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None
# """

with open(regex_test.txt) as f:
  data = f.readlines()
  print(data[0])
  
pattern = re.compile("([A-Z][a-z]+), ([A-Z][a-z]+) ")

def president(person):
  president_names = ["Abraham Lincoln", "Andrew P Garfield", "Connor Milliken", "Jordan Alexander Williams"]
  
  for person in president:
    match = pattern.search(person)
    
  if match:
    print(president(person))
