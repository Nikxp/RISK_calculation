
import logging
from fractions import Fraction
from typing import Iterable
from itertools import product

available_dices = range(1,7)
"""Comparator

result: (attacker_resources_lost, defender_resources_lost)
"""

def fight (attackers: Iterable, defenders: Iterable)->tuple:
    atk = list(attackers)
    defend = list(defenders)
    atk_lost = 0
    def_lost = 0
    atk.sort()
    defend.sort()
    for pair in zip(atk, defend):
        if (pair[0] > pair[1]):
            def_lost += 1
        else:
            atk_lost += 1
    return (atk_lost, def_lost)

def main():
    atk_squad_size = 3 
    def_squad_size = 2
    atk_lost = 0
    def_lost = 0
    print("Hello. Start calculating")
    for attackers in product(*[available_dices]*atk_squad_size):
        for defenders in product(*[available_dices]*def_squad_size):
            result = fight(attackers, defenders)
            atk_lost += result[0]
            def_lost += result[1]
            logging.info(f"{attackers = }, {defenders = }. atk loses {result[0]}, def_loses {result[1]}")
    if atk_lost > def_lost:
        print(f"Defenders wins! {atk_lost = } , but {def_lost = }")
    elif atk_lost < def_lost:
        print(f"Attackers wins! {atk_lost = } , and {def_lost = }")
    if atk_lost == def_lost:
        print(f"They are equal! {atk_lost = } , but {def_lost = }")
    print(f"Ratio is : {Fraction(atk_lost,atk_lost+def_lost)} or {atk_lost/(atk_lost+def_lost)}")
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    main()