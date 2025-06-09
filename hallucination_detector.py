from trusted_symptom_disease import trusted_dict

def check_for_hallucination(symptoms, gpt_diagnosis):
    matched = []
    hallucinated = []
    logs = []
    total_checks = 0
    total_matches = 0

    for symptom in symptoms:
        trusted_diseases = trusted_dict.get(symptom.lower(), [])
        for disease in gpt_diagnosis:
            total_checks += 1
            if disease.lower() in trusted_diseases:
                total_matches += 1
                matched.append(disease)
                logs.append(f"✔ Matched: '{disease}' is valid for symptom '{symptom}'")
            else:
                hallucinated.append(disease)
                logs.append(f"⚠ Possible Hallucination: '{disease}' is not listed for symptom '{symptom}'")

    score = (total_matches / total_checks) * 100 if total_checks > 0 else 0

    return {
        "matched": list(set(matched)),
        "hallucinated": list(set(hallucinated)),
        "logs": logs,
        "score": round(score, 2)
    }
