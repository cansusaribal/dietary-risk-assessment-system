# Personalized Dietary Risk Assessment System (KBRDS)

A rule-based clinical decision support system designed to evaluate dietary risks based on user-specific chronic diseases, food allergies, and nutritional preferences.

Why we built this?
Standard diet plans usually treat everyone the same. But in real life, a person might have both Diabetes and Celiac disease, or high blood pressure with specific allergies.
We wanted to create a system that takes all of a person’s medical restrictions at once and checks if a specific food is actually safe for them—giving instant, color-coded feedback instead of confusing medical jargon.

How the Risk Engine works
The core logic works with a "Most Restrictive Rule Applies" approach:
Allergy Check: If an allergen is found, it immediately flags it as critical (Purple).
Diet Preferences: Checks if the food matches choices like Vegan, Halal, etc.
Chronic Diseases: Evaluates nutritional values (glycemic index, sodium, gluten, lactose) for each condition.
Final Decision: If there is any conflict, the highest risk level wins (Green = Safe, Yellow = Caution, Red = Risky).

Architecture & Tech Stack
We designed the system around a 4-tier architecture to keep the business logic clean and secure:
Core Logic: Python (Object-Oriented design)
Database & Cache: PostgreSQL for user/food data & Redis for caching fast search responses
Security: AES-256 for sensitive health records, Bcrypt for passwords, and JWT for sessions (KVKK & GDPR compliant)
Mobile UI: Clean mobile interface with quick search and test result tracking

### 🚀 Running the prototype locally
You can test the sample simulation (which evaluates sample profiles like Celiac + Diabetes) by running:

```bash
python main.py
