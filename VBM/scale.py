weight_scale = {
    "1": {
        "weight_scale": "Underweight",
        "risk": "Malnutrition_risk"
    },
    
    "2": {
        "weight_scale": "Normal_weight",
        "risk": "Low_risk"  
    },

    "3": {
        "weight_scale": "Overweight",
        "risk": "Enhanced_risk"
    },

    "4": {
        "weight_scale": "Moderately_obese",
        "risk": "Medium_risk"
    },

    "5": {
        "weight_scale": "Severely_obese",
        "risk": "High_risk"
    },

    "6": {
        "weight_scale": "Very_severely_obese",
        "risk": "Very_high_risk"
    }
}

def get_weight_scale(index):
    return weight_scale.get(str(index))