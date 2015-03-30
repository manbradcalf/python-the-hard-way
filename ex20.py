from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline(),
    print "The byte position is %d" % f.tell()
    # http://stackoverflow.com/questions/20969536/learn-python-the-hard-way-ex20-how-does-this-function-work
    
current_file = open(input_file)

print "first let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line= current_line + 1
print_a_line(current_line, current_file)

