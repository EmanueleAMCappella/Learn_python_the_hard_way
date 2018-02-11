from sys import argv

script, user_name, age = argv

prompt= '>'

print "Hi %s, I'm the %s script" %(user_name, script)
print "I see that you are %r years old" %(age)
print "Do you confirm me your age? People underaged cannot play this game..."
years= raw_input (prompt)

print "Ok, that seems fine. Now I'd like to ask you a few questions"

print "Do you like me %s?" %user_name
likes= raw_input(prompt)

print "Where do you live %s?" % user_name
lives= raw_input(prompt)

print "What kind of computer do you have?"
computer= raw_input(prompt)

print """
Allright, so you your age is %r,
You said %r about liking me
You live in %r. Not sure where that is.
nd you have a %r computer. Nice.
""" % (years, likes, lives, computer)