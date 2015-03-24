# converts the decimal to a string?
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# inserts the two string variables
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# %r displays raw data of the variable (mostly for debugging)
print "I said: %r." % x
# %s is used for content displayed to users
print "I also said: '%s'." % y

hilarious = False
# inserts a currently undefined string into the variable
joke_evaluation = "Isn't that joke so funny?! %r"

# defines the string placeholder as the other variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# concatenates two strings
print w + e