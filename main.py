# The following 5 lines assign STRING VALUES to each variable.
title = "Prof."              # assigns the VALUE "Prof." to title
given_name = "Lucas"         # assigns the VALUE "Lucas" to given_name
middle_initial = "A."        # assigns the VALUE "A." to middle_initial
family_name = "Hernandez"    # assigns the VALUE "Hernandez" to family_name
credential = "M.Sc."         # assigns the VALUE "M.Sc." to credential

# The print statement below uses an EXPRESSION made of multiple string values joined by +
print(title + " " + given_name + " " + middle_initial + " " + family_name + ", " + credential)
# Each "+" is an IMPLICIT string concatenation
# ", " is a STRING VALUE used to format the comma and space

# Alternatively, using commas separates string values with IMPLICIT spaces
print(title, given_name, middle_initial, family_name, ",", credential)
# Python adds spaces automatically between items, causing a space before the comma in the output
