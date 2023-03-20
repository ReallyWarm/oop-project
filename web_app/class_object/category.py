class Category:
    def __init__(self) -> None:
        self._categories = [ ]

    def get_type_of_tool(self):
        pass    

class TypeOfTool:
    def __init__(self, name) -> None:
        self._typename = name
        self._subtype_of_tools = [ ]

    def get_subtype_of_tool(self):
        pass
class SubtypeOfTool:
    def __init__(self, name) -> None:
        self._subtypename = name
        self._tools_list = []

    def get_tools_list(self):
        pass
