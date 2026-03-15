from importlib import resources
from .fuzzy_matching import find_most_similar_street, fetch_streets
from error_handling import Result, Ok, Err
import functools
import re

_key_to_index: dict[str,int] = {}
_index_to_types: list[list[str]] = []

def _parse_keys(path: str = 'wikipedia_street_types.txt') -> None:
    ''' ## This function is internal only. Do not call it in code.
        I beg you, o RAM<br>
        Just a drop of memory<br>
        It would quench my thirst<br>'''
            
    traversable = resources.files('cross_streets').joinpath(path)
    with traversable.open('r') as f:
        lines = f.readlines()
    
    for i in range(len(lines)):
        line = lines[i].strip().split('->')
        # print(line)
        forms = [line[0].lower()]
        
        if len(line) == 2:
            forms += [a.lower() for a in line[1].split(',')]
            
        for form in forms:
            _key_to_index[form] = i
        _index_to_types.append(forms)            

@functools.cache
def get_types(key: str|None) -> list[str]|None:
    '''Given a street type (e.g. 'ave'), 
        return all versions of that type (e.g. ['av', 'avenu', 'avenue'])'''
    if key is None:
        return None
    index = _key_to_index.get(key.lower())
    if index is None:
        return None
    return list(map(lambda x: x.capitalize(),_index_to_types[index]))

class Street:
    name: str # main street name ("Hennepin", etc.)
    type: str | None # unabbreviated street type # ("Avenue", etc.)
    direction: str | None # direction code ('N', 'SE', etc.)
    # Modifiers come immediately before/after the name (like a second name)
    # ^ extrapolated from https://www.austintexas.gov/sites/default/files/files/Planning/Applications_Forms/street-naming-standards.pdf
    modifier: str | None # street modifier
    
    def __str__(self):
        out = '\n\t'.join(['[Street Object]:',
                            f'name:     \t{self.name}',
                            f'type:     \t{self.type if self.type else ''}',
                            f'direction:\t{self.direction if self.direction else ''}',
                            f'modifier: \t{self.modifier if self.modifier else ''}',
                            'permutations:\t'])
        out += '\n\t\t\t'.join(self.permutations())
        
        return out
    
    def __init__(self, tag: dict[str,str]):
        self.name = tag['StreetName']
        self.direction = self.map_direction(tag.get('StreetNamePreDirectional') if tag.get('StreetNamePreDirectional') else tag.get('StreetNamePostDirectional'))
        self.type = self.long_type(tag.get('StreetNamePreType') if tag.get('StreetNamePreType') else tag.get('StreetNamePostType'))
        self.modifier = tag.get('StreetNamePreModifier') if tag.get('StreetNamePreModifier') else tag.get('StreetNamePostModifier')
        self.raw = self.raw_input(tag)
        
    def map_direction(self, dir: str|None) -> str|None:
        if dir is None:
            return None
        out = ''
        dir = dir.lower()
        
        if len(dir) <= 2:
            return (dir.upper()*2)[:2]
        
        # They call me The Riddler:
        matches = re.match(r'^(no?r?t?h?)?(so?u?t?h?)?(ea?s?t?)?(we?s?t?)?$',dir)
        if matches is None:
            return ''
        # North/South
        if matches.group(1):
            out += 'N'
        elif matches.group(2):
            out += 'S'
        # East/West    
        if matches.group(3):
            out += 'E'
        elif matches.group(4):
            out += 'W'    
        return out
    
    def permute_directions(self) -> list[str]:
        '''Gets a list of [abbr. direction (`NE`), full direction (`Northeast`)]''' # type: ignore
        if self.direction is None:
            return []
        
        short = self.direction
        long = ''
        # North/South:
        if self.direction.startswith('N'):
            long += 'north'
        elif self.direction.startswith('S'):
            long += 'south'
        # East/West:
        if self.direction.endswith('E'):
            long += 'east'
        elif self.direction.endswith('W'):
            long += 'west'
        
        return [short, long.capitalize()]
    
    def long_type(self, type: str|None) -> str|None:
        if type is None:
            return None
        
        forms = get_types(type)
        if forms is None:
            return None
        return forms[0]
    
    def raw_input(self,tag: dict[str,str]) -> str:
        '''Reconstruct a (lightly sanitized) version of the input street'''
        out = tag['StreetName']
        # Modifier:
        if tag.get('StreetNamePreModifier'):
            out = f'{tag['StreetNamePreModifier']} {out}'
        if tag.get('StreetNamePostModifier'):
            out = f'{out} {tag['StreetNamePostModifier']}'
        # Type:
        if tag.get('StreetNamePreType'):
            out = f'{tag['StreetNamePreType']} {out}'
        if tag.get('StreetNamePostType'):
            out = f'{out} {tag['StreetNamePostType']}'
        # Direction:
        if tag.get('StreetNamePreDirectional'):
            out = f'{tag['StreetNamePreDirectional']} {out}'
        if tag.get('StreetNamePostDirectional'):
            out = f'{out} {tag['StreetNamePostDirectional']}'
        # Output D:
        return out
    
    def permutations(self) -> list[str]:
        '''### Gets all permutations of the street\n\n
           We use the following CFG under the hood:\n
           N &rarr; name<br>
           M &rarr; modifier [N]] | [N] modifier | [N] <br>
           T &rarr; type [M] |[M] type | [M] <br>
           D &rarr; direction [T] | [T] direction | [T] <br>
           [Output D]
        '''
        
        # M -> modifier name] | name modifier | modifier
        if self.modifier:
            m_cfg = [f'{self.modifier} {self.name}', f'{self.name} {self.modifier}']
        else: 
            m_cfg = [self.name]
        # T -> [M] type | type [M] | [M]
        types = get_types(self.type)
        t_cfg = []
        if types:
            for type in types:
                for m in m_cfg:
                    t_cfg.append(f'{m} {type}')
                    t_cfg.append(f'{type} {m}')
        else:
            t_cfg = m_cfg          
        # D -> direction [T] | [T] direction | [T] <br>
        d_cfg = []
        if self.direction:
            for t in t_cfg:
                for dir in self.permute_directions():
                    d_cfg.append(f'{t} {dir}')
                    d_cfg.append(f'{dir} {t}')
        else: 
            d_cfg = t_cfg
        # [Output D]
        return d_cfg
    
    def get_best_match(self, valid_streets: set[str]) -> str:
        '''Gets the best fuzzy-matched street possible for a given string'''
        matches = [find_most_similar_street(valid_streets,s) for s in self.permutations()]
        matches = list(filter(None, [s.value if type(s) == Ok else None for s in matches]))
        # Failsafe: return raw input
        if len(matches) == 0:
            return self.raw
        return str(max(matches, key=lambda x: x['score'])['match'])

if __name__ == '__main__':
    import usaddress
    # Preprocessing necessary outside package:
    _parse_keys()
    
    tag = usaddress.tag('Hennepin Ave Southeast')[0]
    street = Street(tag)
    print(street)