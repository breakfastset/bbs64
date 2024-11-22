print("{} {} {}".format("a", "b", "c"))     # a b c

print("{0} {1} {2}".format("a", "b", "c"))  # a b c
#                           0    1    2

# reorder the index
print("{2} {0} {1}".format("a", "b", "c"))  # c a b
#                           0    1    2

print("{0} {1} {1} {0}".format("A", "B"))      # A B B A
#                               0    1

print("{0} {2} {3} {1}".format("D", "O", "E", "R"))  # D E R O
#                               0    1    2    3
