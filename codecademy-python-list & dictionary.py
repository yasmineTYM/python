zoo_animals = ["pangolin", "cassowary", "sloth", "giraff"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]
  
  #-------------------------------------------------------------------
  numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1]+numbers[3]
#-------------------------------------------------------------------
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3]="cat"
#-------------------------------------------------------------------
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("ysl")
suitcase.append("chanel")
suitcase.append("dior")


list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase
#-------------------------------------------------------------------
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle =suitcase[2:4]           # Third and fourth items (index two and three)
last   =  suitcase[4:6]             # The last two items (index four and five)
#-------------------------------------------------------------------
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]           # The fourth through sixth characters
frog =    animals[6:]           # From the seventh character to the end
#-------------------------------------------------------------------
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")


print animals # Observe what prints after the insert operation
#-------------------------------------------------------------------
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code her
    print 2*number

start_list = [5, 3, 1, 2, 4]
square_list = []
#-------------------------------------------------------------------
# Your code here!
for number in start_list:
    square_list.append(number**2)
    square_list.sort()
print square_list

#-------------------------------------------------------------------
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']

#-------------------------------------------------------------------

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['aaa']=15
menu['bbb']=34
menu['ccc']=34



print "There are " + str(len(menu)) + " items on the menu."
print menu

#-------------------------------------------------------------------

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin']='fdsafdas'


print zoo_animals
#-------------------------------------------------------------------
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')
#-------------------------------------------------------------------
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here

inventory['pocket']=['seashell', 'strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=550

