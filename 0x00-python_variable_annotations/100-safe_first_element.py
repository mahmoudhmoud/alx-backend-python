#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Any, Union, Sequence, Iterable, List, Tuple


# write the component
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Safe first element """
    if lst:
        return lst[0]
    else:
        return None
