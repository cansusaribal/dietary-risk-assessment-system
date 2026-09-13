from models import RiskLevel, DiseaseType, EvaluationResult

class ClinicalRiskEngine:
    """
    Personalized Dietary Decision Support Engine.
    Evaluates multi-constraint physiological parameters using 
    the 'Most Restrictive Rule Applies' principle.
    """

    COLOR_MAP = {
        RiskLevel.SAFE: "GREEN",
        RiskLevel.CAUTION: "YELLOW",
        RiskLevel.HIGH_RISK: "RED",
        RiskLevel.ALLERGEN: "PURPLE",
        RiskLevel.DIET_NON_COMPLIANT: "BLUE"
    }

    def evaluate(self, profile, food):
        reasons = []

       
        for user_allergy in profile.allergens:
            if user_allergy.lower() in [tag.lower() for tag in food.allergen_tags]:
                return EvaluationResult(
                    food_id=food.food_id,
                    food_name=food.name,
                    overall_risk=RiskLevel.ALLERGEN,
                    color_code=self.COLOR_MAP[RiskLevel.ALLERGEN],
                    is_edible=False,
                    reasons=[f"Contains critical allergen: {user_allergy}"]
                )

       
        if profile.diet_preference not in food.dietary_tags:
            return EvaluationResult(
                food_id=food.food_id,
                food_name=food.name,
                overall_risk=RiskLevel.DIET_NON_COMPLIANT,
                color_code=self.COLOR_MAP[RiskLevel.DIET_NON_COMPLIANT],
                is_edible=False,
                reasons=[f"Item conflicts with {profile.diet_preference.value} dietary preference."]
            )

     
        detected_risks = []

        for disease in profile.chronic_diseases:
            risk, justification = self._check_disease_constraint(disease, food)
            if risk != RiskLevel.SAFE:
                detected_risks.append(risk)
                if justification:
                    reasons.append(justification)

        if RiskLevel.HIGH_RISK in detected_risks:
            final_risk = RiskLevel.HIGH_RISK
        elif RiskLevel.CAUTION in detected_risks:
            final_risk = RiskLevel.CAUTION
        else:
            final_risk = RiskLevel.SAFE
            reasons.append("Nutritional profile aligns with metabolic constraints.")

        return EvaluationResult(
            food_id=food.food_id,
            food_name=food.name,
            overall_risk=final_risk,
            color_code=self.COLOR_MAP[final_risk],
            is_edible=(final_risk != RiskLevel.HIGH_RISK),
            reasons=reasons
        )

    def _check_disease_constraint(self, disease, food):
        nutrition = food.nutrition

        if disease == DiseaseType.DIABETES:
            if nutrition.glycemic_index > 70 or nutrition.sugar_g > 20:
                return RiskLevel.HIGH_RISK, "High Glycemic Index / Excessive sugar spike risk."
            if nutrition.glycemic_index > 55 or nutrition.sugar_g > 10:
                return RiskLevel.CAUTION, "Moderate glycemic load; portion control required."

        elif disease == DiseaseType.CELIAC:
            if nutrition.contains_gluten:
                return RiskLevel.HIGH_RISK, "Contains gluten, prohibited for Celiac pathology."

        elif disease == DiseaseType.HYPERTENSION:
            if nutrition.sodium_mg > 400:
                return RiskLevel.HIGH_RISK, "Excessive sodium concentration."
            if nutrition.sodium_mg > 200:
                return RiskLevel.CAUTION, "Elevated sodium level; consume with caution."

        elif disease == DiseaseType.LACTOSE_INTOLERANCE:
            if nutrition.contains_lactose:
                return RiskLevel.HIGH_RISK, "Contains lactose."

        return RiskLevel.SAFE, None
