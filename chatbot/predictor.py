import pandas as pd
import joblib

# Load saved files

model = joblib.load(
    "models/branch_model.pkl"
)

cat_encoder = joblib.load(
    "models/cat_encoder.pkl"
)

course_encoder = joblib.load(
    "models/course_encoder.pkl"
)


def recommend_branches(rank, category):

    category_encoded = cat_encoder.transform(
        [category]
    )[0]

    sample = pd.DataFrame({
    "KEAM Rank":[rank],
    "Category_Encoded":[category_encoded]
})

    probs = model.predict_proba(sample)[0]

    result = pd.DataFrame({
        "Course": course_encoder.inverse_transform(
            range(len(probs))
        ),
        "Probability": probs * 100
    })

    result = result.sort_values(
        by="Probability",
        ascending=False
    )

    return result.head(2)