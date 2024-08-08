letter = ''' Dear <|Name|>,
            you are selected! 
            <|Date|>'''

print(letter.replace("<|Name|>", "Zakir").replace("<|Date|>", "07 aguest 2024"))