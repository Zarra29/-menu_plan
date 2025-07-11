# Health and Diet Assessment and Menu Plan for Adults/U-5 children/Pregnent Woman /Lactating Mother

age = int(input("Enter your age: "))
gender = input("Enter your gender (male/female): ").lower()
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
muac = float(input("Enter your MUAC (Mid-Upper Arm Circumference) in cm: "))
activity = input("Enter your activity level (low/moderate/high): ").lower()

print("\nWho are you planning the diet for?")
print("1. General (adult)")
print("2. Malnourished child under 5")
print("3. Pregnant woman")
print("4. Lactating mother")

group = input("Enter 1, 2, 3 or 4: ")

height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Your MUAC is: {muac:.1f} cm")

quote = ""
health_status = ""

if group == "1":
    if bmi < 18.5:
        health_status = "You are underweight and might be at risk of malnutrition."
        quote = "Let food be thy medicine and medicine be thy food. – Hippocrates"
        print(f"\nHealth Status: {health_status}")
        print("\nSuggested Daily Meal Plan for Underweight:")
        print("Breakfast: Paratha with honey, boiled egg, and a glass of full-fat milk")
        print("Mid-Morning: Banana or seasonal fruits")
        print("Lunch: Rice with fish curry, mixed vegetables, and dal")
        print("Snack: Chira with jaggery and milk")
        print("Dinner: Khichuri with lentils, vegetables, and boiled egg")
        print("Before Bed: Warm milk with a spoon of ghee or honey")

    elif 18.5 <= bmi < 25:
        health_status = "You have a normal weight. Keep maintaining your healthy lifestyle!"
        quote = "Health is not valued till sickness comes. – Thomas Fuller"
        print(f"\nHealth Status: {health_status}")
        print("\nSuggested Daily Meal Plan for Maintaining Weight:")
        print("Breakfast: Paratha, boiled egg, and a glass of milk")
        print("Mid-Morning: Seasonal fruits or lassi")
        print("Lunch: Rice with chicken curry, mixed vegetables, and dal")
        print("Snack: Chira mixed with banana and milk")
        print("Dinner: Khichuri with lentils, vegetables, and boiled egg")
        print("Before Bed: Warm milk with a spoon of honey")

    else:
        if bmi < 30:
            health_status = "You are overweight. Consider losing some weight for better health."
        else:
            health_status = "You are obese. It is important to lose weight for your health."
        quote = "Take care of your body. It's the only place you have to live. – Jim Rohn"
        print(f"\nHealth Status: {health_status}")
        print("\nSuggested Daily Meal Plan for Weight Loss:")
        print("Breakfast: Oats porridge with fruits and a boiled egg")
        print("Mid-Morning: Fresh vegetable juice or green tea")
        print("Lunch: Brown rice with grilled fish or chicken and steamed vegetables")
        print("Snack: A handful of nuts or seasonal fruit")
        print("Dinner: Vegetable soup with salad and a small portion of lean protein")
        print("Before Bed: Warm turmeric milk (without sugar)")

    if muac < 23.5:
        print("\nNote: Your MUAC suggests nutritional risk, please consult a healthcare provider.")

elif group == "2":
    if muac < 11.5:
        health_status = "Severe acute malnutrition detected. Immediate medical care is needed."
        quote = "Nutrition is the foundation for health."
    elif 11.5 <= muac < 12.5:
        health_status = "Moderate acute malnutrition. Nutritional support recommended."
        quote = "Small steps in nutrition can make a big difference."
    else:
        health_status = "Child’s nutritional status is normal."
        quote = "Healthy children, happy future."
    print(f"\nHealth Status: {health_status}")
    print("\nSuggested Daily Meal Plan for Malnourished Child Under 5:")
    print("Breakfast: Suji with milk and mashed banana")
    print("Mid-Morning: Boiled egg yolk and mashed potato")
    print("Lunch: Soft rice, masoor dal, mashed fish with mustard oil")
    print("Snack: Banana or biscuit with a glass of milk")
    print("Dinner: Khichuri with egg or vegetables, mashed papaya")
    print("Before Bed: Half cup of milk")

elif group == "3":
    if muac < 23:
        health_status = "You may be at risk of malnutrition. Nutritional care is advised."
        quote = "Good nutrition is a foundation for a healthy pregnancy."
    else:
        health_status = "Your nutritional status seems normal."
        quote = "A healthy mom means a healthy baby."
    print(f"\nHealth Status: {health_status}")
    print("\nSuggested Daily Meal Plan for Pregnant Woman:")
    print("Breakfast: Ruti with dim curry and a glass of milk")
    print("Mid-Morning: Seasonal fruits like banana or guava")
    print("Lunch: Rice, fish curry, shobji (leafy greens), and dal")
    print("Snack: Chira mixed with milk or doi")
    print("Dinner: Khichuri with egg or meat and salad")
    print("Before Bed: Warm milk with a date or some nuts")

elif group == "4":
    if muac < 23:
        health_status = "You may be at risk of malnutrition. Nutritional care is advised."
        quote = "Good nutrition supports both mother and child."
    else:
        health_status = "Your nutritional status seems normal."
        quote = "Nourish yourself to nourish your baby."
    print(f"\nHealth Status: {health_status}")
    print("\nSuggested Daily Meal Plan for Lactating Mother:")
    print("Breakfast: Paratha, boiled egg, and a glass of milk")
    print("Mid-Morning: Seasonal fruits or lassi")
    print("Lunch: Rice with chicken curry, mixed vegetables, and dal")
    print("Snack: Chira mixed with banana and milk")
    print("Dinner: Khichuri with lentils, vegetables, and boiled egg")
    print("Before Bed: Warm milk with a spoon of honey")

else:
    print("Invalid selection. Please choose from 1 to 4.")
    exit()

print(f"\nNutrition Quote:\n{quote}")
print("\nThank you for using the Smart Health & Nutrition Planner! Stay healthy and take care!")
