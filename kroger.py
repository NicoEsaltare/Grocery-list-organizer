import json

kroger_dict = {"bagels": 1,
               "lunch meat": 1,
               "veggies": 1,
               "fruit": 1,
               "romaine": 1,
               "yum yum": 2,
               "smoked salmon": 3,
               "tortillas": 3,
               "ramen": 3,
               "baking mix": 4,
               "coffee": 5,
               "cereal": 5,
               "bars": 6,
               "chips": 7,
               "chocolate": 7,
               "toilet paper": 8,
               "laundry": 9,
               "cat stuff": 11,
               "tooth paste": 13,
               "tampons": 13,
               "coconut water": 14,
               "bacon": 15,
               "frozen veggies": 17,
               "oat milk": 17,
               "frozen fruit": 18,
               "pizza": 18,
               "coconut creamer": 19,
               "ice cream": 19,
               "yogurt": 19,
               "medicine": 20,
               "body soaps": 24,
               }


current_choice = None
grocery_items = {}      # create an empty dictionary

while current_choice != "quit":
    if current_choice in kroger_dict:
        chosen_item = kroger_dict[current_choice]
        if current_choice in grocery_items:
            # It's already in, so remove it.
            print(f"Removing Item on Isle:{chosen_item}")
            grocery_items.pop(current_choice)
        else:
            print(f"Adding Item on Isle: {chosen_item}")
            grocery_items[current_choice] = chosen_item
        print(f"Your list now contains: {grocery_items}")
    else:
        print("Check out the current saved grocery items to select one!")
        for key, value in kroger_dict.items():
            print(f"{key}: {value}")
        print("quit: to finish")

    current_choice = input("> ")

final_list = sorted(grocery_items.items(), key=lambda y: y[1])
for i in final_list:
    print(i[0], "| Isle:", i[1])

j = json.dumps(sorted(grocery_items.items(), key=lambda y: y[1]))
with open("kroger.json", "w") as f:
    f.write(j)