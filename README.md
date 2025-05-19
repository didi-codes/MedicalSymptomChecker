# Part 1: Initial Project Ideas

1. Customer Service Chatbot
•	What it does: Simulates a help desk assistant that answers common customer questions.
•	How it works: Uses if-else rules to detect keywords or phrases like "hours," "return policy," or "shipping" in the user's input, and responds with predefined answers.
Example:
•	if "return" in user_input:
•	    return "Our return policy allows returns within 30 days with a receipt."

2. Movie Recommendation System
•	What it does: Suggests movies based on user preferences like genre, mood, or decade.
•	How it works: Follows logic rules to match user input to a list of movies.
Example:
•	if genre == "comedy" and mood == "light":
•	    return ["The Mask", "Ferris Bueller's Day Off"]

3. Medical Symptom Checker
•	What it does: Helps users identify possible illnesses based on symptoms.
•	How it works: Uses rules like "if fever and sore throat, suggest flu" to match input symptoms to possible conditions.
Example:
•	if "fever" in symptoms and "cough" in symptoms:
•	    return "You may have the flu or a common cold. Please consult a doctor."

## Chosen Project: Medical Symptom Checker
Justification:
I’m most interested in the medical symptom checker because it has real-world relevance and shows how expert systems can provide decision support. It also allows for a wide range of rule combinations, making it a great exercise in building and testing logical conditions.

# Part 2: Rules/Logic for the Chosen System

1.	Flu Detection
IF user reports "fever" AND "cough" AND "body aches"
THEN suggest: "You may have the flu. It's recommended to rest and drink fluids. See a doctor if symptoms worsen."
2.	Common Cold
IF user reports "runny nose" AND "sore throat" AND NOT "fever"
THEN suggest: "You may have a common cold. Rest and over-the-counter medicine may help."
3.	COVID-19 Concern
IF user reports "fever" AND "dry cough" AND "loss of taste or smell"
THEN suggest: "These symptoms may indicate COVID-19. Consider getting tested and self-isolate."
4.	Allergy Symptoms
IF user reports "sneezing" AND "itchy eyes" AND "runny nose"
THEN suggest: "These are likely allergy symptoms. Antihistamines may help."
5.	Stomach Virus
IF user reports "nausea" AND "vomiting" AND "diarrhea"
THEN suggest: "You may have a stomach virus. Stay hydrated and monitor symptoms."

# Part 3: Rules/Logic for the Chosen System
Sample input and output: 

Welcome to the Medical Symptom Checker!
Please describe your symptoms separated by commas (e.g., fever, cough, sore throat):
Your symptoms: fever, cough, body aches

Preliminary Diagnosis:
You may have the flu. It's recommended to rest and drink fluids. See a doctor if symptoms worsen.

Welcome to the Medical Symptom Checker!
Please describe your symptoms separated by commas (e.g., fever, cough, sore throat):
Your symptoms: nausea, vomiting, diarrhea

Preliminary Diagnosis:
You may have a stomach virus. Stay hydrated and monitor symptoms.

Welcome to the Medical Symptom Checker!
Please describe your symptoms separated by commas (e.g., fever, cough, sore throat):
Your symptoms: chest pain

Preliminary Diagnosis:
This may be a medical emergency. Seek immediate help or call 911.

# Part 4: Reflection

## Project Overview
My rule-based system is a Medical Symptom Checker designed to simulate how early AI systems used decision trees and if-then logic to mimic reasoning. The system takes user input in the form of symptoms separated by commas and compares the input against a set of predefined rules. Each rule represents a specific condition (such as the flu, common cold, or COVID-19), and if the symptoms match those defined in a rule, the system provides a recommendation or possible diagnosis. If no match is found, it advises the user to consult a healthcare provider. This approach reflects how early AI systems operated based on heuristics and expert knowledge rather than learning from data.

## Challenges
1. While building the system with the help of AI, one challenge I encountered was figuring out how to phrase my prompts clearly to get the most accurate and relevant assistance. At first, my descriptions of the project idea were too vague, which led to general suggestions. Once I provided more specific rules and described the system I wanted to build (like symptom patterns and expected responses), the AI was able to generate more targeted and usable code.
2. Another challenge was understanding how to run and test the code properly. Initially, I tried entering symptoms directly into the terminal without realizing I needed to first run the Python script. The AI helped clarify that the input prompt would only appear once the program was correctly executed using python symptomChecker.py.
