class Category:
    def __init__(self) -> None:
        self._categories = [ ]

class TypeOfTool:
    def __init__(self, name) -> None:
        self._typename = name
        self._subtype_of_tools = [ ]

class SubtypeOfTool:
    def __init__(self, name) -> None:
        self._subtypename = name
        self._tools = [ ]
