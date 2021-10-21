file = open("/Users/Christian Ezeoba/Desktop/new/mbox-shorts.txt","r")
for lines in file:
    lines = lines.rstrip()
    print(lines)
    #opens up the file and prints out its content to be seenm
for lines in file:
    lines = lines.rstrip()
    lines = lines.split( )
    if lines == '' :
        continue
    if len(lines) < 1:
        continue
        #a one line section of this file would most likely not feature an email address
    if lines[0] != 'Received:':
        #this line does not contain an email address. It does not begin with a pointing reference
        continue
    if lines[0] == 'Received':
        print('THIS LINE HAS AN EMAIL ADDRESS--------:',lines)
    words = lines.split()
    
    if words[0] != 'From:' :
        #this will be supposed as a line without an reference email address
        continue
    if len(words) > 0 and words[0] == 'From:':
        print(words[2])
        
number = 0
for lines in file:
    lines = lines.rstrip()
    lines = lines.split()
    for i in lines:
        number = number + 1
    print (number)
print (number)
count = 0
for lines in file:
    count = count + 1
    print (count)
print ('--------------the end')


