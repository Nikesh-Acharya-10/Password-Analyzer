from analyzer import evaluate_password

def run():
    print("=" * 45)
    print("         ANAYALAZER PASSWORD ANALYZER         ")
    print("=" * 45)
    
    pwd = input("Enter a password to evaluate: ").strip()
    if not pwd:
        print("Error: Password cannot be empty.")
        return

    res = evaluate_password(pwd)

    print("\n--- ANALYSIS RESULTS ---")
    print(f"[*] Length:             {res['length']} characters")
    print(f"[*] Uppercase:          {'Yes' if res['has_upper'] else 'No'}")
    print(f"[*] Lowercase:          {'Yes' if res['has_lower'] else 'No'}")
    print(f"[*] Numbers:            {'Yes' if res['has_digit'] else 'No'}")
    print(f"[*] Special Characters: {'Yes' if res['has_special'] else 'No'}")
    print(f"[*] Estimated Entropy:  {res['entropy']} bits")
    print(f"[*] Strength Rating:    {res['rating']}")
    print("=" * 45)

if __name__ == "__main__":
    run()
