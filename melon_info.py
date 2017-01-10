"""
Prints out all the melons in our inventory
"""



from melons import melons  

def print_melon(melon_info):
    """Prints each melon name and corresponding attributes"""
    
    for melon, details in melon_info.items():
        print melon.upper()
        for detail, value in details.items():
            print "{}: {}".format(detail, value)
        print "==============================="

print_melon(melons)



