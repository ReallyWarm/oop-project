class Category:
    def __init__(self) -> None:
        self._types_of_tool = [ ]

    @property
    def types_of_tool(self):
        return self._types_of_tool

    def add_type_of_tool(self, type_of_tool):
        self._types_of_tool.append(type_of_tool)

class TypeOfTool:
    def __init__(self, name) -> None:
        self._typename = name
        self._subtypes_of_tool = [ ]

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
    def tools_list(self):
        return self._tools_list

    def add_tool(self, tool):
        self._tools_list.append(tool)
