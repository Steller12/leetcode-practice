class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        prev_height = float('inf')
        total_sum = 0
        
        for height in maximumHeight:
            if prev_height <= 0:
                return -1  
            
            current_height = min(height, prev_height - 1)  
            
            if current_height <= 0:
                return -1  
            
            total_sum += current_height
            prev_height = current_height  
        
        return total_sum
