from tool import Tool
class Category:
    _all_types = [ ]
    _all_subtypes = [ ]
    _all_tools = [ ]

    def __init__(self) -> None:
        self._types_of_tool = [ ]

    @property
    def types_of_tool(self) -> list:
        return self._types_of_tool
    
    @staticmethod
    def get_subtypes_list(type_of_tool:'TypeOfTool') -> list:
        return type_of_tool.subtypes_of_tool
    
    @staticmethod
    def get_tools_list(subtype_of_tool:'SubtypeOfTool') -> list:
        return subtype_of_tool.tools_list
    


    def add_type(self, type_of_tool:'TypeOfTool') -> None:
        self.types_of_tool.append(type_of_tool)
        self._all_types.append(type_of_tool)

    def type_add_subtype(self, type_of_tool:'TypeOfTool', subtype_of_tool:'SubtypeOfTool') -> None:
        type_of_tool.add_subtype(subtype_of_tool)
        self._all_subtypes.append(subtype_of_tool)

    def subtype_add_tool(self, subtype_of_tool:'SubtypeOfTool', tool:'Tool') -> None:
        subtype_of_tool.add_tool(tool)
        self._all_tools.append(tool)

    def search_by_category(self, category_name:str) -> dict:
        searched = { }
        category_name_lower = category_name.lower()
        for type in self._all_types:
            if category_name_lower in type.typename.lower():
                searched[type.typename] = type
            
        for subtype in self._all_subtypes:
            if category_name_lower in subtype.subtypename.lower():
                searched[subtype.subtypename] = subtype

        return searched

    def search_by_name(self, name:str) -> dict:
        searched = { }
        name_lower = name.lower()
        for tool in self._all_tools:
            if name_lower in tool.name.lower():
                searched[tool.name] = tool
        
        return searched
        
    def __str__(self) -> str:
        return str(self.__class__)+f' -> types of tool : {len(self._all_types)}, subtypes of tool : {len(self._all_subtypes)}, tools : {len(self._all_tools)}'

    def __repr__(self):
        return f'\"{self.__str__()}\"'
    
class TypeOfTool:
    def __init__(self, name:str) -> None:
        self._typename = name
        self._subtypes_of_tool = [ ]

    @property
    def typename(self):
        return self._typename

    @property
    def subtypes_of_tool(self):
        return self._subtypes_of_tool

    def add_subtype(self, subtype_of_tool:'SubtypeOfTool'):
        self._subtypes_of_tool.append(subtype_of_tool)

    def __str__(self) -> str:
        return str(self.__class__)+f' -> name : {self.typename}, subtypes of tool : {len(self.subtypes_of_tool)}'
    
    def __repr__(self):
        return f'\"{self.__str__()}\"'

class SubtypeOfTool:
    def __init__(self, name:str) -> None:
        self._subtypename = name
        self._tools_list = []

    @property
    def subtypename(self):
        return self._subtypename

    @property
    def tools_list(self):
        return self._tools_list

    def add_tool(self, tool:'Tool'):
        self._tools_list.append(tool)

    def __str__(self) -> str:
        return str(self.__class__)+f' -> name : {self.subtypename}, subtypes of tool : {len(self.tools_list)}'
    
    def __repr__(self):
        return f'\"{self.__str__()}\"'
