'''
backtracking template: 

def backtrack(state, choices):
      if is_solution(state): record and return
      for choice in choices:
          if is_valid(choice):
              make_choice()
              backtrack(next_state)
              undo_choice()    ← KEY: restore state
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rv = []

        def backtrack(start: int): 
            if start >= len(nums)-1: #leaves
                rv.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1) 
                nums[i], nums[start] = nums[start], nums[i]
        
        backtrack(0) 
        return rv


