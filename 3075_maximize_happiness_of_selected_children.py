# Test cases
happiness_0 = [1,2,3]
k_0 = 2
# Expected output: 4

happiness_1 = [1,1,1,1]
k_1 = 2
# Expected output: 1

happiness_2 = [2,3,4,5]
k_2 = 1
# Expected output: 5

class Solution:
    def maximumHappinessSum(happiness: list[int], k: int) -> int:
        negativity, total = 0, 0
        # I initialize two variables 'negativity' and 'total'. 'negativity' is the amount of happiness we take off each kid by selecting another. 
        # As it is said in the problem, each time that we select a kid the happiness of all others is reduced by 1, but it CANNOT be smaller than zero. 
        happiness.sort()
        ## As we want to maximize, and 'happiness[i]' is how happy a kid is, if we sorted them in ascending order, the happiest kids would be closer to the ...
        ## ... right edge, while the least happy would be over the left side. 
        while k > 0:
        ### 'k' represents the amount of "turns" we have to take a kid. If it is one, we can take one kid, if it is 2, we can take two kids, and so on. 
        ### As we are guaranteed that 'k' cannot be negative, we know that this 'while' loop will end up always. 
        ### As 'k' is less or equal than 'n' (where n is the lenght of the list 'happiness') we cannot get 'IndexError' either. 
            added_happiness = happiness.pop() - negativity
            # As it is stated in this line, the "effective" or added happiness of each kid is equal to its value stored, minus the 'negativity' it has ...
            # ... accumulated. As our list is sorted, by using the '.pop()' method, we ensure that the kid we're taking away is the happiest of the current ...
            # ... list. >>
            if added_happiness >= 0:
            # >> However, that doesn't mean that the highest happiness in the list isn't zero. 
            # If there would come a moment in which the negativity is higher than the happiness of the kid, we would get a negative number, obtaining in ...
            # ... consequence incorrect output. That is why we check if that 'added_happiness' is at least 0. 
                total += added_happiness
                # If it is, we added to our total. If it isn't, we don't consider, as one of the conditions tells us that we cannot have negative happiness.
            negativity += 1
            ## We add one to 'negativity' on each iteration of the loop. As it has a minus sign ('-') the more we incremented it, the more it will ...
            ## ... substract the happiness of any given kid. 
            k -= 1
            ### We decriment 'k' in order to appropriately tell our loop to finish when it is done. 
        return total
        #### When all the iterations have been made I return 'total', but what if we had an empty array, or one filled with zeros? 
        #### Luckily, neither of those things can happen, as happiness[i] will always be equal or larger than 1, and so is 'k' (as mentioned above). 
        #### And even if that would occur, we initialized 'total' outside of the loop, so it would be fine nonetheless. 
    
    print(maximumHappinessSum(happiness_0, k_0))
    print(maximumHappinessSum(happiness_1, k_1))
    print(maximumHappinessSum(happiness_2, k_2))
