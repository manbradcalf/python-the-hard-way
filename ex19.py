# defines the cheese_and_crackers function and its arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# functions can take raw input as arguments
print "We can just give the function inputs directly:"
cheese_and_crackers(int(raw_input('How much cheese?\n')), int(raw_input('How many crackers?\n')))

# functions can take integers as arguments
print "We can just give the function numbers directly"
cheese_and_crackers(22,33)


# functions can also take variables as arguments
print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "we can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

