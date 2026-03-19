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