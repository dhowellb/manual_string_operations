# Function na sariling gawa para gayahin ang .find() method
def find_first_index(target_string, substring_target):
    # Kunin ang haba nung salitang gusto nating hanapin
    substring_length = len(substring_target)
    
    # EDGE CASE: Kapag walang nilagay na hahanapin (empty string), ibalik agad ang index 0
    if substring_length == 0:
        return 0
        
    # Gumamit ulit ng "sliding window" para silipin ang bawat part ng string
    for i in range(len(target_string) - substring_length + 1):
        # Kumuha ng sample (slice) na kasing-haba nung hinahanap natin
        extracted_part = target_string[i:i + substring_length]
        
        # Kung nag-match yung sample sa mismong target...
        if extracted_part == substring_target:
            # I-return agad kung pang-ilang index siya nahanap (hihinto na agad ang loop!)
            return i
            
    # Kung natapos ang buong loop at walang nag-match, sabihing hindi nahanap
    return "substring not found"