# includes argv from system module
from sys import argv

# instantiates variable from argv
script, filename = argv

# calls open on the file name and instantiates a variable with the result
txt = open(filename)

# prints the filename
print "Here's your file %r:" % filename
# prints the result of open(filename)
print txt.read()
txt.close()

print "Type the filename again:"
# gets the filename as raw_input
file_again = raw_input("> ")
# opens that file and assigns it to the text_again variable
text_again = open(file_again)

# prints the result of open() called on text_again
print text_again.read()
text_again.close()
