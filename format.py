from zones import tabs

# combine zips
'''
Upper Manhattan + Bronx = light green 
Westchester County = light blue 
Staten Island = light orange 
NJ = light yellow
CT = light purple
'''

green = tabs["man"]["upper manhattan"] + tabs["bronx"]["bronx"]
blue = []
for zones in tabs["wc"].values():
    blue += zones
orange = tabs["si"]["SI"]
yellow = tabs["nj"]["nj"]
purple = tabs["ct"]["ct"]

code_lists = [green, blue, orange, yellow, purple]
color_list = ["green", "blue", "orange", "yellow", "purple"]

total_len = 0
for color in code_lists:
    total_len += len(color)
print(total_len)

# print(green)
# print(blue)
# print(orange)
# print(yellow)
# print(purple)

# for index, code in enumerate(code_list):
#     if index == len(code_list)-1:
#         zip_string += "^{code}$".format(code=code)
#     else:
#         zip_string += "^{code}$|".format(code=code)

for color_i, color in enumerate(code_lists):
    #print("{region}\n".format(region=color))
    print("{color}\n".format(color=color_list[color_i]))
    zip_string = ""
    for index, code in enumerate(color):
        if index == len(color)-1:
            zip_string += "{code}".format(code=code)
        else:
            zip_string += "{code}|".format(code=code)
    final = '=REGEXMATCH(D2:D1181, "' + zip_string + '")'
    print("{final}\n".format(final=final))





