import re
import math

COMMON_PASSWORDS = {"password", "123456", "12345678", "qwerty", "admin", "welcome", "password123"}

def get_time_to_crack(entropy: float) -> str:
    guesses = 2 ** entropy
    seconds = guesses / 10_000_000_000
    
    if seconds < 1:
        return "Instantly"
    elif seconds < 60:
        return f"{int(seconds)} seconds"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours"
    elif seconds < 31536000:
        return f"{int(seconds / 86400)} days"
    elif seconds < 3153600000:
        return f"{int(seconds / 31536000)} years"
    else:
        return "Centuries+"

def evaluate_password(password: str) -> dict:
    suggestions = []
    
    results = {
        "length": len(password),
        "has_upper": bool(re.search(r'[A-Z]', password)),
        "has_lower": bool(re.search(r'[a-z]', password)),
        "has_digit": bool(re.search(r'\d', password)),
        "has_special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        "is_common": password.lower() in COMMON_PASSWORDS,
        "rating": "Weak"
    }

    # Generate suggestions
    if results["length"] < 12:
        suggestions.append(f"Make it longer (currently {results['length']} chars; aim for 12+).")
    if not results["has_upper"]:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not results["has_lower"]:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not results["has_digit"]:
        suggestions.append("Add at least one number (0-9).")
    if not results["has_special"]:
        suggestions.append("Add at least one special character (!@#$...).")
    if results["is_common"]:
        suggestions.append("CRITICAL: This is a widely leaked/common password. Avoid using it.")

    # Calculate entropy
    pool_size = 0
    if results["has_lower"]: pool_size += 26
    if results["has_upper"]: pool_size += 26
    if results["has_digit"]: pool_size += 10
    if results["has_special"]: pool_size += 32

    entropy = len(password) * (math.log2(pool_size) if pool_size > 0 else 0)
    results["entropy"] = round(entropy, 2)
    results["crack_time"] = get_time_to_crack(entropy)
    results["suggestions"] = suggestions

    # Strict Strength Rating Logic
    # 1. Must have NO missing requirements (len(suggestions) == 0) to be Strong or Very Strong
    if results["is_common"]:
        results["rating"] = "Very Weak"
    elif len(suggestions) == 0 and results["length"] >= 14 and entropy >= 75:
        results["rating"] = "Very Strong"
    elif len(suggestions) == 0 and entropy >= 60:
        results["rating"] = "Strong"
    elif results["length"] >= 8 and sum([results["has_upper"], results["has_lower"], results["has_digit"], results["has_special"]]) >= 3:
        results["rating"] = "Moderate"
    else:
        results["rating"] = "Weak"

    return results
