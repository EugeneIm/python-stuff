magicians = ['alice', 'david', 'carol']
for magician in magicians:
    print(magician)
    #print(magician.title())

print('this is our list of magicians performing tonight')

#slicing a list
agents = ['jett', 'sage', 'brim', 'sova', 'raze']
print(agents[0:3]) #this just prints to the third one starting from the index of 0 (jett)
    #'jett', 'sage', 'brim'
print(agents[1:3]) #start this list at the index of 1 (sage)
    #'sage', 'brim'
print(agents[:4]) #no first slice = python writing out the list from the beginning up to your slice
    #'jett', 'sage', 'brim', 'sova'
