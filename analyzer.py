import re
import math

def evaluate_password(password: str) -> dict:
    results = {
        "length": len(password),
        "has_upper": bool(re.search(r'[A-Z]', password)),
        "has_lower": bool(re.search(r'[a-z]', password)),
        "has_digit": bool(re.search(r'\d', password)),
        "has_special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "score": 0,
        "rating": "Weak"
    }

    # Scoring logic
    pool_size = 0
    if results["has_lower"]: pool_size += 26
    if results["has_upper"]: pool_size += 26
    if results["has_digit"]: pool_size += 10
    if results["has_special"]: pool_size += 32

    # Calculate entropy: E = L * log2(pool_size)
    entropy = len(password) * (math.log2(pool_size) if pool_size > 0 else 0)
    results["entropy"] = round(entropy, 2)

    # Determine Rating
    if results["length"] >= 8 and entropy >= 50 and sum([results["has_upper"], results["has_lower"], results["has_digit"], results["has_special"]]) >= 3:
        results["rating"] = "Strong"
        if results["length"] >= 12 and entropy >= 65:
            results["rating"] = "Very Strong"
    elif results["length"] >= 6 and entropy >= 30:
        results["rating"] = "Moderate"

    return results
