# Function na sariling gawa para gayahin ang .rjust() method (Right Justify)
def right_justify_string(target_string, target_width):
    # Kuwentahin kung ilang spaces pa ang kulang para maabot ang target width
    padding_needed = target_width - len(target_string)
    
    # Kung may kulang pa na spaces (greater than 0)...
    if padding_needed > 0:
        # Gumawa ng string na puro spaces na kasing-dami ng kulang
        added_spaces = " " * padding_needed
        # Idikit yung spaces sa KALIWA ng original na salita para umurong siya pakanan
        return added_spaces + target_string
        
    # Kung sobra o sapat na yung haba ng salita, ibalik na lang yung original
    return target_string