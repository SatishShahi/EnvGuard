import sys
from scanner import CodeScanner
from reporter import SecurityReporter

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"[*] Initializing EnvShield Enterprise Scanner on target: {target}")
    
    scanner = CodeScanner(target)
    findings = scanner.scan_directory()
    
    report = SecurityReporter.generate_report(findings)
    print(report)
    
    # Exit with code 1 if secrets found (useful for CI/CD pipelines & pre-commit hooks)
    if findings:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()