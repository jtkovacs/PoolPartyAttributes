# coding: utf-8
import json
import sys


try:
    # File & script must be colocated 
    file_in = sys.argv[1]
    #file_in = "ppatt_in.rj"
except:
    print("Please type a valid command, e.g: python3 ppatt.py filename.rj")


# Read JSON into dict of dicts of lists of dicts (I think)
raw_json = json.load(open(file_in, "r"))


attribute_names = list()
for row in raw_json.values():
    object_type = row["http://www.w3.org/1999/02/22-rdf-syntax-ns#type"]
    
    # Extract attributes, drop classes and relations
    if object_type[0]["value"] == "http://schema.semantic-web.at/ppt/AttributeProperty":
    
        # Extract attribute names
        attribute_names.append(row["http://www.w3.org/2000/01/rdf-schema#label"][0]["value"]+"\n")

        
# Sort attributes (insensitive to case)
attribute_names.sort(key=lambda v: v.lower())


# Write text file
file_out = open("ppatt_out.txt", "w")
file_out.write("{} attributes were extracted\n\n\n".format(len(attribute_names)))
for a in attribute_names:
    file_out.write(a)
