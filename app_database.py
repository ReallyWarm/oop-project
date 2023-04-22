
from customerinfo import CustomerInfo
from tool import Tool
from category import SubtypeOfTool, TypeOfTool
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from system import System

def add_database_users(system:'System'):
    # Customer information
    customers = [CustomerInfo('NorNor007', '$2b$12$DmZVZhN.hpSa.QbeXWfUzO5Nh8b5Csh7AvqYFZsTR6i8KfdWlg6Am',
                              'NorNor', 'Sawongnam', 'NorNor@gmail.com', 'Kmitl'), # pass nornor
                CustomerInfo('PreeOhm','$2b$12$w4yNVfOcN36ylngAaAmW1etV8pD9H9ju0pbbeYFdbUaYof60CjA72',
                             'พรี่โอมใจเกเร', 'สองศรี', 'Thanasak@gmail.com', 'Kmitl'), # pass OhmZAZA
                CustomerInfo('KorphaiSK','$2b$12$3XJZVS.xPIG5NE46RspWZOsdQEbq3EFtKxMl7zB9.9XY9cf8283ny',
                             "Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL") # pass korphai1234
                ]

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
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    faifa_drill = Tool('02x', 'Faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    sawaan_drill = Tool('03x', 'Sawaan', 'go to hell', 'HEAVEN', 15, None, 2000.00, 'Drills')
    system.category.subtype_add_tool(drills_type, test_drill)
    system.category.subtype_add_tool(drills_type, faifa_drill)
    system.category.subtype_add_tool(drills_type, sawaan_drill)
    test_saw = Tool('04x', 'Testing saw', 'da-da', 'idk', 10, None, 700.00, 'Saws')
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