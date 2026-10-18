class SecurityReporter:
    @staticmethod
    def generate_report(findings: list) -> str:
        if not findings:
            return "\n[+] SUCCESS: No exposed secrets or API keys detected. Repository is secure!\n"
            
        report = [
            f"\n[-] CRITICAL SECURITY ALERT: Detected {len(findings)} potential secret(s)!\n" + "="*60
        ]
        
        for idx, f in enumerate(findings, 1):
            report.append(f"  [{idx}] Type: {f['type']}")
            report.append(f"      File: {f['file']} (Line {f['line']})")
            report.append(f"      Code: {f['snippet']}")
            report.append("-" * 60)
            
        report.append("\nAction Required: Revoke these credentials immediately and remove them from history.")
        return "\n".join(report)