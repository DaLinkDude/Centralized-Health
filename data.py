# data.py

HEALTH_DATABASE = {
    "Alzheimer's Disease": {
        "summary": "Best preventative measures are good, deep sleep, excercise, and mentally stimulating activities.",
        "nutrients": [
            {"factor": "B Vitamins (Folate, B6, B12)",
                "impact": "Limited evidence that B vitmamins/Folate help slow/prevent dementia, it is associated with slowing cognitive decline."},
            {"factor": "Magnesium",
                "impact": "Most people have healthy levels of magnesium. Defiiceny is linked to a 36% risk increase and excesssive levels increase risk by 30%."},
            {"factor": "Pottasium",
                "impact": "Some evidence to show that a higher intake of pottasium decreases odds of cognitive impairment, most people are pottasium defficient."},
        ],
        "actions": [
            {"factor": "Sleep Well",
                "impact": "20-45% lower risk with 150minutes of activity. Improves blood flow to brain, supports brain cell surivvival, and lowers chronic inflammation."},
            {"factor": "Excercise",
                "impact": "~30-40% lower risk of dementia compared to people that sleep <6 hours. Helps the brain clear out toxic byproducts."},
            {"factor": "Mentally Stimulating Activities",
                "impact": "5 year delayed onset of alzheimers with high levels of cognitive activity compared to low activity."},
        ],
        "risks": [
            {"factor": "Smoking",
                "impact": "40% higher risk due to sustained lack of oxygen in brain (nicotine/carbon monoxide) and combustion products cause oxidative stress and inflammation"},
            {"factor": "Excessive Alcohol",
                "impact": "Excessive alcohol increases risk significantly due to decreased brain volume/white matter, restricted blood flow, depleteing B1 vitamin, and oxidative stress"},
        ],
    },
    "Arthritis": {
        "summary": "A broad name for conditions that cause inflammation, swelling, and pain in joints/connective tissues.",
        "nutrients": [
            {"factor": "Monounsaturated Fats (healthy fats)",
                "impact": "Lowers systemic inflammation examples are olive oil, avocados, and nuts."},
            {"factor": "Omega-3s",
                "impact": "Act in a similiar way to monounsaturated fats, come from fatty fish, nuts, or plant oils (canola, soybean, etc.)."},
            {"factor": "Fiber",
                "impact": "Decreases inflammation, comes from oats, brown rice, whole grains."},
            {"factor": "Antioxidants",
                "impact": "Slows/decreases downstream cartilage breakdown, chronic inflammatoin, and joint tissue death. Eat your fruits/vegetables."},
        ],
        "actions": [
            {"factor": "sleep well",
                "impact": "Helps the brain clear out toxic byproducts, regular <6 hours/night results in ~30-40% higher risk of dementia "},
            {"factor": "excersize",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
        ],
    },
    "Heart Disease": {
        "summary": "A range of conditions that affect the heart, often linked to plaque buildup in the arteries.",
        "nutrients": [
            {"factor": "B Vitamins (Folate, B6, B12)",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Magnesium",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Pottasium",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Deep Sleep",
                "impact": "Essential for the glymphatic system to clear out amyloid-beta plaques from the brain."}
        ],
        "actions": [
            {"factor": "sleep well",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "excersize",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Pottasium",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Deep Sleep",
                "impact": "Essential for the glymphatic system to clear out amyloid-beta plaques from the brain."}
        ],
    },
}

SUBSTANCE_DATABASE = {
    "Nicotine": {
        "summary": "bad bad bad",
        "nutrients": [
            {"factor": "poo",
                "impact": "Limited evidence that B vitmamins/Folate help slow/prevent dementia, it is associated with slowing cognitive decline."},
            {"factor": "Magnesium",
                "impact": "Most people have healthy levels of magnesium. Defiiceny is linked to a 36% risk increase and excesssive levels increase risk by 30%."},
            {"factor": "Pottasium",
                "impact": "Some evidence to show that a higher intake of pottasium decreases odds of cognitive impairment, most people are pottasium defficient."},
        ],
        "actions": [
            {"factor": "sleep well",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "excersize",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Pottasium",
                "impact": "Helps lower homocysteine levels, an amino acid linked to brain atrophy and increased Alzheimer's risk."},
            {"factor": "Deep Sleep",
                "impact": "Essential for the glymphatic system to clear out amyloid-beta plaques from the brain."}
        ],
    }
}
