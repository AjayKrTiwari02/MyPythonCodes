import pickle as pic

ex={1:"6",2:"3",3:"A"}                                         #dictionary

# p=open("Pickle@.txt","wb")              #path
# pic.dump(ex,p)
# p.close()

                                                            # wb:data write mode
                                                            # rb:data load mode

#DATA LOAD:
# f=open("Pickle@.txt","rb")
# a=pic.load(f)
# print(a)

                                            #or

# print(pic.load(f))

#The load()function takes a file object,reconstruct the objects from the pickled representation & return it.

