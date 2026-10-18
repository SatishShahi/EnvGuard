import math

class EntropyAnalyzer:
    @staticmethod
    def calculate_shannon_entropy(data: str) -> float:
        """Calculates the Shannon entropy of a string to detect high randomness (secrets)."""
        if not data or len(data) < 8:
            return 0.0
            
        entropy = 0.0
        length = len(data)
        
        # Count frequency of each character
        char_counts = {}
        for char in data:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        for count in char_counts.values():
            probability = float(count) / length
            entropy -= probability * math.log(probability, 2)
            
        return round(entropy, 3)