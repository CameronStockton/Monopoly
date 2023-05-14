#Create board here, since never changes prob hard code

from properties import Property, Station, Utility
#initialize the properties first

#Brown
med_ave = Property(1, 'Mediterranean Avenue', 60, (2, 10, 30, 90, 160, 250), 50, 30, 30, ["Baltic Avenue"])
bal_ave = Property(2, 'Baltic Avenue', 60, (4, 20, 60, 180, 320, 450), 50, 30, 30, ["Mediterranean Avenue"])

#Light Blue
ori_ave = Property(3, 'Oriental Avenue', 100, (6, 30, 90, 270, 400, 550), 50, 50, 50, ["Vermont Avenue", "Connecticut Avenue"])
ver_ave = Property(4, 'Vermont Avenue', 100, (6, 30, 90, 270, 400, 550), 50, 50, 50, ["Oriental Avenue", "Connecticut Avenue"])
con_ave = Property(5, 'Connecticut Avenue', 120, (8, 40, 100, 300, 450, 600), 50, 60, 60, ["Oriental Avenue", "Vermont Avenue"])

#Pink
stc_pla = Property(6, 'St. Charles Place', 140, (10, 50, 150, 450, 625, 750), 100, 70, 70, ["States Avenue", "Virginia Avenue"])
sta_ave = Property(7, 'States Avenue', 140, (10, 50, 150, 450, 625, 750), 100, 70, 70, ["St. Charles Place", "Virginia Avenue"])
vir_ave = Property(8, 'Virginia Avenue', 160, (12, 60, 180, 500, 700, 900), 100, 80, 80, ["St. Charles Place", "States Avenue"])

#Orange
stj_pla = Property(9, 'St. James Place', 180, (14, 70, 200, 550, 750, 950), 100, 90, 90, ["Tennessee Avenue", "New York Avenue"])
ten_ave = Property(10, 'Tennessee Avenue', 180, (14, 70, 200, 550, 750, 950), 100, 90, 90, ["St. James Place", "New York Avenue"])
new_ave = Property(11, 'New York Avenue', 200, (16, 80, 220, 600, 800, 1000), 100, 100, 100, ["St. James Place", "Tennessee Avenue"])

#Red
ken_ave = Property(12, 'Kentucky Avenue', 220, (18, 90, 250, 700, 875, 1050), 150, 110, 110, ["Indiana Avenue", "Illinois Avenue"])
ind_ave = Property(13, 'Indiana Avenue', 220, (18, 90, 250, 700, 875, 1050), 150, 110, 110, ["Kentucky Avenue", "Illinois Avenue"])
ill_ave = Property(14, 'Illinois Avenue', 240, (20, 100, 300, 750, 925, 1100), 150, 120, 120, ["Kentucky Avenue", "Indiana Avenue"])

#Yellow
atl_ave = Property(15, 'Atlantic Avenue', 260, (22, 110, 330, 800, 975, 1150), 150, 130, 130, ["Ventnor Avenue", "Marvin Gardens"])
ven_ave = Property(16, 'Ventnor Avenue', 260, (22, 110, 330, 800, 975, 1150), 150, 130, 130, ["Atlantic Avenue", "Marvin Gardens"])
mar_gar = Property(17, 'Marvin Gardens', 280, (24, 120, 360, 850, 1025, 1200), 150, 140, 140, ["Atlantic Avenue", "Ventnor Avenue"])

#Green
pac_ave = Property(18, 'Pacific Avenue', 300, (26, 130, 390, 900, 1100, 1275), 200, 150, 150, ["North Carolina Avenue", "Pennsylvania Avenue"])
nor_ave = Property(19, 'North Carolina Avenue', 300, (26, 130, 390, 900, 1100, 1275), 200, 150, 150, ["Pacific Avenue", "Pennsylvania Avenue"])
pen_ave = Property(20, 'Pennsylvania Avenue', 320, (28, 150, 450, 1000, 1200, 1400), 200, 160, 160, ["Pacific Avenue", "North Carolina Avenue"])

#Dark Blue
par_pla = Property(21, 'Park Place', 350, (35, 175, 500, 1100, 1300, 1500), 200, 175, 175, ["Boardwalk"])
boardwalk = Property(22, 'Boardwalk', 400, (50, 200, 600, 1400, 1700, 2000), 200, 175, 175, ["Park Place"])

#Stations
rea_rail = Station(101, "Reading Railroad", 200, (25, 50, 100, 200), 100, 100, ["Pennsylvania Railroad", "B&O Railroad", 'Short Line'])
pen_rail = Station(102, "Pennsylvania Railroad", 200, (25, 50, 100, 200), 100, 100, ["Reading Railroad", "B&O Railroad", 'Short Line'])
bo_rail = Station(103, "B&O Railroad", 200, (25, 50, 100, 200), 100, 100, ["Reading Railroad", "Pennsylvania Railroad", 'Short Line'])
short_line = Station(104, "Short Line", 200, (25, 50, 100, 200), 100, 100, ["Reading Railroad", "Pennsylvania Railroad", 'B&O Railroad'])

#Utilities
ele_com = Utility(201, "Electric Company", 150, (4, 10), 75, 75, ["Water Works"])
wat_wor = Utility(202, "Water Works", 150, (4, 10), 75, 75, ["Electric Company"])


board = ['Go', med_ave, 'Community Chest', bal_ave, 'Income Tax', rea_rail, ori_ave, 'Chance', ver_ave, con_ave,
         'Just Visiting', stc_pla, ele_com, sta_ave, vir_ave, pen_rail, stj_pla, 'Community Chest', ten_ave, new_ave,
         'Free Parking', ken_ave, 'Chance', ind_ave, ill_ave, bo_rail, atl_ave, ven_ave, wat_wor,
         mar_gar, 'Go To Jail', pac_ave, nor_ave, 'Community Chest', pen_ave, short_line, 'Chance', par_pla,
         'Luxury Tax', boardwalk]

pos_prop = [1,3,6,8,9, 11,13,14,16,18,19, 21,23,24,26,27,29, 31,32,34,37,39]
pos_stat = [5, 15, 25, 35]
pos_util = [12, 28]