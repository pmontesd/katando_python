def add_to_discount_list(season, discount_lists):

     for discount_list in discount_lists:
        if season not in discount_list:
            discount_list.append(season)
            return
     discount_lists.append([season])
     return

def get_series_price(seasons):
    prices = {
        "0": 3,
        "1": 3.5,
        "2": 4,
        "3": 4.5,
        "4": 5
    }

    discount = {
        "1": 1,
        "2": 1,
        "3": .9,
        "4": .8,
        "5": .7
    }

    curr_discount = discount[str(len(seasons))]
    nom_price = sum([prices[str(season)] for season in seasons])

    return round(curr_discount * nom_price, 2)


def get_price(seasons):

    discount_lists = []

    for season in seasons:
        add_to_discount_list(season, discount_lists)

    return sum([get_series_price(discount_list) for discount_list in discount_lists])
