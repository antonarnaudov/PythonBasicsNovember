groups_count = int(input())

all_climbers_count = 0

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

for group in range(groups_count):
    climbers_count = int(input())

    if climbers_count <= 5:
        musala += climbers_count
    elif climbers_count <= 12:
        monblan += climbers_count
    elif climbers_count <= 25:
        kilimanjaro += climbers_count
    elif climbers_count <= 40:
        k2 += climbers_count
    else:
        everest += climbers_count

    all_climbers_count += climbers_count

musala = musala / all_climbers_count * 100
monblan = monblan / all_climbers_count * 100
kilimanjaro = kilimanjaro / all_climbers_count * 100
k2 = k2 / all_climbers_count * 100
everest = everest / all_climbers_count * 100

print(f'{musala:.2f}%')
print(f'{monblan:.2f}%')
print(f'{kilimanjaro:.2f}%')
print(f'{k2:.2f}%')
print(f'{everest:.2f}%')
