# Write a Python functionthat accepts a hyphen-separated sequence of colorsas input and returnsthe colorsin a hyphen-separated sequence after sorting them alphabetically.Constraint:All the colors will be completely in either lower case or upper case.
# Sample input1:green-red-yellow-black-white
# Sample output1:black-green-red-white-yellow

# Sample input2:PINK-BLUE-TAN-PURPLE
# Sample output2:BLUE-PINK-PURPLE-TAN

def sort_colors(color):
    colors=[]
    colors=color.split('-')
    colors.sort()
    ans='-'
    ans=ans.join(colors)
    print(ans)

color="green-red-yellow-black-white"
sort_colors(color)