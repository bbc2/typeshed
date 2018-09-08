from typing import Dict

class symbol:
    symbols: Dict[str, 'symbol']
    def __new__(cls, name: str) -> 'symbol': ...
