from math import floor

tournaments_count = int(input())
initial_points = int(input())

w = 2000
f = 1200
sf = 720
won = 0
points = 0

for i in range(tournaments_count):
    tournament_stage = input()

    if tournament_stage == 'W':
        points += w
        won += 1
    elif tournament_stage == 'F':
        points += f
    elif tournament_stage == 'SF':
        points += sf

win_percent = won / tournaments_count * 100
average_points = floor(points / tournaments_count)
final_points = initial_points + points

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")
