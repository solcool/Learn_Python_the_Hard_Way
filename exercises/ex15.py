from sys import argv

script , filename = argv

txt = open(filename)

print "Here's your file name : %r" % filename

print "And this is the text in it:"

print txt.read()

print "Type the filename again:"

filename = raw_input(">")

print "And this is the text in the file:"

txt = open(filename)

print txt.read()

txt.close()
