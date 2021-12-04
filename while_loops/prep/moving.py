width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
space_taken = 0
done = True

box = input()
while box != 'Done':
    space_taken += int(box)

    if free_space <= space_taken:
        print(f"No more free space! You need {space_taken - free_space} Cubic meters more.")
        done = False
        break

    box = input()

if done:
    print(f"{free_space - space_taken} Cubic meters left.")
