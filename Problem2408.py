# designing sql
class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.namesTable = {}
        for i in range(len(columns)):
            self.namesTable[columns[i]] = names[i]

    def ins(self, name: str, row: List[str]) -> bool:
        

    def rmv(self, name: str, rowId: int) -> None:

    
    def sel(self, name: str, rowId: int, columnId: int) -> str:

    
    def exp(self, name: str) -> List[str]:

