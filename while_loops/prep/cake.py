w = int(input())
h = int(input())
peaces_count = w * h

while True:
    peace = input()
    if peace == 'STOP':
        print(f"{peaces_count} pieces are left.")
        break

    if peaces_count - int(peace) <= 0:
        print(f"No more cake left! You need {int(peace) - peaces_count} pieces more.")
        break
    else:
        peaces_count -= int(peace)
