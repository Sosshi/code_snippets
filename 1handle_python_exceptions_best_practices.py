# Not recommended
# This is because errors might hide inside the code
# This makes it is very difficult to know whether it is the
# expected type of errror which has occured or its a
# new type of error
try:
    8 + "8"
except:
    print("I run after any error has occured")


# recommended
# This is recommended as only the errors the user expects
# are handled, which makes it easy to identify bugs
# The error must be identified and not generalised
try:
    8 + "8"
except TypeError:
    print("I am the expected error ")