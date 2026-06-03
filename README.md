# 🔐 Encryption Terminal

![Python](https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)
![No Dependencies](https://img.shields.io/badge/dependencies-none-success?style=flat-square)
![CLI](https://img.shields.io/badge/interface-terminal-black?style=flat-square)

> A modular, terminal-based encryption system built in Python — with user authentication, classical cipher operations, and persistent operation history. Built while learning cryptography and CLI architecture from scratch.

---

## Why this project exists

Most encryption tutorials stop at the algorithm. This project goes further: it wraps the ciphers inside a real system with auth, persistent storage, session handling, and a navigable terminal UI — the kind of structure you'd actually find in a small production tool.

The goal wasn't just to implement Caesar or Vigenère. It was to practice building something modular, where each component has a clear responsibility and can be changed without breaking everything else.

---

## Demo

```
══════════════════════════════════════════════════
═══════════════ ENCRYPTION ═══════════════════════
══════════════════════════════════════════════════
Register............................................[1]
Login...............................................[2]
Exit................................................[3]
══════════════════════════════════════════════════
Choose an option: 2

══════════════════════════════════════════════════
═══════════════════ LOGIN ════════════════════════
══════════════════════════════════════════════════
Username: lucas
Password: ****
✔ Login successful!

══════════════════════════════════════════════════
═══════════════ CRYPTO MENU ══════════════════════
══════════════════════════════════════════════════
Encrypt.............................................[1]
Decrypt.............................................[2]
History.............................................[3]
Back................................................[4]
══════════════════════════════════════════════════
Choose an option: 1

Text: Hello World
Key (number): 3
→ Khoor Zruog
```

---

## Features

- **User Authentication** — Register and log in; credentials persisted in JSON
- **Caesar Cipher** — Encrypt/decrypt with a numeric shift key
- **Vigenère Cipher** — Polyalphabetic cipher using a keyword
- **ROT13** — Symmetric cipher; no key required
- **Operation History** — Every operation is logged with input, output, key, and timestamp
- **Colored Terminal UI** — ANSI-colored, menu-driven interface with case-preserving cipher output
- **Modular Architecture** — Six focused modules; zero cross-contamination of concerns

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Data Storage | JSON (flat-file) |
| UI | Terminal / ANSI escape codes |
| Standard Library | `os`, `json`, `pathlib`, `datetime` |
| External dependencies | None |

---

## Project Structure

```
encryption-project/
├── main.py                  # Entry point — top-level navigation loop
├── modules/
│   ├── __init__.py
│   ├── auth.py              # Registration and login logic
│   ├── crypto.py            # Cipher algorithms + cipher sub-menus
│   ├── history.py           # Log read/write and display
│   ├── menu.py              # Menu rendering, input handling, formatting helpers
│   └── utils.py             # Color output, screen clear, separator lines
└── data/
    ├── users.json           # Persisted user accounts
    └── logs.json            # Persisted operation history
```

**Data flow:**

```
main.py
  └─► menu.py       — renders main menu, reads user input
  └─► auth.py       — validates credentials against users.json
        └─► crypto.py  — cipher sub-menus + algorithm calls
              └─► history.py — writes records to logs.json
```

Each module imports only what it needs. No globals, no shared state — just clean function calls across a flat module tree.

---

## Installation

No dependencies to install. Python 3.10+ is all you need.

```bash
git clone https://github.com/yaakz007/encryption-terminal.git
cd encryption-terminal
python main.py
```

> **Windows note:** ANSI colors require Windows 10 v1511 or later. Most modern terminals (Windows Terminal, VS Code) support them by default.

---

## Usage

### Register

```
Select [1] → enter username (min 3 chars) + password (min 4 chars)
```

### Login and encrypt

```
Select [2] → login → Crypto Menu → Encrypt → choose cipher → enter text + key
```

### Supported ciphers

| Cipher | Key Type | Notes |
|---|---|---|
| Caesar | Integer (shift amount) | Preserves case, passes non-alpha |
| Vigenère | String (keyword) | Polyalphabetic; key cycles over text |
| ROT13 | None | Symmetric — same function encrypts and decrypts |

### View history

```
Crypto Menu → [3] History
```

Displays all past operations with full context:

```
═══════════════════════════════════
User:      lucas
Cipher:    vigenere
Operation: encrypt
Input:     Hello World
Output:    Zincd Pgvnu
Key:       secret
Date:      2026-06-03 19:01:45
```

---

## Future Improvements

- **Password hashing** — Passwords are currently stored in plaintext. Using `hashlib.pbkdf2_hmac` or `bcrypt` is the most important next step.
- **Input masking** — Replace `input()` for passwords with `getpass.getpass()` to hide typed characters.
- **Per-user history** — The log currently shows all operations from all users. Filtering by the logged-in user is a privacy and UX improvement.
- **Input validation** — Caesar/Vigenère key inputs don't guard against non-numeric or empty input; unhandled exceptions can crash the session.
- **CLI arguments** — Flag-based interface (`--cipher caesar --key 3 --text "hello"`) would make the tool scriptable and pipeline-friendly.
- **Export history** — Allow saving the operation log to `.txt` or `.csv`.
- **More ciphers** — Atbash, Rail Fence, or XOR would slot cleanly into the existing module pattern.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
