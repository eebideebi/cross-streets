import cross_streets as cs
import usaddress

import pytest

# Simple initialization
class TestInitializationFunctions:
    tag = usaddress.tag('Hennepin Ave Southeast')[0]
    print(tag)
    street = cs.Street(tag)

    def test_init_name(self):
        assert self.street.name == 'Hennepin'    
    def test_direction(self):
        assert self.street.direction == 'SE'
    def test_type(self):
        assert self.street.type == 'Avenue'
        
    def test_permute_direction(self):
        dirs = self.street.permute_directions()
        assert dirs[0] == 'SE'
        assert dirs[1] == 'Southeast'
        
    def test_permutations_unique(self):
        perms = self.street.permutations()
        assert len(set(perms)) == len(perms)
