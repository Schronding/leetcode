# Test cases
people_0 = [1,2]
limit_0 = 3
# Expected output: 1

people_1 = [3,2,2,1]
limit_1 = 3
# Expected output: 3

people_2 = [3,5,3,4]
limit_2 = 5
# Expected output: 4

class Solution:
    def numRescueBoats(people: list[int], limit: int) -> int:
        boats, current_weight = 0, 0
        while people:
            if people[0] == limit:
                people.remove(people[0])
                boats += 1
            elif people[0] < limit:
                for weight in people:
                    if people[0] + weight == limit:
                        people.remove(people[0])
                        people.remove(weight)
                        boats += 1
            people.remove(people[0])
            boats += 1
        return boats
            
                
    
    #print(numRescueBoats(people_0, limit_0))
    print(numRescueBoats(people_1, limit_1))
    print(numRescueBoats(people_2, limit_2))


