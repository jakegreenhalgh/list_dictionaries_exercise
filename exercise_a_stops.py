from ast import Index


stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverly")
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops = ["Glasgow Queen Street", "Croy", "Cumbernauld", "Falkirk High", "Polmont", "Linlithgow", "Livingston", "Haymarket"]
#4. Print out the index position of "Linlithgow"
print(stops[5])
#5. Remove "Livingston" from the list using its name

#6. Delete "Cumbernauld" from the list by index
stops.pop(1)
#7. Print the number of stops there are in the list
print(len(stops))
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)
