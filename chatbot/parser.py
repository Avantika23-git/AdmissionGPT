# parser.py

import re

def extract_rank_category(text):

    text_upper = text.upper()

    # -----------------
    # RANK
    # -----------------

    rank = None

    rank_match = re.search(
        r"\d+",
        text
    )

    if rank_match:
        rank = int(rank_match.group())

    # -----------------
    # CATEGORY MAPPING
    # -----------------

    category_map = {

        "GENERAL":"GN",
        "GEN":"GN",
        "GN":"GN",

        "ST":"ST",

        "SC":"SC",

        "EZHAVA":"EZ",
        "EZ":"EZ",

        "EW":"EW",

        "MUSLIM":"MU",
        "MU":"MU",

        "BH":"BH",
        "VK":"VK",
        "LA":"LA",
        "DV":"DV",
        "BX":"BX",
        "KU":"KU",
        "KN":"KN"
    }

    category = None

    for key, value in category_map.items():

        if key in text_upper:

            category = value
            break

    return rank, category
"""print(extract_rank_category(
    "Rank 12000 muslim"
))"""

# (12000,'EZ')