def shift(letter):
    return chr( 97 + ( ( (ord(letter) + 1 - 97) % 26) ) )

print shift('z')
