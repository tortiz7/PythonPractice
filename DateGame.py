# Alright, here is my nested dictionary with the menu for KuraCafe! I've expanded on it from what was created with my group during class - each category has two food items now. I won't use the ingredients in the dating script, but i've left them in the dict for posterity.
# I've also made all the courses lowercase, so that I can use the the .casefold() method to make all the user inputs case insensitive. THe method renders the inputs in lower case, however, so for variables comparisons, the variable value must also be lowercase in the dict in order to make the lowercase input correct
KuraCafeMenu= {
  "Pastries":{
        "croissant":{"Price":3.00,"Ingredients":["Flour","Butter","Eggs"]},
        "cheese danish":{"Price":4.00,"Ingredients":["Sugar","Butter","Cream Cheese","Dough"]}
    },
  "Entrees": {
        "bacon egg & cheese":{"Price":7.50,"Ingredients":["Bagel","Cheese","Eggs","Bacon"]},
        "blueberry pancakes":{"Price":8.00,"Ingredeints":["Flour","Milk","Sugar","Blueberries"]}
    },
  "Desserts": {
        "cheesecake":{"Price":10.00,"Ingredients":["Crust","Cream cheese","Eggs","Strawberries"]},
        "apple pie":{"Price":6.50,"Ingredients":["Crust","Brown Sugar","Cinammon","Apples"]}
    },
  "Bevs": {
        "drip coffee":{"Price":3.00,"Ingredients":["Colombian Coffee Bean","Water"]},
        "matcha tea":{"Price":3.50,"Ingredients":["Hot Water", "Matcha", "Soy Milk"]}
    }
}

# Below, I created a function to quickly print the course categories, coruses in the categories, and corresponding prices for the courses, to server to the user as a menu for them to choose from
# I chose to create a function for this so I can easily call upon it later in the script, when the date is given the option to review the menu to choose there order
# So, calling dictionary values: the Cafe Menu consists of an outer dict, where the keys are the category of food (Entree, Pastries etc.) and the corresponding values are the courses witin those categories, and the details of those values are the corresponding prices. That is called via the KuraCafeMenu.items
# Then we have the inner dictionary, where the key are the names of the courses (cheesecake, blueberry pancakes etc) and then the items are the corresponding prices for the courses. this inner dict is called via the items.items
def Kura_Cafe_Menu():
    for category, courses in KuraCafeMenu.items():
        print(f"Course: {category}")
        for course, prices in courses.items():
            Price=prices["Price"]
            print(f"{course}: ${Price:.2f}")    #:.2f is our format specifer, where the .2 specifies our float will go to 2 decimal points, and the f is "fixed-point notation", designating we are formatting a float


# I've imported time here so I can use the sleep function to allow the user time to read the menu before having to make their choice
import time
# Here we will start a variable library via the input function, getting variables from the user for their name, their dates name, and their budget
UserName=input("Welcome to the Kura Cafe! What's your name friend?: ")
Date=input (f"And who is this lovely person with you, {UserName}?: ")
Budget=float(input("And how much we looking to spend today?: "))



# The script (waiter) then mirrors back all the information to make sure they have it correct 
print(f"Gotcha, so let me just write this all down. {UserName} is on a date with {Date} and doesn't want to spend more than ${Budget:.2f}. We can work with that!")
print("Alrighty, why don't you take a look at the menu!")

# Now we print the menu for the user to choose what they want to order
time.sleep(1)
Kura_Cafe_Menu()
time.sleep(1)

# Here we initialize 3 counters: TotalBill keeps track of the whole total amount of money all the orders cost throughout the date - this will incremeent by the price of the orders.
# OrdersMade keeps track of how many orders the User makes on the date. This increments by 1 everytime an order is made.
# OrdersMadeDate keeps tracks of how many orders the date makes, and also increments by 1 everytime an order is made
TotalBill=0.00
OrdersMade=0
OrdersMadeDate=0

