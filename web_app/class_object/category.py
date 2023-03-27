class Category:
    def __init__(self) -> None:
        self._types_of_tool = [ ]

    @property
    def types_of_tool(self):
        return self._types_of_tool

    def add_type_of_tool(self, type_of_tool):
        self._types_of_tool.append(type_of_tool)

    def search_by_category(self, category_name):
        searched = { }
        category_name_lower = category_name.lower()
        for type in self.types_of_tool:
            if category_name_lower in type.typename.lower():
                searched[type.typename] = type
            
            for subtype in type.subtypes_of_tool:
                if category_name_lower in subtype.subtypename.lower():
                    searched[subtype.subtypename] = subtype

        # searched = [category for  ]

        return searched

class TypeOfTool:
    def __init__(self, name) -> None:
        self._typename = name
        self._subtypes_of_tool = [ ]

    @property
    def typename(self):
        return self._typename

    @property
    def subtypes_of_tool(self):
        return self._subtypes_of_tool

    def add_subtype(self, subtype_of_tool):
        self._subtypes_of_tool.append(subtype_of_tool)

class SubtypeOfTool:
    def __init__(self, name) -> None:
        self._subtypename = name
        self._tools_list = []

    @property
    def subtypename(self):
        return self._subtypename

    @property
    def tools_list(self):
        return self._tools_list

    def add_tool(self, tool):
        self._tools_list.append(tool)
