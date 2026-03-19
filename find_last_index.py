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