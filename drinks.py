
import json
from datetime import datetime, timedelta

AGE = 15
WEIGHT_KG = 50

CAFFEINE_MG = {
    "filter_coffee": 140, "espresso": 65, "cappuccino": 65, "monster": 150, "red_bull_250ml": 80, "red_bull_355ml": 114
    
    }

def get_caffeine_day():
    sixhours = datetime.now() - timedelta(hours=6)
    return sixhours.date().isoformat()
    
def reset_today():
    save_data({"day": get_caffeine_day(), "total_mg": 0})

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)
    
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"day":"", "total_mg": 0}

def get_daily_limit(age, weight_kg):
    if age < 4:
        return 0
    elif age <= 6:
        return 45
    elif age <= 9:
        return 62.5
    elif age <= 12:
        return 85
    elif age <= 18:
        return weight_kg * 3
    elif age >= 19:
        return 400

def get_warning(total_mg, limit):
    if total_mg > limit:
        return "over"
    elif total_mg == limit:
        return "limit"
    elif total_mg == limit/2:
        return "half"
    else:
        return "ok"
    
def add_drink(drink_name):
    data = load_data()
    
    if data["day"] != get_caffeine_day():
        data["total_mg"] = 0
        data["day"] = get_caffeine_day()
        
    data["total_mg"] += CAFFEINE_MG[drink_name]
    
    save_data(data)
    
    if AGE <= 12 and drink_name != "coffee":
        return "no_energy_drinks"
        
    limit = get_daily_limit(AGE, WEIGHT_KG)
    return get_warning(data["total_mg"], limit)
        
    
