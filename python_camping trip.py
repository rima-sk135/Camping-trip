# hey, we're going on a camping trip!!!
# here's the stuff we'll need

camping_stuff = "tent, sleeping bags, water, raspberry pi, marshmallows,coffee, flash drive, ethernet cable, knife"

# PYTHON_LIST
camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "marshmallows","coffee", "flash drive", "ethernet cable", "knife"]
camp_site = ["Crystal Lake", 494, 89.3, True]

# adding things to a list
camping_list.append("toilet paper")
camping_list.extend(["bidet", "toilet paper"])
camping_list.insert(-1, "bidet")
print(camping_list)

# deleting things from a list
camping_list.remove("tent")
# camping_list.pop(0)
print(camping_list.pop(0))
print(camping_list)
