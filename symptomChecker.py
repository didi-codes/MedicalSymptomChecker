def symptom_checker():
    print("Welcome to the Medical Symptom Checker!")
    print("Please describe your symptoms separated by commas (e.g., fever, cough, sore throat):")
    
    # Get user input, convert to lowercase, split into list of symptoms, and strip whitespace
    symptoms_input = input("Your symptoms: ").lower()
    symptoms = [symptom.strip() for symptom in symptoms_input.split(",")]

    # Rule 1: Flu Detection
    if "fever" in symptoms and "cough" in symptoms and "body aches" in symptoms:
        suggestion = "You may have the flu. It's recommended to rest and drink fluids. See a doctor if symptoms worsen."

    # Rule 2: Common Cold
    elif "runny nose" in symptoms and "sore throat" in symptoms and "fever" not in symptoms:
        suggestion = "You may have a common cold. Rest and over-the-counter medicine may help."

    # Rule 3: COVID-19 Concern
    elif "fever" in symptoms and "dry cough" in symptoms and ("loss of taste" in symptoms or "loss of smell" in symptoms or "loss of taste or smell" in symptoms):
        suggestion = "These symptoms may indicate COVID-19. Consider getting tested and self-isolate."

    # Rule 4: Allergy Symptoms
    elif "sneezing" in symptoms and "itchy eyes" in symptoms and "runny nose" in symptoms:
        suggestion = "These are likely allergy symptoms. Antihistamines may help."

    # Rule 5: Stomach Virus
    elif "nausea" in symptoms and "vomiting" in symptoms and "diarrhea" in symptoms:
        suggestion = "You may have a stomach virus. Stay hydrated and monitor symptoms."

    # Rule 6: Emergency Condition
    elif "chest pain" in symptoms or "shortness of breath" in symptoms:
        suggestion = "This may be a medical emergency. Seek immediate help or call 911."

    # Rule 7: No Match
    else:
        suggestion = "Your symptoms don't match any known conditions in our system. Please consult a healthcare provider for an accurate diagnosis."

    # Output the suggestion
    print("\nPreliminary Diagnosis:")
    print(suggestion)


# Run the symptom checker
symptom_checker()
