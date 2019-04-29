long = int(input())

best_d = 0
biggest_volume = -1

for d in range( (long//2) +1 ):
    volume = (long - 2*d) * (long - 2*d) * d 
    if volume >= biggest_volume:
        biggest_volume = volume
        best_d = d

print(best_d, biggest_volume)