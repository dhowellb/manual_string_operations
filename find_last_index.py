# Function na sariling gawa para gayahin ang .rfind() method (hanapin ang huling index)
def find_last_index(target_string, substring_target):
    # Kunin ang haba nung salitang gusto nating hanapin
    substring_length = len(substring_target)
    
    # Mag-set ng default value na -1 (ibig sabihin, hindi pa nahahanap)
    last_found_index = -1
    
    # EDGE CASE: Kapag empty string ang hinahanap, ibalik ang pinakadulo (length ng string)
    if substring_length == 0:
        return len(target_string)
        
    # Gumamit ng sliding window para silipin ang buong text mula simula hanggang dulo
    for i in range(len(target_string) - substring_length + 1):
        extracted_part = target_string[i:i + substring_length]
        
        # Kapag nag-match, i-save yung index. Dahil tuloy-tuloy ang loop, 
        # mao-overwrite ito kapag may nahanap pang iba sa unahan!
        if extracted_part == substring_target:
            last_found_index = i
            
    # Pagkatapos ng buong loop, kung -1 pa rin, ibig sabihin walang nahanap
    if last_found_index == -1:
        return "substring not found"
        
    # Ibalik kung saan huling nakita
    return last_found_index
# Function para i-test at patakbuhin yung ginawa nating logic sa taas
def main_execution():
    # Mag-set ng test string at yung letrang gusto nating hanapin
    test_string = "banana"
    target_substring = "a"
    
    # Ipasa yung data dun sa custom function at i-save ang huling index na nahanap
    last_index = find_last_index(test_string, target_substring)
    
    # I-print ang original string at kung saang index siya huling lumabas
    print("\033[96mString:\033[0m '" + test_string + "'")
    print("\033[92mLast index of target:\033[0m " + str(last_index))

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    main_execution()