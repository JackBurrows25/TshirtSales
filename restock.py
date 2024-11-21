def restock_inventory(available_items, inventory_records, current_day):
    '''
    This function is responsible for updating the stock/restock for a given day.
    ---------------
    Function Input:
    ---------------
    available_items: (integer) Available Tshirts from the previous day.
    inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
    current_day: (integer) Day number which you want to add as the current day. 

    ----------------
    Function Output:
    ----------------
    available_items: (integer) This function returns this integer which updates the available items at the current day.
    The function will also update the inventory_records (For restocking) for a given current day. 
    '''
    if current_day == 0:
        available_items = 0
        stock_needed = 2000 
    if current_day % 7 == 0: 
        stock_needed = 2000 - available_items
        available_items += stock_needed
        inventory_records.append([current_day, 0, stock_needed, available_items])

    return available_items

