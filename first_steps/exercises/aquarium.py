length = int(input())
width = int(input())
height = int(input())
percent = float(input())

aquarium_volume = length * width * height
volume_in_liters = aquarium_volume / 1000
occupied_volume = percent / 100

liters_needed = volume_in_liters * (1 - occupied_volume)

print(liters_needed)
