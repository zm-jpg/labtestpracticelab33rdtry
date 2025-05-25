import price_info as price

def test_total_cost_shopping():
    result=price.total_cost_shopping()
    expected=46.75
    assert (result==expected)

def test_cost_of_fruits():
    result=price.cost_of_fruits('watermelon', 100)
    expected=650
    assert(result==expected)