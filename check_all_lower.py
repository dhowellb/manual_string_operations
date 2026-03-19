# Function na sariling gawa para i-recreate ang .islower() method
def check_all_lower(target_string):
    # Reference lists para sa malalaki at maliliit na letra
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Tracker kung may nahanap tayong kahit isang maliit na letra (default ay False)
    has_lower_letter = False
    
    # Isa-isang i-check ang bawat character sa string
    for character in target_string:
        # Kung may nakitang malaking letra, ibig sabihin hindi lahat lowercase. I-return agad ang False!
        if character in upper_letters:
            return False
            
        # Kung maliit na letra ito, i-update yung tracker natin to True
        if character in lower_letters:
            has_lower_letter = True
            
    # I-return ang True kung may nakitang lowercase at walang nakitang uppercase.
    # I-return ang False kung puro numbers/symbols lang at walang letters.
    return has_lower_letter
# Function para i-test kung gumagana yung custom logic natin sa taas
def main_execution():
    # Mag-set ng test string na puro lowercase at may symbol (_)
    test_string = "snake_case_only"
    
    # Ipasa yung string dun sa function at i-save ang True/False na sagot
    is_valid_lower = check_all_lower(test_string)
    
    # I-print ang string at kung True o False ba na naka-lowercase lahat ng letters niya
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mIs Lower:\033[0m " + str(is_valid_lower))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()