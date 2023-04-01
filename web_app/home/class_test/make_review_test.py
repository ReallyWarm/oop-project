import sys
sys.path.append('./web_app/class_object/')
from customerinfo import CustomerInfo
from tool import Tool


test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
korphai = CustomerInfo("Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")
meawhod = CustomerInfo("prakonthakrit", "Picthaya", "meawnoy@gmail.com", "KMITL")
korphai.create_review(test_drill, "test_review1", "good_tool", 4.5, "4/1/2023")
meawhod.create_review(test_drill, "test_review2", "that broke", 1.5, "4/1/2023")

print("------------------------------------")
print(korphai.my_reviewed[0])
print("------------------------------------")
print(test_drill.review_list[0])
print("------------------------------------")
print(test_drill.review_list[1])
print("------------------------------------")
print(test_drill.rating)
