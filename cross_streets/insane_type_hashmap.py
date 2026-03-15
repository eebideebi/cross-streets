# I beg you, my RAM
# Just a drop of memory
# It would quench my thirst

import functools

key_to_index = {
    'alley': 0,
    'allee': 0,
    'ally': 0,
    'aly': 0,
    'annex': 1,
    'anex': 1,
    'annx': 1,
    'anx': 1,
    'arcade': 2,
    'arc': 2,
    'avenida': 3,
    'avenue': 4,
    'av': 4,
    'ave': 4,
    'aven': 4,
    'avenu': 4,
    'avn': 4,
    'avnue': 4,
    'bayou': 5,
    'bayoo': 5,
    'byu': 5,
    'beach': 6,
    'bch': 6,
    'bend': 7,
    'bnd': 7,
    'bluff': 8,
    'bluf': 8,
    'blf': 8,
    'bluffs': 9,
    'blfs': 9,
    'bottom': 10,
    'bot': 10,
    'bottm': 10,
    'btm': 10,
    'boulevard': 11,
    'boul': 11,
    'boulv': 11,
    'bld': 11,
    'blv': 11,
    'blvd': 11,
    'branch': 12,
    'brnch': 12,
    'br': 12,
    'bridge': 13,
    'brdge': 13,
    'brg': 13,
    'brook': 14,
    'brk': 14,
    'brooks': 15,
    'brks': 15,
    'burg': 16,
    'bg': 16,
    'burgs': 17,
    'bgs': 17,
    'bypass': 18,
    'bypa': 18,
    'bypas': 18,
    'byps': 18,
    'byp': 18,
    'calle': 19,
    'camino': 20,
    'camp': 21,
    'cmp': 21,
    'cp': 21,
    'canyon': 22,
    'canyn': 22,
    'cnyn': 22,
    'cyn': 22,
    'cape': 23,
    'cpe': 23,
    'causeway': 24,
    'causwa': 24,
    'cswy': 24,
    'center': 25,
    'cen': 25,
    'cent': 25,
    'centr': 25,
    'centre': 25,
    'cnter': 25,
    'cntr': 25,
    'ctr': 25,
    'centers': 26,
    'ctrs': 26,
    'circle': 27,
    'circ': 27,
    'circl': 27,
    'crcl': 27,
    'crcle': 27,
    'cir': 27,
    'circles': 28,
    'cirs': 28,
    'cliff': 29,
    'clf': 29,
    'cliffs': 30,
    'clfs': 30,
    'club': 31,
    'clb': 31,
    'common': 32,
    'cmn': 32,
    'commons': 33,
    'cmns': 33,
    'corner': 34,
    'cor': 34,
    'corners': 35,
    'cors': 35,
    'course': 36,
    'crse': 36,
    'court': 37,
    'ct': 37,
    'courts': 38,
    'cts': 38,
    'cove': 39,
    'cv': 39,
    'coves': 40,
    'cvs': 40,
    'creek': 41,
    'crk': 41,
    'crescent': 42,
    'crsent': 42,
    'crsnt': 42,
    'cres': 42,
    'crest': 43,
    'crst': 43,
    'crossing': 44,
    'crssng': 44,
    'xing': 44,
    'crossroad': 45,
    'xrd': 45,
    'curve': 46,
    'curv': 46,
    'dale': 47,
    'dl': 47,
    'dam': 48,
    'dm': 48,
    'divide': 49,
    'div': 49,
    'dvd': 49,
    'dv': 49,
    'drive': 50,
    'driv': 50,
    'drv': 50,
    'dr': 50,
    'drives': 51,
    'drs': 51,
    'estate': 52,
    'est': 52,
    'estates': 53,
    'ests': 53,
    'expressway': 54,
    'exp': 54,
    'expr': 54,
    'express': 54,
    'expw': 54,
    'expwy': 54,
    'expy': 54,
    'extension': 55,
    'extn': 55,
    'extnsn': 55,
    'ext': 55,
    'extensions': 56,
    'exts': 56,
    'fall': 57,
    'falls': 58,
    'fls': 58,
    'ferry': 59,
    'frry': 59,
    'fry': 59,
    'field': 60,
    'fld': 60,
    'fields': 61,
    'flds': 61,
    'flat': 62,
    'flt': 62,
    'flats': 63,
    'flts': 63,
    'ford': 64,
    'frd': 64,
    'fords': 65,
    'frds': 65,
    'forest': 66,
    'frst': 66,
    'forge': 67,
    'forg': 67,
    'frg': 67,
    'forges': 68,
    'frgs': 68,
    'fork': 69,
    'frk': 69,
    'forks': 70,
    'frks': 70,
    'fort': 71,
    'frt': 71,
    'ft': 71,
    'freeway': 72,
    'freewy': 72,
    'frway': 72,
    'frwy': 72,
    'fwy': 72,
    'garden': 73,
    'gardn': 73,
    'grden': 73,
    'grdn': 73,
    'gdn': 73,
    'gardens': 74,
    'gdns': 74,
    'gateway': 75,
    'gatewy': 75,
    'gatway': 75,
    'gtway': 75,
    'gtwy': 75,
    'glen': 76,
    'gln': 76,
    'glens': 77,
    'glns': 77,
    'green': 78,
    'grn': 78,
    'greens': 79,
    'grns': 79,
    'grove': 80,
    'grov': 80,
    'grv': 80,
    'groves': 81,
    'grvs': 81,
    'harbor': 82,
    'harb': 82,
    'harbr': 82,
    'hrbor': 82,
    'hbr': 82,
    'harbors': 83,
    'hbrs': 83,
    'haven': 84,
    'hvn': 84,
    'heights': 85,
    'hts': 85,
    'highway': 86,
    'highwy': 86,
    'hiway': 86,
    'hiwy': 86,
    'hway': 86,
    'hwy': 86,
    'hill': 87,
    'hl': 87,
    'hills': 88,
    'hls': 88,
    'hollow': 89,
    'hllw': 89,
    'holw': 89,
    'holws': 89,
    'inlet': 90,
    'inlt': 90,
    'island': 91,
    'is': 91,
    'islands': 92,
    'iss': 92,
    'isle': 93,
    'junction': 94,
    'jction': 94,
    'jctn': 94,
    'junctn': 94,
    'juncton': 94,
    'jct': 94,
    'junctions': 95,
    'jcts': 95,
    'key': 96,
    'ky': 96,
    'keys': 97,
    'kys': 97,
    'knoll': 98,
    'knol': 98,
    'knl': 98,
    'knolls': 99,
    'knls': 99,
    'lake': 100,
    'lk': 100,
    'lakes': 101,
    'lks': 101,
    'land': 102,
    'landing': 103,
    'lndng': 103,
    'lndg': 103,
    'lane': 104,
    'la': 104,
    'ln': 104,
    'light': 105,
    'lgt': 105,
    'lights': 106,
    'lgts': 106,
    'loaf': 107,
    'lf': 107,
    'lock': 108,
    'lck': 108,
    'locks': 109,
    'lcks': 109,
    'lodge': 110,
    'ldge': 110,
    'lodg': 110,
    'ldg': 110,
    'loop': 111,
    'lp': 111,
    'mall': 112,
    'manor': 113,
    'mnr': 113,
    'manors': 114,
    'mnrs': 114,
    'meadow': 115,
    'mdw': 115,
    'meadows': 116,
    'medows': 116,
    'mdws': 116,
    'mews': 117,
    'mill': 118,
    'ml': 118,
    'mills': 119,
    'mls': 119,
    'mission': 120,
    'msn': 120,
    'motorway': 121,
    'mtwy': 121,
    'mount': 122,
    'mt': 122,
    'mountain': 123,
    'mtn': 123,
    'mountains': 124,
    'mtns': 124,
    'neck': 125,
    'nck': 125,
    'orchard': 126,
    'orchrd': 126,
    'ch': 126,
    'oval': 127,
    'ovl': 127,
    'overlook': 128,
    'ovlk': 128,
    'overpass': 129,
    'opas': 129,
    'park': 131,
    'prk': 130,
    'parks': 131,
    'parkway': 132,
    'parkwy': 132,
    'pkway': 132,
    'pky': 132,
    'pkwy': 132,
    'parkways': 133,
    'pkwys': 133,
    'pass': 134,
    'passage': 135,
    'psge': 135,
    'path': 136,
    'pike': 137,
    'pk': 137,
    'pine': 138,
    'pne': 138,
    'pines': 139,
    'pnes': 139,
    'place': 140,
    'pl': 140,
    'plain': 141,
    'pln': 141,
    'plains': 142,
    'plns': 142,
    'plaza': 143,
    'plza': 143,
    'plz': 143,
    'point': 144,
    'pt': 144,
    'points': 145,
    'pts': 145,
    'port': 146,
    'prt': 146,
    'ports': 147,
    'prts': 147,
    'prairie': 148,
    'prr': 148,
    'pr': 148,
    'radial': 149,
    'rad': 149,
    'radiel': 149,
    'radl': 149,
    'ramp': 150,
    'rmp': 150,
    'ranch': 151,
    'rnch': 151,
    'rnchs': 151,
    'rapid': 152,
    'rpd': 152,
    'rapids': 153,
    'rpds': 153,
    'rest': 154,
    'rst': 154,
    'ridge': 155,
    'rdge': 155,
    'rdg': 155,
    'ridges': 156,
    'rdgs': 156,
    'river': 157,
    'rvr': 157,
    'rivr': 157,
    'riv': 157,
    'road': 158,
    'rd': 158,
    'roads': 159,
    'rds': 159,
    'route': 160,
    'rte': 160,
    'row': 161,
    'rue': 162,
    'run': 163,
    'shoal': 164,
    'shl': 164,
    'shoals': 165,
    'shls': 165,
    'shore': 166,
    'shr': 166,
    'shores': 167,
    'shrs': 167,
    'skyway': 168,
    'skwy': 168,
    'spring': 169,
    'spng': 169,
    'sprng': 169,
    'spg': 169,
    'springs': 170,
    'spgs': 170,
    'spur': 171,
    'square': 172,
    'sqr': 172,
    'sqre': 172,
    'squ': 172,
    'sq': 172,
    'squares': 173,
    'sqs': 173,
    'station': 174,
    'statn': 174,
    'stn': 174,
    'sta': 174,
    'strasse': 175,
    'the': 175,
    'stravenue': 176,
    'strav': 176,
    'straven': 176,
    'stravn': 176,
    'strvn': 176,
    'strvnue': 176,
    'stra;': 176,
    'stream': 177,
    'streme': 177,
    'strm': 177,
    'street': 178,
    'str': 178,
    'strt': 178,
    'st': 178,
    'streets': 179,
    'sts': 179,
    'summit': 180,
    'sumit': 180,
    'sumitt': 180,
    'smt': 180,
    'terrace': 181,
    'terr': 181,
    'ter': 181,
    'throughway': 182,
    'trwy': 182,
    'trace': 183,
    'trce': 183,
    'track': 184,
    'trak': 184,
    'trk': 184,
    'trks': 184,
    'trafficway': 185,
    'trfy': 185,
    'trail': 186,
    'trl': 186,
    'trailer': 187,
    'trlr': 187,
    'tunnel': 188,
    'tunl': 188,
    'turnpike': 189,
    'trnpk': 189,
    'turnpk': 189,
    'tpke': 189,
    'underpass': 190,
    'upas': 190,
    'union': 191,
    'un': 191,
    'unions': 192,
    'uns': 192,
    'valley': 193,
    'vally': 193,
    'vlly': 193,
    'vly': 193,
    'valleys': 194,
    'vlys': 194,
    'via': 196,
    'viaduct': 196,
    'vdct': 196,
    'viadct': 196,
    'view': 197,
    'vw': 197,
    'views': 198,
    'vws': 198,
    'village': 199,
    'vill': 199,
    'villag': 199,
    'villg': 199,
    'vlg': 199,
    'villages': 200,
    'vlgs': 200,
    'ville': 201,
    'vl': 201,
    'vista': 202,
    'vist': 202,
    'vst': 202,
    'vsta': 202,
    'vis': 202,
    'walk': 203,
    'wall': 204,
    'way': 205,
    'wy': 205,
    'well': 206,
    'wl': 206,
    'wells': 207,
    'wls': 207
}

