letter = ''' Dear <|name|>,
        you are selected !
        <|Date|>'''

print(letter.replace("<|name|>" , "akshata").replace("<|Date|>","2026 sep 16"))