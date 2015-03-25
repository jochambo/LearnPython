# create a mapping of state to abbreviation
states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'New York': 'NY',
  'Michigan': 'MI'
}

# creates a basic set of states and some cities in them
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}


def seperator():
    print '-' * 10

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
seperator()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
seperator()
print "Michigan's abbreviation is: ", states["Michigan"]
print "Florida's abbreviation is: ", states["Florida"]

# do it by using the state then cities dict
seperator()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
seperator()
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
seperator()
for abbrev, city in cities.items():
    print "%s has %s." % (abbrev, city)

# now do both at the same time
seperator()
for state, abbrev in states.items():
    print "%s is abbreviated %s and has %s." % (state, abbrev, cities[abbrev])

# safely get an abbreviation by state that might not be there
seperator()
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state of 'TX' is: %s" % city
