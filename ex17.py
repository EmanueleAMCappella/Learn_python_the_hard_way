from sys import argv
from os.path import exists

script, from_file, to_file= argv

print "Copying from %s to %s" %(from_file, to_file)

#fallo in una riga
#indata= open(from_file).read()
in_file=open(from_file)
indata=in_file.read()

print "The input file is %d bytes long" %len(indata)

print "Does the input file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort"
raw_input()

out_file= open (to_file, 'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()
#from_file.close() qui emerge il problema se voglio chiudere il file 

#problema con la versione di una riga scritta: l'oggetto e' una stringa e non ha l'attributo close
#http://stackoverflow.com/questions/12118609/python-str-object-has-no-attribute-close
#https://www.google.it/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=object%20of%20type%20%27file%27%20has%20no%20len

#why you need to close() https://mail.python.org/pipermail/tutor/2012-January/088030.html
#http://stackoverflow.com/questions/30092249/about-close-a-file-in-python
#leggi anche il suo commento sul libro