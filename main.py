from resources import MENU, resources_data

def checking_input_user(val):
    return val in ["espresso", "latte", "cappuccino", "report", "off"]

def report():
    return (f"Water: {resources_data['water']}ml\n"
            f"Milk: {resources_data['milk']}ml\n"
            f"Coffee: {resources_data['coffee']}g\n"
            f"Money: ${resources_data['money']}")

def checking_ingredients(menu_item, resources):
    ingredients = MENU[menu_item]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}")
            return False
    return True

def process_coins():
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }
    total = 0.0

    while True:
        print("Please insert coins:")
        print("1. Quarters ($0.25)")
        print("2. Dimes ($0.10)")
        print("3. Nickels ($0.05)")
        print("4. Pennies ($0.01)")
        print("type 'stop' if you're done")

        user_coin = input("insert coins that you want to give (eg.quarters):").lower()
        if user_coin == "stop":
            break
        if user_coin not in coins.keys():
            print("invalid input, please input value that we have show")
            continue

        while True:
            try:
                amount_coin = int(input(f"how much {user_coin}?:"))
                break
            except ValueError:
                print("invalid input, please input number value")
        total += coins[user_coin] * amount_coin

    return total

def checking_money(user_money, coffee_price):
    if user_money == coffee_price:
        return True
    elif user_money > coffee_price:
        change = user_money - coffee_price
        print("--------------------------------------------------------")
        print(f"Transaction successful. Your change is ${change:.2f}")
        return True
    else:
        short = coffee_price - user_money
        print("--------------------------------------------------------")
        print(f"Sorry, not enough money, You need ${short:.2f} more")
        return False

def make_coffee(coffee_name):
    coffee_ingredient = MENU[coffee_name]['ingredients']
    coffee_price = MENU[coffee_name]['cost']
    print("report before purchasing")
    print(report())
    for item in coffee_ingredient:
        resources_data[item] = resources_data[item] - coffee_ingredient[item]
    resources_data["money"] += coffee_price
    print("==========================")
    print("report after purchasing")
    print(report())




def main():
    machine_on = True
    # prompt user by asking
    while machine_on:
        while True:
            user_request = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
            if checking_input_user(user_request):
                break
            print("Invalid input, Please choose from espresso, latte, or cappuccino")
            print("=================================================================")

        if user_request == "report":
            print(report())
        elif user_request == "off":
            machine_on = False
        elif user_request in MENU:
            if not checking_ingredients(menu_item=user_request, resources=resources_data):
                continue
            user_money = process_coins()
            if not checking_money(user_money, MENU[user_request]["cost"]):
                continue
            make_coffee(user_request)


    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()


