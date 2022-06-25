from resources.modules.users import *
from resources.modules.verify import *
from resources.modules.paths import *

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d