# our order script is encapsulated in a while statement, where the script will continue to run until the Ordered variable is changed to True. This allows us to nest multiple if statements into the while loop
while True:
    Order=input("What would you like from the menu?: ").casefold()  # here's our first .casefold()! This will ensure the input is case sensitive, and the script won't break due to capitilization issues
    Ordered=False   # we set the Ordered variable to false to initate the while loop. 

    for course, items in KuraCafeMenu.items():
        if Order in items:    # This if statement initates as long as the order inputted by the user exists as a value within our Menu dictionary (as an course, hence why it's an "item")
            Price=items[Order]["Price"]    # this calls the correspondin price for the Order (which we've already checks exists as an item in our Menu dict) and sets it the variable "Price"
            if Budget>=Price:     # This if statement initiates only if the price of the item ordered is less than the remaining budget
                Budget-=Price     # This subtracts the Price of the ordered item from the remaining budget
                TotalBill+=Price  # This increments our first counter, the ToTalBill, by the amount the ordered item costs
                OrdersMade+=1     # This increments our second counter, OrdersMade, by 1 - so everytme an order is made
                print(f"{UserName}, you ordered {Order}. A delicious choice! That costs ${Price:.2f}. You have ${Budget:.2f} remaining from what you told me you'd like to spend today.")
                Ordered=True      # The Ordered status is changed to true, because the order was successfully placed. This fulfills the While loop
                break             # Break ends the while loop without having to iterate through any of the other steps within
            else:                 # This else statement is triggered if the price of the order is greater than the remaining budget. VSCode is a godsend with the lines clearly showning what if statement you are working in!
                 print(f"Oh hun, this is embarrassing, but you don't have enough money left for {Order}. You have ${Budget:.2f} left to spend. Why don't you choose something else?")
                 Ordered=True     # Ordered=True here to maintain the logic of the while loop - if it was false, the below print statement would also print to the terminal when there is not enough money in the budget
                 break
    if not Ordered:               # Python if statements have a "Not" operator that checks if the reverse of the condition is true. In this case, the script checks if Ordere still = False. Since we already have an if statement that checks if the price of the ordered item is greater than the budget, thsi statement serves to check if the ordered item exists on the menu.
        print(f"Sorry hun, we don't have {Order} on the menu right now. Why don't you look again and see if there's something else you like?")
        continue                  # THe continue starts the while loop over again, allowing the user to input a valid menu item as their order.

    if Budget<=2.5:                 # If the remaining budget is less than or equal to 2.5, the script will break. There are multipe other if statements checking if the budget is <=0 throughout the remainder of the script, so if Budget<=2.5 here, you are taken straight to the final bill function. 2.5 is used here instead of 0 because every item on the menu is 3 or greater - this makes it so the user doesn't have to iterate through the script if they don't have enough money for anything on the menu
        print(f"Looks like y'all spent all the money you wanted to today! Let me go get you the check.")
        break
    else:                         # If Budget is greater than 2.5, the User is given the option to order something else on the menu
        OrderAgain=input(f"I'll get your order to the kitchen {UserName}. Do you want anything else before I go? (Yes/No): ")
        if OrderAgain.casefold()=='no':
            break

if Budget>2.5:                    # The Date only gets the option to look at the menu if there is enough money to spend on an item
    DateMenu=input(f"Would you like to see the menu, {Date}? (Yes/No): ")
    if DateMenu.casefold()=='yes':
        time.sleep(1)
        Kura_Cafe_Menu()

if Budget>2.5:                     # Again, the Date can only order if there is enough money in the Budget to do so. The rest of this while loop is identical to the first, apart from the OrdersMadeDate variable being specific to the Date
    while True:
        Order=input(f"What would you like from the menu, {Date}?: ").casefold()
        Ordered=False

        for course, items in KuraCafeMenu.items():
            if Order in items:
                Price=items[Order]["Price"]
                if Budget>=Price:
                    Budget-=Price
                    TotalBill+=Price
                    OrdersMadeDate+=1
                    print(f"{Date}, you ordered {Order}. A delicious choice. That costs ${Price:.2f}. You have ${Budget:.2f} remaining from what you told me you'd like to spend today.")
                    Ordered=True
                    break
                else:
                    print(f"Oh hun, this is embarrassing, but you don't have enough money left for {Order}. Your remaining budget is ${Budget:.2f}. Why don't you choose something else?")
                    Ordered=True
                    break
        if not Ordered:
                    print(f"Sorry hun, we don't have {Order} on the menu right now. Why don't you look again and see if there's something else you like?")
                    continue
        if Budget>2:
            OrderAgain=input(f"I'll get your order to the kitchen {Date}. Do you want anything else before I go? (Yes/No): ")
            if OrderAgain.casefold() == 'no':
                break
        else:
            break

print("Alrighty lovebirds! here's the final bill:")
print(f"${TotalBill:.2f}")                         # The FinalBill is the accumulated prices incremented in the TotalBill counter, printed in $USD

PayBill=input(f"And who will be paying today?({UserName}, {Date}, split): ").casefold()     # The PayBill variable will store one of the 3 choices to use for the formula that will decide if there will be a second date

# Different print statements will print to the terminal depending on who is chosen. The last is my favorite - if none of the 3 given choices are selected, the "waiter" will run after the couple for their money! Wonder if you get a second date for dine and dashing...
if PayBill==UserName.casefold():
    print(f"I'll take your card then {UserName}!")
elif PayBill==Date.casefold():
    print(f"I'll take your card then {Date}!")
elif PayBill=="split".casefold():
    print("I'll take both of your cards then!")
else:
    print("Y'all better come back here with my money!")

# The final formula! I created a formula to decide if there will be a second date, using the remaining Budget, both OrdersMade counters and who paid the bill. The deciding factors for if the User gets a second date are arbitrary and fickle, but so is the nature of love! It's pretty difficult to get a second date, but such is life....
# I didn't really need to define a formula for the SecondDate, mind you - it doesn't get used anywhere else in the script. Just wanted to flex my def muscles. 
def SecondDate():
    if Budget<=8 and OrdersMade<=3 and PayBill==UserName.casefold():
        print(f"{Date} thinks you're a big spender and wants to go on a second date with you!")
    elif Budget<=5 and OrdersMade<=OrdersMadeDate and PayBill=="split".casefold():
        print(f"{Date} feels respected by your decision to share the financial burden with them, and asks you on another date!")
    elif OrdersMade>OrdersMadeDate and PayBill=="split".casefold():
        print(f"{Date} does not want to pay money for the privilege of watching you feast, and you never heard from {Date} again :( ")
    elif OrdersMade>=3:
        print(f"{Date} feels like you two could not connect because your mouth was full the whole date, and you never heard from {Date} again :(")
    else:
        print(f"{Date} is mortified you turned out to be a deviant criminal, and you never heard from {Date} again :( ")

SecondDate()
# This must be the longest script I've written yet! Hope you enjoyed playing the DateGame!