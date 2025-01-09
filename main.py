n=int(input())
print(n)


cost=[[int(input()) for i in range(n)] for j in range(n)]
print(cost)

travel=[0]
pos=0
travelling_cost=0;
for i in range(n+1):
    min=100
    i=pos
    for j in range(n):   
        if(cost[i][j]<min and cost[i][j] != 0 and j not in travel ):
            min=cost[i][j]
            pos=j
    if(pos not in travel ):
        travel.append(pos)
        travelling_cost +=min;
        if(len(travel) == n):
            for k in range(n):
                if(k == travel[0]):
                    travel.append(k)
                    travelling_cost +=cost[pos][k];

for i in travel:
    print(f"{i+1}->",end=" ")
print(f"cost={travelling_cost}")

"""
input:
8
[[0, 5, 0, 6, 0, 4, 0, 7],
 [5, 0, 2, 4, 3, 0, 0, 0],
 [0, 2, 0, 1, 0, 0, 0, 0],
 [6, 4, 1, 0, 7, 0, 0, 0],
 [0, 3, 0, 7, 0, 0, 6, 4],
 [4, 0, 0, 0, 0, 0, 3, 0],
 [0, 0, 0, 0, 6, 3, 0, 2],
 [7, 0, 0, 0, 4, 0, 2, 0]]
 
output:
1->6->7->8->5->2->3->4->1->  
cost=25
"""
