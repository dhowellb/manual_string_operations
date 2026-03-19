# Function na sariling gawa para i-recreate ang .startswith() method
def check_starting_string(target_string, prefix_string):
    # Kunin ang haba ng hinahanap nating salita sa unahan
    prefix_length = len(prefix_string)
    
    # EDGE CASE: Kung mas mahaba yung hinahanap kaysa sa mismong text, imposible mag-match. False agad!
    if prefix_length > len(target_string):
        return False
        
    # Kumuha ng sample sa unahan ng target string gamit ang slicing
    extracted_start = target_string[:prefix_length]
    
    # I-check kung nag-match ba yung kinuha nating sample sa hinahanap na prefix
    if extracted_start == prefix_string:
        return True
        
    # Kung hindi nag-match, ibalik ang False
    return False
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string at yung salitang gusto nating hanapin sa simula
    test_string = "computer engineering"
    target_prefix = "computer"
    
    # Ipasa yung data dun sa custom function at i-save ang True/False na resulta
    is_match = check_starting_string(test_string, target_prefix)
    
    # I-print ang original string at kung nag-match ba yung target prefix
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mStarts with target:\033[0m " + str(is_match))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()