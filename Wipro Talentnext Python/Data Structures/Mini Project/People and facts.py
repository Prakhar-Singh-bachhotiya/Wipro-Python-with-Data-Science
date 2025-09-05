# Create a dictionary that contains a list of people and one interesting fact about each of them.Display each person and his or herinteresting fact to the screen. Next, change a fact about one ofthe people. Also add an additional person and corresponding fact. Display the new list of peopleand facts. Run the program multiple times and notice if the order changes.Sample output:Jeff: Is afraid of Dogs.David: Plays the piano.Jason: Can fly anairplane.Jeff: Is afraid of heights.David: Plays the piano.Jason: Can fly an airplane.Jill: Can hula dance


people={"Jeff": "Is afraid of Dogs.",
        "David": "Plays the piano.",
        "Jason": "Can fly anairplane."}
for key,value in people.items():
    print(key," : ",value)

name=input("Enter a Name : ")
info=input("Enter Info : ")

people[name]=info

for key,value in people.items():
    print(key," : ",value)