index_to_forms = [
    [
        'Alley',
        'Allee',
        'Ally',
        'Aly'
    ],
    [
        'Annex',
        'Anex',
        'Annx',
        'Anx'
    ],
    [
        'Arcade',
        'Arc'
    ],
    [
        'Avenida'
    ],
    [
        'Avenue',
        'Av',
        'Ave',
        'Aven',
        'Avenu',
        'Avn',
        'Avnue'
    ],
    [
        'Bayou',
        'Bayoo',
        'Byu'
    ],
    [
        'Beach',
        'Bch'
    ],
    [
        'Bend',
        'Bnd'
    ],
    [
        'Bluff',
        'Bluf',
        'Blf'
    ],
    [
        'Bluffs',
        'Blfs'
    ],
    [
        'Bottom',
        'Bot',
        'Bottm',
        'Btm'
    ],
    [
        'Boulevard',
        'Boul',
        'Boulv',
        'Bld',
        'Blv',
        'Blvd'
    ],
    [
        'Branch',
        'Brnch',
        'Br'
    ],
    [
        'Bridge',
        'Brdge',
        'Brg'
    ],
    [
        'Brook',
        'Brk'
    ],
    [
        'Brooks',
        'Brks'
    ],
    [
        'Burg',
        'Bg'
    ],
    [
        'Burgs',
        'Bgs'
    ],
    [
        'Bypass',
        'Bypa',
        'Bypas',
        'Byps',
        'Byp'
    ],
    [
        'Calle'
    ],
    [
        'Camino'
    ],
    [
        'Camp',
        'Cmp',
        'Cp'
    ],
    [
        'Canyon',
        'Canyn',
        'Cnyn',
        'Cyn'
    ],
    [
        'Cape',
        'Cpe'
    ],
    [
        'Causeway',
        'Causwa',
        'Cswy'
    ],
    [
        'Center',
        'Cen',
        'Cent',
        'Centr',
        'Centre',
        'Cnter',
        'Cntr',
        'Ctr'
    ],
    [
        'Centers',
        'Ctrs'
    ],
    [
        'Circle',
        'Circ',
        'Circl',
        'Crcl',
        'Crcle',
        'Cir'
    ],
    [
        'Circles',
        'Cirs'
    ],
    [
        'Cliff',
        'Clf'
    ],
    [
        'Cliffs',
        'Clfs'
    ],
    [
        'Club',
        'Clb'
    ],
    [
        'Common',
        'Cmn'
    ],
    [
        'Commons',
        'Cmns'
    ],
    [
        'Corner',
        'Cor'
    ],
    [
        'Corners',
        'Cors'
    ],
    [
        'Course',
        'Crse'
    ],
    [
        'Court',
        'Ct'
    ],
    [
        'Courts',
        'Cts'
    ],
    [
        'Cove',
        'Cv'
    ],
    [
        'Coves',
        'Cvs'
    ],
    [
        'Creek',
        'Crk'
    ],
    [
        'Crescent',
        'Crsent',
        'Crsnt',
        'Cres'
    ],
    [
        'Crest',
        'Crst'
    ],
    [
        'Crossing',
        'Crssng',
        'Xing'
    ],
    [
        'Crossroad',
        'Xrd'
    ],
    [
        'Curve',
        'Curv'
    ],
    [
        'Dale',
        'Dl'
    ],
    [
        'Dam',
        'Dm'
    ],
    [
        'Divide',
        'Div',
        'Dvd',
        'Dv'
    ],
    [
        'Drive',
        'Driv',
        'Drv',
        'Dr'
    ],
    [
        'Drives',
        'Drs'
    ],
    [
        'Estate',
        'Est'
    ],
    [
        'Estates',
        'Ests'
    ],
    [
        'Expressway',
        'Exp',
        'Expr',
        'Express',
        'Expw',
        'Expwy',
        'Expy'
    ],
    [
        'Extension',
        'Extn',
        'Extnsn',
        'Ext'
    ],
    [
        'Extensions',
        'Exts'
    ],
    [
        'Fall'
    ],
    [
        'Falls',
        'Fls'
    ],
    [
        'Ferry',
        'Frry',
        'Fry'
    ],
    [
        'Field',
        'Fld'
    ],
    [
        'Fields',
        'Flds'
    ],
    [
        'Flat',
        'Flt'
    ],
    [
        'Flats',
        'Flts'
    ],
    [
        'Ford',
        'Frd'
    ],
    [
        'Fords',
        'Frds'
    ],
    [
        'Forest',
        'Frst'
    ],
    [
        'Forge',
        'Forg',
        'Frg'
    ],
    [
        'Forges',
        'Frgs'
    ],
    [
        'Fork',
        'Frk'
    ],
    [
        'Forks',
        'Frks'
    ],
    [
        'Fort',
        'Frt',
        'Ft'
    ],
    [
        'Freeway',
        'Freewy',
        'Frway',
        'Frwy',
        'Fwy'
    ],
    [
        'Garden',
        'Gardn',
        'Grden',
        'Grdn',
        'Gdn'
    ],
    [
        'Gardens',
        'Gdns'
    ],
    [
        'Gateway',
        'Gatewy',
        'Gatway',
        'Gtway',
        'Gtwy'
    ],
    [
        'Glen',
        'Gln'
    ],
    [
        'Glens',
        'Glns'
    ],
    [
        'Green',
        'Grn'
    ],
    [
        'Greens',
        'Grns'
    ],
    [
        'Grove',
        'Grov',
        'Grv'
    ],
    [
        'Groves',
        'Grvs'
    ],
    [
        'Harbor',
        'Harb',
        'Harbr',
        'Hrbor',
        'Hbr'
    ],
    [
        'Harbors',
        'Hbrs'
    ],
    [
        'Haven',
        'Hvn'
    ],
    [
        'Heights',
        'Hts'
    ],
    [
        'Highway',
        'Highwy',
        'Hiway',
        'Hiwy',
        'Hway',
        'Hwy'
    ],
    [
        'Hill',
        'Hl'
    ],
    [
        'Hills',
        'Hls'
    ],
    [
        'Hollow',
        'Hllw',
        'Holw',
        'Holws'
    ],
    [
        'Inlet',
        'Inlt'
    ],
    [
        'Island',
        'Is'
    ],
    [
        'Islands',
        'Iss'
    ],
    [
        'Isle'
    ],
    [
        'Junction',
        'Jction',
        'Jctn',
        'Junctn',
        'Juncton',
        'Jct'
    ],
    [
        'Junctions',
        'Jcts'
    ],
    [
        'Key',
        'Ky'
    ],
    [
        'Keys',
        'Kys'
    ],
    [
        'Knoll',
        'Knol',
        'Knl'
    ],
    [
        'Knolls',
        'Knls'
    ],
    [
        'Lake',
        'Lk'
    ],
    [
        'Lakes',
        'Lks'
    ],
    [
        'Land'
    ],
    [
        'Landing',
        'Lndng',
        'Lndg'
    ],
    [
        'Lane',
        'La',
        'Ln'
    ],
    [
        'Light',
        'Lgt'
    ],
    [
        'Lights',
        'Lgts'
    ],
    [
        'Loaf',
        'Lf'
    ],
    [
        'Lock',
        'Lck'
    ],
    [
        'Locks',
        'Lcks'
    ],
    [
        'Lodge',
        'Ldge',
        'Lodg',
        'Ldg'
    ],
    [
        'Loop',
        'Lp'
    ],
    [
        'Mall'
    ],
    [
        'Manor',
        'Mnr'
    ],
    [
        'Manors',
        'Mnrs'
    ],
    [
        'Meadow',
        'Mdw'
    ],
    [
        'Meadows',
        'Medows',
        'Mdws'
    ],
    [
        'Mews'
    ],
    [
        'Mill',
        'Ml'
    ],
    [
        'Mills',
        'Mls'
    ],
    [
        'Mission',
        'Msn'
    ],
    [
        'Motorway',
        'Mtwy'
    ],
    [
        'Mount',
        'Mt'
    ],
    [
        'Mountain',
        'Mtn'
    ],
    [
        'Mountains',
        'Mtns'
    ],
    [
        'Neck',
        'Nck'
    ],
    [
        'Orchard',
        'Orchrd',
        'Ch'
    ],
    [
        'Oval',
        'Ovl'
    ],
    [
        'Overlook',
        'Ovlk'
    ],
    [
        'Overpass',
        'Opas'
    ],
    [
        'Park',
        'Prk'
    ],
    [
        'Parks',
        'Park'
    ],
    [
        'Parkway',
        'Parkwy',
        'Pkway',
        'Pky',
        'Pkwy'
    ],
    [
        'Parkways',
        'Pkwys'
    ],
    [
        'Pass'
    ],
    [
        'Passage',
        'Psge'
    ],
    [
        'Path'
    ],
    [
        'Pike',
        'Pk'
    ],
    [
        'Pine',
        'Pne'
    ],
    [
        'Pines',
        'Pnes'
    ],
    [
        'Place',
        'Pl'
    ],
    [
        'Plain',
        'Pln'
    ],
    [
        'Plains',
        'Plns'
    ],
    [
        'Plaza',
        'Plza',
        'Plz'
    ],
    [
        'Point',
        'Pt'
    ],
    [
        'Points',
        'Pts'
    ],
    [
        'Port',
        'Prt'
    ],
    [
        'Ports',
        'Prts'
    ],
    [
        'Prairie',
        'Prr',
        'Pr'
    ],
    [
        'Radial',
        'Rad',
        'Radiel',
        'Radl'
    ],
    [
        'Ramp',
        'Rmp'
    ],
    [
        'Ranch',
        'Rnch',
        'Rnchs'
    ],
    [
        'Rapid',
        'Rpd'
    ],
    [
        'Rapids',
        'Rpds'
    ],
    [
        'Rest',
        'Rst'
    ],
    [
        'Ridge',
        'Rdge',
        'Rdg'
    ],
    [
        'Ridges',
        'Rdgs'
    ],
    [
        'River',
        'Rvr',
        'Rivr',
        'Riv'
    ],
    [
        'Road',
        'Rd'
    ],
    [
        'Roads',
        'Rds'
    ],
    [
        'Route',
        'Rte'
    ],
    [
        'Row'
    ],
    [
        'Rue'
    ],
    [
        'Run'
    ],
    [
        'Shoal',
        'Shl'
    ],
    [
        'Shoals',
        'Shls'
    ],
    [
        'Shore',
        'Shr'
    ],
    [
        'Shores',
        'Shrs'
    ],
    [
        'Skyway',
        'Skwy'
    ],
    [
        'Spring',
        'Spng',
        'Sprng',
        'Spg'
    ],
    [
        'Springs',
        'Spgs'
    ],
    [
        'Spur'
    ],
    [
        'Square',
        'Sqr',
        'Sqre',
        'Squ',
        'Sq'
    ],
    [
        'Squares',
        'Sqs'
    ],
    [
        'Station',
        'Statn',
        'Stn',
        'Sta'
    ],
    [
        'Strasse',
        'The'
    ],
    [
        'Stravenue',
        'Strav',
        'Straven',
        'Stravn',
        'Strvn',
        'Strvnue',
        'Stra;'
    ],
    [
        'Stream',
        'Streme',
        'Strm'
    ],
    [
        'Street',
        'Str',
        'Strt',
        'St'
    ],
    [
        'Streets',
        'Sts'
    ],
    [
        'Summit',
        'Sumit',
        'Sumitt',
        'Smt'
    ],
    [
        'Terrace',
        'Terr',
        'Ter'
    ],
    [
        'Throughway',
        'Trwy'
    ],
    [
        'Trace',
        'Trce'
    ],
    [
        'Track',
        'Trak',
        'Trk',
        'Trks'
    ],
    [
        'Trafficway',
        'Trfy'
    ],
    [
        'Trail',
        'Trl'
    ],
    [
        'Trailer',
        'Trlr'
    ],
    [
        'Tunnel',
        'Tunl'
    ],
    [
        'Turnpike',
        'Trnpk',
        'Turnpk',
        'Tpke'
    ],
    [
        'Underpass',
        'Upas'
    ],
    [
        'Union',
        'Un'
    ],
    [
        'Unions',
        'Uns'
    ],
    [
        'Valley',
        'Vally',
        'Vlly',
        'Vly'
    ],
    [
        'Valleys',
        'Vlys'
    ],
    [
        'Via'
    ],
    [
        'Viaduct',
        'Vdct',
        'Viadct',
        'Via'
    ],
    [
        'View',
        'Vw'
    ],
    [
        'Views',
        'Vws'
    ],
    [
        'Village',
        'Vill',
        'Villag',
        'Villg',
        'Vlg'
    ],
    [
        'Villages',
        'Vlgs'
    ],
    [
        'Ville',
        'Vl'
    ],
    [
        'Vista',
        'Vist',
        'Vst',
        'Vsta',
        'Vis'
    ],
    [
        'Walk'
    ],
    [
        'Wall'
    ],
    [
        'Way',
        'Wy'
    ],
    [
        'Well',
        'Wl'
    ],
    [
        'Wells',
        'Wls'
    ]
]

@functools.cache
def key_to_types(key: str|None) -> list[str]|None:
    '''Absolutely terrible way to map street types to all of their permutations'''
    if key is None:
        return None
    index = key_to_index.get(key.lower())
    if index is None:
        return None
    
    return index_to_forms[index]