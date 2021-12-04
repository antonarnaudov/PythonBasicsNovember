# deg = int(input())
# daytime = input()
# outfit = ''
# shoes = ''
#
# if daytime == 'Morning':
#     if 10 <= deg <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif 18 < deg <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     else:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#
# elif daytime == 'Afternoon':
#     if 10 <= deg <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < deg <= 24:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     else:
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
#
# elif daytime == 'Evening':
#     if 10 <= deg <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < deg <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     else:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
deg = int(input())
daytime = input()
outfit = ''
shoes = ''

shirt = 'Shirt'
moccasins = 'Moccasins'
t_shirt = 'T-Shirt'
sandals = 'Sandals'

if daytime == 'Morning':
    if 10 <= deg <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < deg <= 24:
        outfit = shirt
        shoes = moccasins
    else:
        outfit = t_shirt
        shoes = sandals

elif daytime == 'Afternoon':
    if 10 <= deg <= 18:
        outfit = shirt
        shoes = moccasins
    elif 18 < deg <= 24:
        outfit = t_shirt
        shoes = sandals
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif daytime == 'Evening':
    outfit = shirt
    shoes = moccasins

print(f"It's {deg} degrees, get your {outfit} and {shoes}.")
