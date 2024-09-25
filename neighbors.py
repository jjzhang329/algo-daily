# Example:
# { {8, 2, 9}, {4, 6, 4}, {4, 5, 1} }
# Each house is painted, so the second input is an array representing the color codes for each house. 
# { {'r', 'g', 'b'}, {'w', 'c', 'b'}, {'x', 'y', 'b'} }
# This means that House 8 is painted in color r, House 2 is g, House 9 is b etc.

from heapq import heappush, heappop

def rearrange_neighbourhood(house_numbers,house_colors):
    houses = []
    m,n = len(house_numbers), len(house_numbers[0])
    
    for i in range(m):
        for j in range(n): 
            heappush(houses, (house_numbers[i][j], house_colors[i][j]))
        
    ans = []
    discarded = [] # queue
    print(houses)
    
    for neighborhood in range(m):
        
        while discarded and discarded[0][-1]<=neighborhood:
            dnum,dcol,_=discarded.pop(0)
            heappush(houses, (dnum,dcol))
        
        temp = []
        for _ in range(n):
            if not houses: break
            num,col = heappop(houses)
            temp.append((f'{num}{col}'))
            
            # discard same num and colour
            while houses and (houses[0][0]==num or houses[0][1]==col):
                dnum,dcol=heappop(houses)
                discarded.append((dnum,dcol,neighborhood+1))
                
        ans.append(temp[:])
                
    return ans


print(rearrange_neighbourhood([[8,2,9], [4, 6, 4], [4, 5, 1]], [ ['r', 'g', 'b'], ['w', 'c', 'b'], ['x', 'y', 'b'] ])) 