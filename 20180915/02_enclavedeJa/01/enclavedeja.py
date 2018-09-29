def get_price(seasons):

    price_table = {
        "4": .8,
        "2": .9
    }

    num_seasons = len(seasons)
    price = len(seasons) * 5

    for qty, discount in price_table.items():
        if num_seasons > int(qty):
            return price * discount 
    return price

