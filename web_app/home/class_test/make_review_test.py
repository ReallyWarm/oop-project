import sys
sys.path.append('./web_app/class_object/')
from customerinfo import CustomerInfo
from tool import Tool


test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
korphai = CustomerInfo("Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")
korphai.create_review(test_drill)
print("------------------------------------")
