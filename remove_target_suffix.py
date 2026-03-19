# Function na sariling gawa para tanggalin ang specific na suffix sa dulo ng text
def remove_target_suffix(target_string, suffix_string):
    # Kunin ang haba ng salitang gusto nating tanggalin sa dulo
    suffix_length = len(suffix_string)
    
    # EDGE CASE: Kung walang nilagay na tatanggalin (length is 0), ibalik agad yung original na string
    if suffix_length == 0:
        return target_string
        
    # Kumuha ng sample sa pinakadulo ng string gamit ang negative slicing
    extracted_end = target_string[-suffix_length:]
    
    # I-check kung nag-match ba yung dulo ng string sa hinahanap nating suffix
    if extracted_end == suffix_string:
        # Kung nag-match, i-chop natin yung dulo at i-return yung natira sa unahan
        return target_string[:-suffix_length]
        
    # Kung hindi nag-match, ibalik lang yung original na string
    return target_string