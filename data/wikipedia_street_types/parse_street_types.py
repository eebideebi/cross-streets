def main():
    brutish_hashmap: dict[str,int] = {}
    all_forms: list[list[str]] = []
    
    with open('wikipedia_street_types.txt') as f:
        lines = f.readlines()
        
    for i in range(len(lines)):
        line = lines[i]
        split = line.strip().split(' ')
        type = split[0].lower()
        
        all_types = [type]
        
        if len(split) > 1:
            abbr = list(map(lambda x: x.lower(),split[1].strip('()').split(',')))
            all_types += abbr
         
        for key in all_types:
            brutish_hashmap[key] = i
        all_forms.append(list(map(lambda x: x.capitalize(),all_types)))
            
        
    
    print(brutish_hashmap)
    print('\n\n\n\n\n')
    print(all_forms)
        
if __name__ == '__main__':
    main()