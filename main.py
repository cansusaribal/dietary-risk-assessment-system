from models import (
    HealthProfile, FoodItem, NutritionalValue, 
    DietPreference, DiseaseType, FoodCategory
)
from risk_engine import ClinicalRiskEngine

def run_simulation():
    engine = ClinicalRiskEngine()

    # User Profile: Student with Celiac and Diabetes tendencies
    patient = HealthProfile(
        user_id=101,
        age=21,
        height_cm=165.0,
        weight_kg=52.0,
        diet_preference=DietPreference.HALAL,
        chronic_diseases=[DiseaseType.CELIAC, DiseaseType.DIABETES],
        allergens=["Lactose"]
    )

   
    baklava = FoodItem(
        food_id=1,
        name="Baklava",
        category=FoodCategory.OTHER,
        nutrition=NutritionalValue(
            calories=420.0, protein=5.0, carbohydrates=65.0, fat=18.0,
            fiber=1.2, sodium_mg=110.0, sugar_g=38.0, glycemic_index=85,
            contains_gluten=True, contains_lactose=True
        ),
        dietary_tags=[DietPreference.HALAL, DietPreference.STANDARD],
        allergen_tags=["Lactose", "Gluten", "Nuts"]
    )

    grilled_chicken = FoodItem(
        food_id=2,
        name="Grilled Chicken Salad",
        category=FoodCategory.MEAT_FISH,
        nutrition=NutritionalValue(
            calories=220.0, protein=32.0, carbohydrates=4.0, fat=7.0,
            fiber=3.5, sodium_mg=180.0, sugar_g=1.5, glycemic_index=15,
            contains_gluten=False, contains_lactose=False
        ),
        dietary_tags=[DietPreference.HALAL, DietPreference.STANDARD],
        allergen_tags=[]
    )

    print(f"--- CLINICAL EVALUATION FOR PATIENT ID: {patient.user_id} ---")
    for item in [baklava, grilled_chicken]:
        result = engine.evaluate(patient, item)
        print(f"\nFood: {result.food_name}")
        print(f"Risk Level: {result.overall_risk.value} [{result.color_code}]")
        print(f"Edible: {'YES' if result.is_edible else 'NO'}")
        print(f"Clinical Reasons: {'; '.join(result.reasons)}")

if __name__ == "__main__":
    run_simulation()
