for t in range(1, 11):

    N = int(input())

    height = list(map(int, input().split()))
    count = 0

    for i in range(2, N-2):
        next_four = [height[i-2], height[i-1], height[i+1], height[i+2]]
        
        highest_building = height[i-2]
        for building in next_four:
            if building > highest_building:
                highest_building = building

        if height[i] > highest_building:
            count += height[i] - highest_building
        
    print('#{} {}'.format(t, count))

