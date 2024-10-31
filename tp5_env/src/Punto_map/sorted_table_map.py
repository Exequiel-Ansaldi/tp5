from typing import List
from data_structures import MapBase
from sorted_table_map_abstract import SortedTableMap

class SortedTableMap(MapBase, SortedTableMap):

    def __len__(self) -> int:
        return len(self._table)
    
    def __str__(self) -> str:
        return ', '.join(f'({item._key}: {item._value})' for item in self._table)
