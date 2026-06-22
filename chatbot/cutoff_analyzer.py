import pandas as pd

cutoff_df = pd.read_excel(
    "data/MEC_KEAM_Cutoff_Consolidated.xlsx"
)

category_mapping = {

    "GN": ["SM", "MG"],

    "EZ": ["EZ","SM","MG"],
    "MU": ["MU","SM","MG"],
    "EW": ["EW"],
    "SC": ["SC"],
    "ST": ["ST"],
    "BH": ["BH"],
    "VK": ["VK"],
    "LA": ["LA"],
    "DV": ["DV"],
    "BX": ["BX"],
    "KU": ["KU"],
    "KN": ["KN"]
}

def analyze_cutoff(rank, category):

    admission_categories = category_mapping.get(
        category,
        []
    )

    filtered = cutoff_df[
        cutoff_df["Admission Category"].isin(
            admission_categories
        )
    ]

    result = []

    grouped = filtered.groupby(
        [
            "Course",
            "Admission Category"
        ]
    )["Last Rank"].mean()

    grouped = grouped.reset_index()

    for _, row in grouped.iterrows():

        cutoff = row["Last Rank"]

        if rank <= cutoff * 0.5:
            chance = "Very High Chance"

        elif rank <= cutoff:
            chance = "High Chance"

        elif rank <= cutoff * 1.3:
            chance = "Possible"

        else:
            chance = "Low Chance"

        result.append({

            "Course": row["Course"],

            "Admission Category":
            row["Admission Category"],

            "Average Cutoff":
            int(cutoff),

            "Chance": chance

        })

    result = pd.DataFrame(result)

    result = result.sort_values(
        by="Average Cutoff"
    )

    return result