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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string at yung part na gusto nating bilangin
    test_string = "banana"
    target_substring = "na"
    
    # Ipasa yung data dun sa custom function at i-save ang final count
    total_count = count_substring_occurrence(test_string, target_substring)
    
    # I-print ang original string at kung ilang beses nakita yung target
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mCount of target:\033[0m " + str(total_count))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()