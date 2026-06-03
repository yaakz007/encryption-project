# encryption-project
 A Python encryption project built while learning programming.
🔐 Encryption Terminal
A modular, terminal-based encryption system built in Python. Supports user authentication, classical cipher operations (Caesar, Vigenère, ROT13), and persistent operation history — all through a clean, color-coded CLI interface.

Features

User Authentication — Register and log in with username/password stored in JSON
Caesar Cipher — Encrypt and decrypt text with a numeric shift key
Vigenère Cipher — Encrypt and decrypt text with a keyword-based polyalphabetic cipher
ROT13 — One-command symmetric cipher (no key required)
Operation History — All cipher operations are logged with input, output, key, and timestamp
Colored Terminal UI — ANSI-colored, menu-driven interface with clear screen navigation
Modular Architecture — Clean separation into auth, crypto, history, utils, and menu modules


Tech Stack
LayerTechnologyLanguagePython 3.10+Data StorageJSON (flat-file)UITerminal / ANSI escape codesStandard Libraryos, json, pathlib, datetimeNo third-party dependencies✅

Architecture
encryption-project/
├── main.py                  # Entry point — top-level navigation loop
├── modules/
│   ├── __init__.py
│   ├── auth.py              # Registration and login logic
│   ├── crypto.py            # Cipher algorithms + cipher sub-menus
│   ├── history.py           # Log read/write and display
│   ├── menu.py              # Menu rendering, option input, formatting helpers
│   └── utils.py             # Color output, screen clear, separator lines
└── data/
    ├── users.json           # Persisted user accounts
    └── logs.json            # Persisted operation history
Data flow:
main.py
  └─► menu.py       — renders main menu, reads user input
  └─► auth.py       — validates credentials against users.json
        └─► crypto.py  — cipher sub-menus; calls algorithms
              └─► history.py — writes operation records to logs.json
Each module imports only what it needs, keeping coupling low and making individual components easy to test or replace.

Installation
No external dependencies are required. Python 3.10 or later is sufficient.
bashgit clone https://github.com/yaakz007/encryption-terminal.git
cd encryption-terminal
python main.py

On Windows, ANSI color codes require Windows 10 version 1511 or later (most terminals support them by default).


Usage
1. Launch the program
bashpython main.py
2. Main menu
══════════════════════════════════════════════════
═══════════════ ENCRYPTION ═══════════════════════
══════════════════════════════════════════════════
Register............................................[1]
Login...............................................[2]
Exit................................................[3]
══════════════════════════════════════════════════
3. Register an account
Select [1], then enter a username (minimum 3 characters) and a password (minimum 4 characters).
4. Log in and use the crypto menu
Select [2], provide your credentials, and you'll be taken to:
══════════════════════════════════════════════════
═══════════════ CRYPTO MENU ══════════════════════
══════════════════════════════════════════════════
Encrypt.............................................[1]
Decrypt.............................................[2]
History.............................................[3]
Back................................................[4]
══════════════════════════════════════════════════
5. Encrypt a message (example: Caesar)
Choose cipher: 1 (Caesar)
Text: Hello World
Key (number): 3
Result: Khoor Zruog
6. View history
Select [3] from the Crypto Menu to see all past operations:
═══════════════════════════════════
User:      Lucas
Cipher:    caesar
Operation: encrypt
Input:     Hello World
Output:    Khoor Zruog
Key:       3
Date:      2026-06-03 19:01:45

Supported Ciphers
CipherKey TypeSymmetricCaesarInteger (shift)No (use decrypt)VigenèreString (keyword)No (use decrypt)ROT13NoneYes (encrypt = decrypt)

Future Improvements

Password hashing — Passwords are currently stored in plaintext. Replacing with bcrypt or hashlib (PBKDF2) is the most critical security improvement.
Per-user history — The history log is global; filtering or isolating logs by the authenticated user would improve privacy.
Input masking — Use getpass.getpass() to hide passwords during input.
.gitignore for data/ — users.json and logs.json contain sensitive data and should not be committed to version control.
Configurable option range — The option() function in menu.py hardcodes the valid range as 1–4, which breaks when menus have fewer options. Making it dynamic would improve reliability.
CLI arguments — Supporting flags like --encrypt --cipher caesar --key 3 --text "hello" would make the tool scriptable.
Export history — Allow exporting logs to .txt or .csv.
More ciphers — Atbash, Rail Fence, or XOR could be added following the existing module pattern.


License
This project is licensed under the MIT License. See LICENSE for details.
