# Function na sariling gawa para gayahin ang .zfill() method (Zero Fill)
def zero_fill_string(target_string, target_width):
    # Kuwentahin kung ilang zeros pa ang kulang
    padding_needed = target_width - len(target_string)
    
    # Kung may kulang pa (greater than 0)...
    if padding_needed > 0:
        # Gumawa ng string na puro "0" na kasing-dami ng kulang
        added_zeros = "0" * padding_needed
        
        # EDGE CASE: Kung may negative (-) o positive (+) sign sa unahan...
        if len(target_string) > 0 and (target_string[0] == "-" or target_string[0] == "+"):
            # Ihiwalay yung sign
            sign_character = target_string[0]
            # Ihiwalay yung mismong number
            number_part = target_string[1:]
            # Pagdikitin: Sign sa unahan + Zeros sa gitna + Number sa dulo
            return sign_character + added_zeros + number_part
            
        # Kung walang sign, idikit lang yung zeros sa unahan ng text
        return added_zeros + target_string
        
    # Kung sobra o sapat na yung haba, ibalik na lang yung original
    return target_string