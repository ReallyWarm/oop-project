import sys
sys.path.append('./web_app/class_object/') 
from category import TypeOfTool, SubtypeOfTool
from wishlish import Wishlist
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System  
from admin import Admin 
from discount import Wholesale
if __name__ == "__main__":  
    system = System()
    category = system.category
    hand_tools_type = TypeOfTool(name='Hand tools')
    drills_type = SubtypeOfTool(name='Drills')
    nothing = SubtypeOfTool(name='None')

    category.add_type(hand_tools_type)
    category.type_add_subtype(hand_tools_type, drills_type)
    category.type_add_subtype(hand_tools_type, nothing)
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    category.subtype_add_tool(drills_type, test_drill)
    #print(test_drill)

    admin = Admin("admin","1234","Kelvin","Lim","admin@gmail.com")  
    # add wholesale
    system.add_wholesale("03x",5,20) 

    # search tool
    search = category.search_by_name('')
    testing = search['Testing drill']
    print(testing)  

    # update wholesale tool
    wholesale = system.search_wholesale("03x")
    testing.add_wholesale(wholesale)
    print(system.wholesales)
    print(testing.wholesales)

    # modify wholesale
    system.modify_wholesale("03x",10,15) 
    print(system.wholesales[0].amount)
    print(testing.wholesales[0].amount)

    # delete wholesale 
    system.delete_wholesale("03x") 
    print(system.wholesales) 
    # testing.delete_wholesale("03x") 
    print(testing.wholesales)
    # update tool 
    # print(system._wholesale) 