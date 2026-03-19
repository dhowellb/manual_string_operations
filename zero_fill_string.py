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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na may negative sign para ma-test yung edge case
    test_string = "-42"
    # Target na kabuuang haba (width) na gusto nating maabot
    pad_width = 6
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = zero_fill_string(test_string, pad_width)
    
    # I-print ang original at yung bagong string na naka-zero fill na
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()