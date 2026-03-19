# Function na sariling gawa para i-recreate ang .upper() method
def convert_all_upper(target_string):
    # Reference lists para sa alphabet
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Dito natin iipunin yung final na salita
    result_string = ""
    
    # Isa-isang i-check ang bawat character sa ita-type na string
    for character in target_string:
        # Kung yung character ay nasa listahan ng maliliit na letra...
        if character in lower_letters:
            # Hanapin natin kung pang-ilan siya sa alphabet (0 to 25)
            for i in range(26):
                if lower_letters[i] == character:
                    # Idagdag yung katumbas niyang malaking letra sa final string natin
                    result_string = result_string + upper_letters[i]
        else:
            # Kung space, number, o malaking letra na siya, kopyahin na lang as is
            result_string = result_string + character
            
    return result_string