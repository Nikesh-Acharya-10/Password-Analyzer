# AnayaLazer: Password Strength & Complexity Analyzer

**AnayaLazer** is a lightweight Python command-line utility designed to evaluate the strength and security of user passwords. It checks passwords against key security parameters—such as length, character diversity, and common password patterns—and provides actionable feedback to improve credential security.

---

## Features

* **Length Verification:** Ensures passwords meet minimum security thresholds (8+ characters recommended).
* **Character Diversity Analysis:** Checks for uppercase letters, lowercase letters, numbers, and special symbols.
* **Common Pattern Detection:** Identifies predictable patterns, repeated characters, or common words (e.g., `123456`, `password`).
* **Entropy & Strength Scoring:** Calculates a real-time security score ranging from *Weak* to *Very Strong*.
* **Actionable Feedback:** Provides specific recommendations to strengthen weak passwords.

---

## Prerequisites

* **Python 3.8+** installed on your system.

To verify your installation:
  ```bash
    python --version
```
Installation & Setup
Clone the Repository:
```bash
git clone [https://github.com/your-username/anayalazer.git](https://github.com/your-username/anayalazer.git)
cd anayalazer
```
Set Up a Virtual Environment (Optional, Recommended):
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/venv/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```
Install Dependencies:
```bash
pip install -r requirements.txt
```
Usage
Run the script from your terminal:
```Bash
python main.py
```
Example Input/Output
```
Input:

Enter password to analyze: P@ssw0rd2026!
Output:

==================================================
                 ANAYALAZER REPORT                
==================================================
[+] Length:              12 characters (Good)
[+] Uppercase Letters:   Present (1)
[+] Lowercase Letters:   Present (6)
[+] Numbers:             Present (4)
[+] Special Characters:  Present (2)
--------------------------------------------------
Overall Rating:          VERY STRONG
Estimated Entropy:       ~68.4 bits
Status:                  Passes standard security policies.
==================================================
```
