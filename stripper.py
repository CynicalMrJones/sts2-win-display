# For moving files
# import os
# path = r"cards/silent"
#
# for entry in os.scandir(path):
#     new_path = entry.path
#     # print(f'New PATH: {new_path}')
#     for ent in os.scandir(new_path):
#         # print(ent.path)
#         if ent.is_file:
#             os.rename(ent.path, f'{path}/{ent.name}')

# For getting rid of old data
# p = r"cards/curse"
#
# banlist = ["banner.png", "description_text.png",
#            "energy_icon.png",
#            "energy_label.png",
#            "frame.png",
#            "metadata.json",
#            "portrait_border.png",
#            "portrait_native.png",
#            "portrait.png",
#            "prolong.png",
#            "title_text.png",
#            "type_label.png",
#            "type_plaque.png"]
#
# for e in os.scandir(p):
#     card_name = e.name
#     print(f'Card name: {card_name}')
#     path = f'{p}/{card_name}'
#     print(path)
#     for file in os.scandir(path):
#         print(file.name)
#         if file.name == 'composite.png':
#             os.rename(f'{path}/composite.png', f'{path}/{card_name}.png')
#         if file.name in banlist:
#             os.remove(f'{path}/{file.name}')
