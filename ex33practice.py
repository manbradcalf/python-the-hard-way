numbers = []

def loopthing(n):
    i = 0
    while i < n:
        numbers.append(i)
        i += 1
        print numbers
        

n = int(raw_input("> "))      
print loopthing(n)

#print "The list is: "
#for num in numbers:
#	print num