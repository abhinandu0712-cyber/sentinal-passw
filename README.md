# 🛡️ SentinelPass — Password Security Analyzer

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![UI](https://img.shields.io/badge/UI-CustomTkinter-00D4FF)](https://customtkinter.tomschimansky.com/)
[![Analysis](https://img.shields.io/badge/Analysis-zxcvbn-7C3AED)](https://github.com/dropbox/zxcvbn)
[![Tests](https://img.shields.io/badge/Tests-pytest-0A9EDC)](https://pytest.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A local-first desktop password analyzer** with a modern dark interface, actionable feedback, and a cryptographically secure password generator.

> SentinelPass is an educational portfolio project. It does not crack passwords, verify them against breached-password databases, or guarantee account security.

## Features

- zxcvbn password-strength estimation (score 0–4)
- Strength meter, crack-time category, character groups, and local heuristic checks
- Recommendations informed by zxcvbn feedback and detected patterns
- Secure local password generator powered by Python's `secrets` module
- Dark CustomTkinter interface with no remote images or API calls
- Automated unit tests using pytest
- No password history, file storage, analytics, or network requests

## Screenshots

Screenshots have not been included yet. Add your own captures after running the application.

| Main dashboard | Generator |
|---|---|
| `docs/screenshots/dashboard.png` *(placeholder)* | `docs/screenshots/generator.png` *(placeholder)* |

Create the folder and save screenshots there if you want to use the paths above.

## Technology stack

- Python 3.10+
- CustomTkinter — desktop UI
- zxcvbn — password-strength estimation
- Python standard library (`secrets`, `string`, `re`, `math`)
- pytest — tests

## Project structure

```text
SentinelPass/
├── main.py
├── ui/
│   ├── __init__.py
│   └── main_window.py
├── security/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── recommendations.py
│   └── password_generator.py
├── tests/
│   ├── __init__.py
│   ├── test_analyzer.py
│   └── test_generator.py
├── assets/
│   └── README.md
├── docs/
│   └── screenshots/        # create when capturing screenshots
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### Windows (PowerShell)

```powershell
cd SentinelPass
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

If PowerShell blocks activation, you can use the virtual environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

### Linux

Install Python 3, `venv`, and Tk support using your distribution's package manager if needed. For Debian/Ubuntu:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-tk
cd SentinelPass
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

A graphical desktop session is required. A headless terminal/SSH session without a display cannot open the desktop window.

## Run the tests

With the virtual environment active:

```bash
python -m pytest -q
```

The tests use illustrative sample strings only. Do not reuse sample passwords for real accounts.

## How the strength score works

SentinelPass uses **zxcvbn as the primary assessment**, which considers common passwords, recognizable patterns, and other guessability signals. Its score maps directly to the five displayed labels:

| zxcvbn score | Display label |
|---:|---|
| 0 | Very Weak |
| 1 | Weak |
| 2 | Fair |
| 3 | Strong |
| 4 | Very Strong |

This mapping is a UI label, not a guarantee that a password is safe. Estimates depend on context, attacker knowledge, password reuse, service protections, and the attack scenario.

The displayed crack-time estimate uses zxcvbn's `offline_slow_hashing_1e4_per_second` scenario. It is an explanatory model, **not a measured cracking attempt**. The analyzer also reports a rough character-set entropy estimate; that estimate assumes independent, uniformly random characters and can substantially overstate human-chosen password entropy.

Additional checks flag short length, recognizable sequence strings, adjacent repeated characters, and low character variety. These checks supplement zxcvbn and do not override its score.

## Security and privacy design

- Password analysis runs locally through Python libraries.
- The app contains no HTTP client, telemetry, analytics, or breach-checking integration.
- Password values are not written to files, settings, logs, or test reports by application code.
- The analysis result excludes the password itself.
- Reset clears the input and generated-password fields.
- Password generation uses `secrets`, not `random`.
- Copying a generated password puts it on the system clipboard, which may be visible to other applications. Use the copy feature deliberately.

**Privacy note:** local processing reduces exposure, but the Python runtime, operating system, clipboard, screen capture, and other software on the device remain outside this app's control. Avoid testing with a password currently used for an important account.

## Limitations

- zxcvbn estimates guessability; it cannot know every password, attacker, or service-specific policy.
- The sequence and repetition checks are intentionally simple and may miss patterns or flag harmless ones.
- The entropy figure is a rough educational estimate, not a security proof.
- No breached-password database is queried.
- The UI requires a graphical desktop and a working Tk environment.
- A generated password is not automatically saved. If you copy it, clipboard exposure is possible.

## Learning outcomes

- Building a modular Python desktop application
- Applying password-strength estimation responsibly
- Separating presentation, analysis, recommendations, and generation logic
- Using `secrets` for security-sensitive randomness
- Writing unit tests with pytest
- Applying privacy-by-design principles and documenting limitations

## Future improvements

- More comprehensive local pattern checks with transparent rules
- Accessibility and keyboard-navigation review
- Additional UI automation tests on Windows and Linux
- Optional integration with a carefully designed privacy-preserving breach-check workflow, disabled by default
- Packaging as an installable desktop application

## Responsible use

Use SentinelPass for education and to evaluate passwords you are permitted to test. Do not use it to collect, store, or inspect other people's credentials. Never submit real passwords to public websites or issue trackers.

## License

Released under the [MIT License](LICENSE).
