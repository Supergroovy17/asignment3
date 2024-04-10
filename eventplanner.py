
# tTsk 1
attendees = (int)(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2
print("Veggie Delight Caterers" if input("Would you like vegetarian options? (yes/no)") == "yes" else "Gourmet Meals Caterers")