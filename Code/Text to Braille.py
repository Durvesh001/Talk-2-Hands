def text_to_braille(text):
    braille_dict = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋',
        'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇',
        'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 'r': '⠗',
        's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
        'y': '⠽', 'z': '⠵',
        'A': '⠠⠁', 'B': '⠠⠃', 'C': '⠠⠉', 'D': '⠠⠙', 'E': '⠠⠑', 'F': '⠠⠋',
        'G': '⠠⠛', 'H': '⠠⠓', 'I': '⠠⠊', 'J': '⠠⠚', 'K': '⠠⠅', 'L': '⠠⠇',
        'M': '⠠⠍', 'N': '⠠⠝', 'O': '⠠⠕', 'P': '⠠⠏', 'Q': '⠠⠟', 'R': '⠠⠗',
        'S': '⠠⠎', 'T': '⠠⠞', 'U': '⠠⠥', 'V': '⠠⠧', 'W': '⠠⠺', 'X': '⠠⠭',
        'Y': '⠠⠽', 'Z': '⠠⠵',
        '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', '4': '⠲', '5': '⠢',
        '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔',
        ',': '⠂', '.': '⠲', '?': '⠦', '!': '⠖', "'": '⠄', '"': '⠐⠄',
        '-': '⠤', '_': '⠤', '(': '⠦⠴', ')': '⠴⠦', '&': '⠯', ';': '⠆⠂',
        ':': '⠒⠒', '/': '⠲⠆', '\\': '⠲⠆', '@': '⠈⠹',
        ' ': ' '
    }
    
    braille_text = ''
    for char in text:
        if char in braille_dict:
            braille_text += braille_dict[char]
    
    return braille_text

input_text = input("Enter text to convert to Braille: ")
braille_output = text_to_braille(input_text)
print("Braille:", braille_output)