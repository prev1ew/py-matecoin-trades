import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    file_data = None
    money_res = 0
    coins_res = 0
    with open(filename) as file_opened:
        file_data = json.load(file_opened)
    for el in file_data:
        is_it_a_purchase = el["bought"] is not None

        purchased_amount = Decimal(el["bought"]) if is_it_a_purchase \
            else Decimal(el["sold"]) * -1

        money_res += purchased_amount * Decimal(el["matecoin_price"])
        coins_res += purchased_amount

    with open("profit.json", "w+") as curr_file:
        obj_to_dump = {
            "earned_money": f"{money_res: .f}",
            "matecoin_account": f"{coins_res: .f}"
        }
        json.dump(obj_to_dump, curr_file)
