# Expert system for diagnosing diseases based on symptoms

responses = {} # Store user responses

def ask(symptom):
    if symptom in responses:
        return responses[symptom]
    
    response = input(f"Does the patient have {symptom.replace('_', ' ')}? (yes/no): ").strip().lower()
    while response not in ['yes', 'no', 'y', 'n']:
        response = input("Please answer with yes or no: ").strip().lower()
    
    is_yes = response in ['yes', 'y']
    responses[symptom] = is_yes
    return is_yes

def diagnose():
    if flu():
        return "Flu"
    elif common_cold():
        return "Common Cold"
    elif covid19():
        return "COVID-19"
    elif food_poisoning():
        return "Food Poisoning"
    elif malaria():
        return "Malaria"
    else:
        return "an Unknown Illness"

# Disease rules
def flu():
    return (
        ask("has_fever") and
        ask("has_body_ache") and
        ask("has_chills") and
        ask("has_sore_throat")
    )

def common_cold():
    return (
        ask("has_runny_nose") and
        ask("has_sneezing") and
        ask("has_sore_throat")
    )

def covid19():
    return (
        ask("has_fever") and
        ask("has_dry_cough") and
        ask("has_loss_of_taste_or_smell") and
        ask("has_difficulty_breathing")
    )

def food_poisoning():
    return (
        ask("has_nausea") and
        ask("has_vomiting") and
        ask("has_diarrhea") and
        ask("has_stomach_pain")
    )

def malaria():
    return (
        ask("has_fever") and
        ask("has_chills") and
        ask("has_sweating") and
        ask("has_headache")
    )


print("=== Medical Diagnosis Expert System ===")
diagnosis = diagnose()
print("\nDiagnosis: The patient might be suffering from", diagnosis)

# Output:

'''
=== Medical Diagnosis Expert System ===
Does the patient have has fever? (yes/no): y
Does the patient have has body ache? (yes/no): y
Does the patient have has chills? (yes/no): y
Does the patient have has sore throat? (yes/no): n
Does the patient have has runny nose? (yes/no): y
Does the patient have has sneezing? (yes/no): y
Does the patient have has dry cough? (yes/no): y
Does the patient have has loss of taste or smell? (yes/no): y
Does the patient have has difficulty breathing? (yes/no): y

Diagnosis: The patient might be suffering from COVID-19
'''