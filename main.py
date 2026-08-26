import sys
import secrets
import string
import datetime
from analyzer import evaluate_password

def generate_strong_password(length: int = 16) -> str:
    """Generates a cryptographically strong random password."""
    # Pool includes letters, numbers, and special symbols
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def get_status_str(check: bool) -> str:
    return "Yes" if check else "No"

def save_report_to_file(res: dict, suggested_pwd: str = None, filename: str = "password_report.txt"):
    """Writes the password analysis results to a clean text file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report_content = f"""==================================================
              ANAYALAZER SECURITY REPORT          
==================================================
Generated On:           {timestamp}
Length:                 {res['length']} characters
Uppercase Present:      {'Yes' if res['has_upper'] else 'No'}
Lowercase Present:      {'Yes' if res['has_lower'] else 'No'}
Numbers Present:        {'Yes' if res['has_digit'] else 'No'}
Special Chars Present:  {'Yes' if res['has_special'] else 'No'}
Common/Leaked Password: {'YES (DANGER)' if res['is_common'] else 'No'}
--------------------------------------------------
Estimated Entropy:      {res['entropy']} bits
Crack Time (Est.):      {res['crack_time']}
Overall Strength:       {res['rating']}
==================================================
SUGGESTIONS FOR IMPROVEMENT:
"""
    if res['suggestions']:
        for s in res['suggestions']:
            report_content += f"- {s}\n"
    else:
        report_content += "- None! Password meets core security standards.\n"

    if suggested_pwd:
        report_content += f"\nSUGGESTED STRONG PASSWORD:\n{suggested_pwd}\n"

    report_content += "==================================================\n"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"\n[+] Success: Report exported to '{filename}'")
    except IOError as e:
        print(f"\n[!] Failed to save report: {e}")

def run():
    print("=" * 50)
    print("         ANAYALAZER PASSWORD ANALYZER         ")
    print("=" * 50)
    
    pwd = input("Enter a password to evaluate: ").strip()
    if not pwd:
        print("\n[!] Error: Password cannot be empty.")
        return

    res = evaluate_password(pwd)

    print("\n--- ANALYSIS RESULTS ---")
    print(f"[*] Length:             {res['length']} characters")
    print(f"[*] Uppercase:          {get_status_str(res['has_upper'])}")
    print(f"[*] Lowercase:          {get_status_str(res['has_lower'])}")
    print(f"[*] Numbers:            {get_status_str(res['has_digit'])}")
    print(f"[*] Special Characters: {get_status_str(res['has_special'])}")
    
    is_common_str = "YES (In Common List)" if res['is_common'] else "No"
    print(f"[*] Known Leaked:       {is_common_str}")
    
    print(f"[*] Estimated Entropy:  {res['entropy']} bits")
    print(f"[*] Time to Crack:      {res['crack_time']}")
    print(f"[*] Strength Rating:    {res['rating']}")

    if res['suggestions']:
        print("\n[!] Recommendations:")
        for s in res['suggestions']:
            print(f"    - {s}")

    # Generate a strong password replacement if weak
    suggested_pwd = None
    if res['rating'] in ["Weak", "Very Weak", "Moderate"]:
        suggested_pwd = generate_strong_password(16)
        print("\n" + "-" * 50)
        print(f"[+] Suggested Strong Password: {suggested_pwd}")
        print("-" * 50)

    print("=" * 50)

    # Prompt user to save report
    choice = input("\nWould you like to save this report to a text file? (y/n): ").strip().lower()
    if choice in ['y', 'yes']:
        save_report_to_file(res, suggested_pwd)

if __name__ == "__main__":
    run()
