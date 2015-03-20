name = 'Zed Shaw'
age = 35
height = 74.0 #inches
height_in_cm = height * 2.54
weight = 180.0 #lbs
weight_in_kg = weight * 0.453592
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %r centimeters tall" % height_in_cm
print "He's %r kilograms heavy" % weight_in_kg
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d and %d, I get %d" % (age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg)