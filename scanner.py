import os
from config import ScanConfig
from entropy import EntropyAnalyzer

class CodeScanner:
    def __init__(self, target_dir: str):
        self.target_dir = os.path.abspath(target_dir)

    def scan_directory(self) -> list:
        findings = []
        for root, dirs, files in os.walk(self.target_dir):
            # Prune excluded directories in-place
            dirs[:] = [d for d in dirs if d not in ScanConfig.EXCLUDED_DIRS]
            
            for file in files:
                if any(file.endswith(ext) for ext in ScanConfig.EXCLUDED_EXTENSIONS):
                    continue
                    
                file_path = os.path.join(root, file)
                findings.extend(self._scan_file(file_path))
                
        return findings

    def _scan_file(self, file_path: str) -> list:
        file_findings = []
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line_num, line in enumerate(f, 1):
                    line_stripped = line.strip()
                    
                    # Skip comment lines or empty lines to reduce false positives
                    if line_stripped.startswith(("#", "//", "/*", "*")):
                        continue

                    # 1. Check against known regex patterns
                    for label, pattern in ScanConfig.PATTERNS.items():
                        match = pattern.search(line)
                        if match:
                            file_findings.append({
                                "file": os.path.relpath(file_path, self.target_dir),
                                "line": line_num,
                                "type": label,
                                "snippet": self._mask_secret(line_stripped)
                            })
                            break # One finding per line pattern match is enough
                            
        except Exception as e:
            # Gracefully handle permission errors or locked files
            print(f"[-] Warning: Could not read file {file_path}: {e}")
            
        return file_findings

    @staticmethod
    def _mask_secret(line: str) -> str:
        """Masks out parts of the line for safe logging/reporting."""
        if len(line) > 50:
            return line[:30] + "..." + line[-10:]
        return line