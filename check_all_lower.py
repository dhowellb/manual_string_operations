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