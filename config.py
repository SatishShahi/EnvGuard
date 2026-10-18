import re

class ScanConfig:
    # High-precision regex patterns for popular API keys and tokens
    PATTERNS = {
        "GitHub Personal Access Token": re.compile(r"ghp_[a-zA-Z0-9]{36}"),
        "GitHub OAuth Access Token": re.compile(r"gho_[a-zA-Z0-9]{36}"),
        "OpenAI API Key": re.compile(r"sk-[a-zA-Z0-9]{48}"),
        "AWS Access Key ID": re.compile(r"AKIA[0-9A-Z]{16}"),
        "Slack Token": re.compile(r"xox[baprs]-[0-9a-zA-Z]{10,48}"),
        "Private SSH Key": re.compile(r"-----BEGIN (RSA|EC|DSA|OPENSSH) PRIVATE KEY-----"),
        "Generic Assignment Secret": re.compile(r"(api[_-]?key|secret[_-]?key|auth[_-]?token|password)['\"]?\s*[:=]\s*['\"]([a-zA-Z0-9-_]{16,64})['\"]", re.IGNORECASE)
    }
    
    # Directories and file extensions to skip
    EXCLUDED_DIRS = {".git", "__pycache__", "venv", "env", "node_modules", "dist", "build"}
    EXCLUDED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip", ".tar", ".gz", ".pyc", ".db"}
    
    # Entropy threshold for string randomness evaluation
    ENTROPY_THRESHOLD = 4.2