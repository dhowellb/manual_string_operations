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
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na naka-lowercase
    test_string = "python programming"
    
    # Ipasa yung string sa custom function natin para ma-convert
    result_string = convert_all_upper(test_string)
    
    # I-print ang pinagkaiba ng original at yung naka-all caps na string
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()