# import json
#
# # card_dict = {
# #     "user_token": "**USER TOKEN**",
# #     "card_product_token": "**CARD PRODUCT TOKEN**"
# # }
# # print(card_dict)
# #
# # # card_details = json.dumps(card_dict['user_token'] == "new_user", card_dict[
# # #     'card_product_token'] == "new_card",)
# #
# #
# # card_dict.update(user_token="new_user", card_product_token="new_product")
# # print(card_dict)
# #
# # card_details = json.dumps(card_dict)
# # print(card_details)
#
#
# def get_card_payload(**kwargs):
#     card_dict = {
#         "user_token": "**USER TOKEN**",
#         "card_product_token": "**CARD PRODUCT TOKEN**"
#     }
#     if len(kwargs) >= 2:
#         for key in kwargs:
#             for k, v in card_dict.items():
#                 if key == k:
#                     card_dict[k] = kwargs[key]
#
#
#
#
#     card_payload = json.dumps(card_dict)
#     return card_payload
#
# print(get_card_payload(user_token="new_user",
#                        card_product_token="new+product"))

import random
number  = str(random.randrange(1000000000, 9999999999))
print("First random number of length 4 is ", number)
number  = random.randrange(1000, 9999)
print("Second random number of length 4 is ", number)

3440390611
123456890