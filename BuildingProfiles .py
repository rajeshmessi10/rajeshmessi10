# build_profile("Isaac", "Newton",  location="Kensington",
              #field=["physics", "math", "astronomy", "theology"] ) ➞ { "first_name": "Isaac", "last_name": "Newton", "location": "Kensington", "field": ["physics", "math", "astronomy", "theology"] }
#Create a function that takes multiple arguments, including the first and last name of a person. It should return a dictionary containing all the information which was given in an orderly manner.
def para(*args, **kwargs):
    d = {"first_name": args[0] , "second_name":  args[1]}
    d.update(kwargs)
    return d
print(para("Isaac", "Newton",  location="Kensington",
           field=["physics", "math", "astronomy", "theology"]))
print(para("Marie", "Curie",  location="Sancellemoz", field="chemistry",
           discovered="Radium, Polonium"))