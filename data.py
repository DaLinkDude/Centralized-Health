# data.py

HEALTH_DATABASE = {
    "Alzheimer's Disease": {
        "summary": "A progressive disease that destroys memory and other important mental functions.",
        "levers": [
            {"factor": "B Vitamins (Folate, B6, B12)",
             "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Deep Sleep",
                "impact": "Essential for the glymphatic system to clear out amyloid-beta plaques from the brain."}
        ],
        "foods": [
            {"Food": "Spinach", "Key Nutrient": "Folate / Vitamin B9",
                "Type": "Leafy Green"},
            {"Food": "Wild Salmon",
                "Key Nutrient": "Vitamin B12 & Omega-3", "Type": "Seafood"},
            {"Food": "Walnuts", "Key Nutrient": "Polyphenols & Vitamin E", "Type": "Nut"}
        ]
    },
    "Type 2 Diabetes": {
        "summary": "A chronic condition that affects the way the body processes blood sugar (glucose).",
        "levers": [
            {"factor": "Dietary Fiber",
                "impact": "Slows sugar absorption, improving blood sugar levels and preventing insulin spikes."},
            {"factor": "Magnesium Intake",
                "impact": "Plays a crucial role in glucose metabolism; deficiency is frequently linked to insulin resistance."}
        ],
        "foods": [
            {"Food": "Avocado", "Key Nutrient": "Healthy Fats & Fiber", "Type": "Fruit"},
            {"Food": "Lentils", "Key Nutrient": "Soluble Fiber & Magnesium",
                "Type": "Legume"},
            {"Food": "Pumpkin Seeds", "Key Nutrient": "Magnesium", "Type": "Seed"}
        ]
    },
    "Heart Disease": {
        "summary": "A range of conditions that affect the heart, often linked to plaque buildup in the arteries.",
        "levers": [
            {"factor": "Omega-3 Fatty Acids",
                "impact": "Helps lower triglycerides, reduce blood pressure, and decrease inflammation in blood vessels."},
            {"factor": "Potassium Intake",
                "impact": "Crucial for managing blood pressure because it helps your body ease tension in your blood vessel walls."}
        ],
        "foods": [
            {"Food": "Bananas", "Key Nutrient": "Potassium", "Type": "Fruit"},
            {"Food": "Chia Seeds",
                "Key Nutrient": "Plant-based Omega-3 (ALA)", "Type": "Seed"},
            {"Food": "Extra Virgin Olive Oil",
                "Key Nutrient": "Oleic Acid / Antioxidants", "Type": "Healthy Fat"}
        ]
    }
}
