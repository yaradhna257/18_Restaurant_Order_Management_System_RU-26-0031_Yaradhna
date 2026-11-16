print("--- Welcome to Restaurant Order Management System ---")

menu = {
    "Burger": 100,
    "Pizza": 200,
    "Coffee": 50
}

while True:
    table_input = input("Table: ")
    if not table_input.isdigit():
        print("Invalid table number. Enter a number between 1 and 20.")
        continue
    table = int(table_input)
    if table < 1 or table > 20:
        print("Invalid table number. Enter a number between 1 and 20.")
    else:
        break

table_orders = []  

while True:
    print("\n1. Add")
    print("2. Generate bill")
    print("3. Exit")

    choice = input("choice: ")

    if choice == "Add" or choice == "1":
        order = input("Order item: ")
        if order not in menu:
            print(f"Item not on the menu. Available: {', '.join(menu.keys())}")
            continue

      
        qwt_input = input("Quantity: ")
        if not qwt_input.isdigit():
            print("Invalid quantity. Enter a whole number.")
            continue
        qwt = int(qwt_input)

        amount = menu[order] * qwt
        
        
        item_found = False
        for entry in table_orders:
            if entry["item"] == order:
                entry["qwt"] += qwt
                entry["amount"] += amount
                item_found = True
                break
        if not item_found:
            table_orders.append({"item": order, "qwt": qwt, "amount": amount})

        print(f"{order} x{qwt} added to Table {table} | Amount: {amount}")

    elif choice == "Generate bill" or choice == "2":
        if not table_orders:
            print("No items ordered yet.")
            break

       
        item_strings = [f"{entry['item']} x{entry['qwt']} = {entry['amount']}" for entry in table_orders]
        subtotal = sum(entry["amount"] for entry in table_orders)
        service_charge = subtotal * 0.10
        gst = subtotal * 0.05
        total = subtotal + service_charge + gst

        
        if len(item_strings) > 1:
            print(" | ".join(item_strings))
        
        print(f"Subtotal: {subtotal} | Service charge (10%): {service_charge:.2f}")
        print(f"GST (5%): {gst:.2f} | Total: {total:.2f}")
        break

    elif choice == "Exit" or choice == "3":
        print("Thank You! Please Come Again.")
        break

    else:
        print("Invalid choice. Please choose 'Add' or 'Generate bill'.")

   
