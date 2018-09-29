def add_to_discount_list(season, discount_lists):

     for discount_list in discount_lists:
        if season not in discount_list:
            discount_list.append(season)
            return
     discount_lists.append([season])
     return

def get_series_price(seasons):
    prices = {
        "0": 2.5,
        "1": 3,
        "2": 3.5,
        "3": 4,
        "4": 4.5,
        "5": 5
    }

    discount = {
        "1": 1,
        "2": 1,
        "3": .9,
        "4": .8,
        "5": .7,
        "6": .7
    }

    curr_discount = discount[str(len(seasons))]
    return curr_discount * sum([prices[str(season)] for season in seasons if season != 5]) + seasons.count(5) * prices["5"]



def get_price(seasons):

    discount_lists = []

    for season in seasons:
        add_to_discount_list(season, discount_lists)

    print(discount_lists)

    return round(sum([get_series_price(discount_list) for discount_list in discount_lists]), 2)
