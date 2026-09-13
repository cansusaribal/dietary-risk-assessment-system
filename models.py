from enum import Enum

class RiskLevel(Enum):
    SAFE = "GUVENLI"
    CAUTION = "DIKKATLI"
    HIGH_RISK = "RISKLI"
    ALLERGEN = "ALERJI"
    DIET_NON_COMPLIANT = "DIYET_DISI"

class DietPreference(Enum):
    VEGETARIAN = "VEJETARYEN"
    VEGAN = "VEGAN"
    PESCATARIAN = "PESKETARYEN"
    HALAL = "HELAL"
    STANDARD = "NORMAL"

class DiseaseType(Enum):
    DIABETES = "DIYABET"
    CELIAC = "COLYAK"
    HYPERTENSION = "HIPERTANSIYON"
    LACTOSE_INTOLERANCE = "LAKTOZ_INTOLERANSI"
    IBS = "IBS"
    HIGH_CHOLESTEROL = "YUKSEK_KOLESTEROL"
    GERD = "REFLU"

class FoodCategory(Enum):
    VEGETABLE = "SEBZE"
    FRUIT = "MEYVE"
    GRAIN = "TAHIL"
    DAIRY = "SUT_URUNLERI"
    MEAT_FISH = "ET_BALIK"
    LEGUME = "BAKLAGIL"
    NUTS = "KURUYEMIS"
    BEVERAGE = "ICECEK"
    OTHER = "DIGER"

class HealthProfile:
    def __init__(self, user_id, age, height_cm, weight_kg, diet_preference, chronic_diseases=None, allergens=None):
        self.user_id = user_id
        self.age = age
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.diet_preference = diet_preference
        self.chronic_diseases = chronic_diseases if chronic_diseases else []
        self.allergens = allergens if allergens else []

class NutritionalValue:
    def __init__(self, calories, protein, carbohydrates, fat, fiber, sodium_mg, sugar_g, glycemic_index, contains_gluten=False, contains_lactose=False):
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.fiber = fiber
        self.sodium_mg = sodium_mg
        self.sugar_g = sugar_g
        self.glycemic_index = glycemic_index
        self.contains_gluten = contains_gluten
        self.contains_lactose = contains_lactose

class FoodItem:
    def __init__(self, food_id, name, category, nutrition, dietary_tags=None, allergen_tags=None):
        self.food_id = food_id
        self.name = name
        self.category = category
        self.nutrition = nutrition
        self.dietary_tags = dietary_tags if dietary_tags else []
        self.allergen_tags = allergen_tags if allergen_tags else []

class EvaluationResult:
    def __init__(self, food_id, food_name, overall_risk, color_code, is_edible, reasons=None):
        self.food_id = food_id
        self.food_name = food_name
        self.overall_risk = overall_risk
        self.color_code = color_code
        self.is_edible = is_edible
        self.reasons = reasons if reasons else []
