# Function na sariling gawa para gayahin ang .count() method
def count_substring_occurrence(target_string, substring_target):
    # Kunin ang haba nung salitang gusto nating hanapin at bilangin
    substring_length = len(substring_target)
    occurrence_count = 0
    
    # EDGE CASE: Ayon sa rules ng Python, kapag empty string ("") ang hinahanap,
    # ang sagot ay palaging length ng string + 1.
    if substring_length == 0:
        return len(target_string) + 1
        
    # Gumamit ng "sliding window" para silipin ang bawat part ng string.
    # Uusog tayo mula simula hanggang sa pinakadulo kung saan kasya pa yung hinahanap natin.
    for i in range(len(target_string) - substring_length + 1):
        # Kumuha ng sample (slice) na kasing-haba nung hinahanap natin
        extracted_part = target_string[i:i + substring_length]
        
        # Kung nag-match yung nakuha nating sample sa mismong target...
        if extracted_part == substring_target:
            # Dagdagan natin ng isa yung counter natin
            occurrence_count = occurrence_count + 1
            
    return occurrence_count