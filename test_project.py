from project import set_date
from project import add_food
from project import search_food

def test_set_date():
    assert set_date("14/29/2029") == "\nInvalid date." + "\n"
    assert set_date("14/32/2029") == "\nInvalid date." + "\n"
    assert set_date("12/30/2024") == "\nDate created: 12/30/2024\n"
    assert set_date("02/21/2006") == "\nDate created: 02/21/2006\n"

def test_search_food():
    assert search_food("broccoli") == "BROCCOLI | FDC ID: 2549992\n"
    assert search_food("BROCCOLI") == "BROCCOLI | FDC ID: 2549992\n"
    assert search_food("honey") == "HONEY | FDC ID: 2345841\n"
    assert search_food("white rice") == "WHITE RICE | FDC ID: 2488703\n"

def test_add_food():
    assert add_food("Q", "1") == "\nDate has not been set properly.\n"
    assert add_food("2345841", "50") == "\nInvalid input. FDC ID and amount must both be numeric.\n"
    