#The pickle module implements a fundamental,but powerful algorithm for serializing & de-serializing a python object structure.
#it is used for :-list ,touple ,Dictionarys,sets etc.
#Serialize-> storing data.
#De-Serialize->Readinhg..

# You can pickle object with the folowing data types;
# booleans
# intiger
# floats 
# Complex number 
# (normal & unicode )Strings,
# tuples
# lists 
# sets
# Dictionarys

# Pickle has two methods:
# dump()->This function is called to serialize an object hierarchy.
#load()->This fubction is called to de-serialize a data straem.


#Pickling data is done via the dump()function.it accept data & file object
#The dump() function then serialize the data & writes it to the file.
#The syntax : dump(obj,file)
