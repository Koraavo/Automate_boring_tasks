import re
import pyperclip
text = ("""1FH49AA HP EliteDisplay E243i Monitor:
1ME40AA NVIDIA Quadro P4000 8GB Graphics:
1TJ76AA HP E243d Docking Monitor: March 2021
2UK37AA HP Thunderbolt Dock 120W G2:
3AQ21AA HP TB Dock Audio Module:
3TR87AA HP TB Dock G2 w/ Combo Cable:
3YE87AA HP TB Dock 120W G2 w/ Audio :
4QL34AA HP USB Business Slim Keyboard (OPINEL):              
4WX89AA HP Elite USB-C Hub:
5FT13AA HP EliteDisplay E243p Monitor:
7KN32EA HP EB840G6 i7-8565U 14 16GB/512 LTEA PC
7PF12EA HP EliteDesk 800G5 SFF i59500 16G/512 PC
7PF12EA HP EliteDesk 800G5 SFF i59500 16G/512 PC
7YL38EA HP EBx3601030G4 i58265U1316GB/512LTEAPC
8MJ35EA HP EB840G6HC i5-8265U 14 8GB/256 PC
8MK80EA HP Dragonfly i7-8565U 13 16GB/1T LTEA P
D9Y32AA HP UltraSlim Docking Station
J9P80AA HP Z440 Fan and Front Card Guide Kit
LQ037AA HP 1TB SATA 6Gb/s 7200 HDD
N3R87AA HP USB Business Slim Keyboard
QY778A6 HP (Bulk) USB 1000dpi Laser Mouse
QY778AA HP USB 1000dpi Laser Mouse
V7W66AA HP USB-C to RJ45 Adapter
""")

# text_break = re.compile(r'\b\w{7}\b')
# matches3 = text_break.finditer(text)
# for match3 in matches3:
#     if not match3.group().isalpha() and not match3.group().islower():
#         print(match3.group())

text_1 = text.split("\n")
for texts in text_1:
    new_split = texts.split(" ")
    print(new_split[0])
    models = " ".join(new_split[1:])
    print(models)



