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