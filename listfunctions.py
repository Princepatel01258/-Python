lucky_numbers = [4,7,9,8,34,43]
friends = ["Kevin" , "Karen" , "Jim", "Oscar" , "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed") #This Function Always Adds The Things On End Of the list
 #friends.index(1,"Kelly") #This Function Lets You Add Wherever you want has 2 parameters
friends.remove("Jim") #This Function Lets You To remove things From Lists 
#friends.clear()
friends.pop() #this can randomly remove one thing from list
#print(friends.index("Mike"))
lucky_numbers.sort() #This is Ascending Order
print(lucky_numbers)
lucky_numbers.reverse() #This Is Descending Order
print(lucky_numbers)
friends2 = friends.copy() #this copies the items in list
print(friends) 