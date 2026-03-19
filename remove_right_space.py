# Function na sariling gawa para tanggalin ang spaces sa kanan (custom .rstrip)
def remove_right_space(target_string):
    # Simulan ang index sa pinakadulo ng string
    last_index = len(target_string) - 1
    
    # Habang hindi pa tayo umaabot sa unahan (>= 0) AT space (" ") ang nakikita natin...
    while last_index >= 0 and target_string[last_index] == " ":
        # Umatras tayo ng isang hakbang pakaliwa
        last_index = last_index - 1
        
    # I-return yung string mula simula hanggang dun sa huling hindi-space na character
    # Nilagyan ng + 1 para masama yung mismong huling character sa slice
    return target_string[:last_index + 1]
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string na may spaces sa dulo
    test_string = "hello world   "
    
    # Ipasa yung data dun sa custom function at i-save ang resulta
    result_string = remove_right_space(test_string)
    
    # I-print ang original at yung bagong string (gamit ang single quotes para makita ang spaces)
    print("\033[96mOriginal:\033[0m '" + test_string + "'")
    print("\033[92mResult:\033[0m   '" + result_string + "'")

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()