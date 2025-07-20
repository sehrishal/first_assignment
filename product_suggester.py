 # File: product_suggester.py

def suggest_product(user_input):
    # Basic keyword-based logic
    user_input = user_input.lower()

    if "headache" in user_input:
        return {
            "product": "Panadol",
            "reason": "Panadol contains paracetamol, which helps relieve headache pain."
        }
    elif "cold" in user_input:
        return {
            "product": "Disprin Cold+Flu",
            "reason": "It helps relieve symptoms of cold like congestion, runny nose, and body ache."
        }
    elif "stomach" in user_input:
        return {
            "product": "Eno",
            "reason": "Eno gives fast relief from acidity and indigestion."
        }
    elif "allergy" in user_input:
        return {
            "product": "Rigix",
            "reason": "Rigix is an antihistamine that reduces allergy symptoms like sneezing and itching."
        }
    else:
        return {
            "product": "No specific suggestion",
            "reason": "Sorry, I couldn't identify the issue. Please describe your need more clearly."
        }

# Interaction loop
if __name__ == "__main__":
    user_input = input("👤 Describe your need: ")
    suggestion = suggest_product(user_input)
    print(f"💊 Suggested Product: {suggestion['product']}")
    print(f"📝 Reason: {suggestion['reason']}")
