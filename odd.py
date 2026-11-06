count = 0
for i in range(0, 626001):
    square = i*i
    if square % 2 == 1:
        count = count + square
print(count)        
