# EnvGuard

**EnvGuard** is a lightweight, zero-dependency Python security utility designed to scan codebases, project directories, and configuration files for accidentally leaked API keys, credentials, and high-entropy secrets before they can be committed to version control.



## Features

* **High-Precision Signatures:** Pre-configured regex patterns to detect popular service credentials (GitHub PATs/OAuth tokens, OpenAI keys, AWS Access Keys, Slack tokens, and private SSH keys).
* **Smart Filtering:** Automatically ignores non-source binary files, images, build directories (`dist`, `build`, `node_modules`), and version control metadata (`.git`).
* **False-Positive Reduction:** Skips comment lines (`#`, `//`) and documentation blocks to prevent noise from example configuration files.
* **CI/CD Ready:** Returns explicit exit codes (`0` for clean, `1` if secrets are detected) to integrate seamlessly into automated workflows and pre-commit hooks.



## Project Architecture


EnvGuard/
│
├── config.py       # Secret signatures, regex patterns, and ignore rules
├── entropy.py      # Shannon entropy analysis engine for string randomness
├── scanner.py      # Core file traversal, filtering, and pattern-matching logic
├── reporter.py     # Formatter for critical security alerts and audit reports
└── guard.py        # CLI entry point and exit-code handler


## Installation & Setup
Clone or copy the project files into your local directory.

Ensure you have Python 3.8+ installed. No external pip dependencies are required.

How to Use
Run the security scanner from your terminal by pointing it to any target directory or repository path.

1. Scan the Current Directory
If you are already inside the directory you want to audit:

## Bash
python guard.py
2. Scan a Specific Repository or Path
Pass any target folder path as a command-line argument:

## Bash
python guard.py /path/to/your/target/repository
Example Outputs
Secure State
Plaintext
[*] Initializing EnvGuard Enterprise Scanner on target: guard.py /path/to/your/target/repository

[+] SUCCESS: No exposed secrets or API keys detected. Repository is secure!
Alert State
If exposed keys are discovered, EnvGuard lists the file paths, line numbers, and credential types, and terminates with an error code to block unsafe deployments:

Plaintext
[-] CRITICAL SECURITY ALERT: Detected 1 potential secret(s)!
============================================================
  [1] Type: OpenAI API Key
      File: config.py (Line 14)
      Code: OPENAI_API_KEY = "sk-..."
------------------------------------------------------------
Action Required: Revoke these credentials immediately and remove them from history.

## Version & Roadmap
Current Release: v1.0.0
Core Scanner: Static pattern matching via regular expressions and Shannon entropy calculation.

Architecture: Modular 5-file Python structure with zero external dependencies.

Interface: Command-line interface with automated CI/CD exit codes.

## License
This project is open-source and available under the MIT License.