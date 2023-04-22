
from customerinfo import CustomerInfo
from tool import Tool
from category import SubtypeOfTool, TypeOfTool
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from system import System

def add_database_users(system:'System'):
    # Customer information
    customers = [CustomerInfo('NorNor', 'Sawongnam', 'NorNor@gmail.com', 'Kmitl'), 
                CustomerInfo('พรี่โอมใจเกเร', 'สองศรี', 'Thanasak@gmail.com', 'Kmitl'),
                CustomerInfo("Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")]

    # Customer addresses
    customers[0].create_address('NorNor','จารย์แดง จำกัด','Thailand','Udon Thani','-','-','0210567473','10010')
    customers[1].create_address('พรี่โอมใจเกเร','ใจเกเร จำกัด','Thailand','Udon Thani','-','-','0810567473','10010')
    customers[2].create_address('Prakrittipon','KMIL','Thailand','Bangkok','Pha ya tai','sol.12 24/89','0901276842','11120')

    for i in range(len(customers)):
        system.add_customerinfo(customers[i])

def add_database_system(system:'System'):
    # Tool Types
    hand_tools_type = TypeOfTool(name='Hand tools')
    system.category.add_type(hand_tools_type)

    # Tool Sub Types
    drills_type = SubtypeOfTool(name='Drills')
    saws_type = SubtypeOfTool(name='Saws')
    system.category.type_add_subtype(hand_tools_type, drills_type)
    system.category.type_add_subtype(hand_tools_type, saws_type)

    # Tools
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1332&q=80", 1000.00, 'Drills')
    faifa_drill = Tool('02x', 'Faifa drill', 'POWER', 'idk', 12, "https://images.unsplash.com/photo-1504148455328-c376907d081c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1278&q=80", 800.00, 'Drills')
    sawaan_drill = Tool('03x', 'Sawaan', 'go to hell', 'HEAVEN', 15, "https://images.unsplash.com/photo-1622044939413-0b829c342434?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80", 2000.00, 'Drills')
    system.category.subtype_add_tool(drills_type, test_drill)
    system.category.subtype_add_tool(drills_type, faifa_drill)
    system.category.subtype_add_tool(drills_type, sawaan_drill)
    test_saw = Tool('04x', 'Testing saw', 'da-da', 'idk', 10, "https://images.unsplash.com/photo-1540104539488-92a51bbc0410?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80", 700.00, 'Saws')
    system.category.subtype_add_tool(saws_type, test_saw)

    # System Wholesales
    system.add_wholesale('01w',5,5) 
    system.add_wholesale('02w',10,8)

    # Tool Wholesale
    test_drill.add_wholesale(system.search_wholesale('01w'))
    test_drill.add_wholesale(system.search_wholesale('02w'))
    faifa_drill.add_wholesale(system.search_wholesale('01w'))

    # System Coupon
    system.add_coupon("1234",20,"สว่านใหม่ เจาะทะลุทะลวง ดุดันไม่เกรงใจใคร")

def add_database_userdata(system:'System'):
    test_drill = system.category.search_by_name('Testing drill')['Testing drill']
    system.customerinfos[2].create_review(test_drill, "test_review1", "good_tool", 4.5, "4/1/2023")