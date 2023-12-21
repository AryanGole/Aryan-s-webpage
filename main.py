class SymptomChecker:
    def __init__(self):
        self.symptom_database = {
            'Fever': ['high body temperature', 'chills', 'sweating'],
            'Headache': ['pain in head', 'sensitivity to light or noise'],
            'Cough': ['persistent cough', 'phlegm production'],
            'Viral': ['cold', 'cough', 'fever'],
            'Dengue': ['very high fever', 'body ache', 'skin rash'],
            'Acute cholecystitis': ['pain in the upper right abdomen', 'nausea', 'vomiting'],
            'Arthritis': ['joint pain', 'stiffness'],
            'Asthma': ['wheezing when breathing out', 'shortness of breath'],
            'Conjunctivitis': ['redness', 'itching', 'discharge', 'swelling of the eye or the eye lid'],
            'Diarrhea': ['loose', 'watery stools', 'abdominal cramps', 'nausea', 'dehydration'],
        }

    def check_symptoms(self, symptoms):
        possible_conditions = []
        for condition, associated_symptoms in self.symptom_database.items():
            if any(symptom in symptoms for symptom in associated_symptoms):
                possible_conditions.append(condition)
        return possible_conditions

    def get_advice(self, condition):
        advice = {
            'Fever': 'Rest, drink fluids, and consider over-the-counter medication. Consult a doctor if it persists.',
            'Headache': 'Rest in a quiet, dark room. Over-the-counter pain relievers may help.',
            'Cough': 'Stay hydrated and consider over-the-counter cough medicine. Consult a doctor if it persists.',
            'Viral': 'Antiviral medication, self care, maintaining electrolyte balance. Consult doctor if it persists.',
            'Dengue': 'Drinking plenty of water, get plenty of rest, using pain relief. Consult doctor if it persists.',
            'Acute cholecystitis': 'Antibiotics, surgery.',
            'Arthritis': 'Medication to manage symptoms, using stockings.',
            'Asthma': 'Inhalers containing bronchodilators',
            'Conjunctivitis': 'Applying eye cream, resting the eyes. Consult a doctor if it persists.',
            'Diarrhea': 'Antibiotics, rest, drink plenty of fluids. Consult a doctor if it persists.',
        }
        return advice.get(condition, 'Advice not available for this condition.')



# driver code:
if __name__ == "__main__":
    checker = SymptomChecker()

    user_symptoms = input("Enter the symptoms: ").lower()

    possible_conditions = checker.check_symptoms(user_symptoms)

    if possible_conditions:
        for condition in possible_conditions:
            advice = checker.get_advice(condition)
            print(f"The possible condition is: {condition}.\nAdvice: {advice}")
    else:
        print("No matching conditions found.")

"""In this example, we have a basic expert system that can diagnose conditions based on provided symptoms. It is 
important to note that this is a simplified and static example. A real-world expert system in a medical setting would be
much more sophisticated, with a comprehensive knowledge base, advanced inference engine, user interface, and likely
integration with actual medical data."""