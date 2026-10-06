class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # Sort tiles by start position
        tiles.sort()
        n = len(tiles)
        
        # Create arrays for starts, ends and prefix sums
        starts = [tile[0] for tile in tiles]
        ends = [tile[1] for tile in tiles]
        prefix = [0] * (n + 1)
        
        # Calculate prefix sums
        for i in range(n):
            prefix[i + 1] = prefix[i] + (tiles[i][1] - tiles[i][0] + 1)
            
        ans = 0
        
        # Try placing carpet from start of each tile
        for i in range(n):
            curr = 0
            start = tiles[i][0]
            target = start + carpetLen - 1
            
            # Binary search to find where carpet ends
            j = bisect_left(ends, target)
            curr += prefix[j] - prefix[i]
            
            # Handle partial overlap
            if j < n:
                curr += max(0, target - tiles[j][0] + 1)
            ans = max(ans, curr)
            
        # Try placing carpet from end of each tile
        for i in range(n):
            curr = 0
            start = tiles[i][1]
            target = start - carpetLen + 1
            
            # Binary search to find where carpet starts
            j = bisect_left(starts, target)
            curr += prefix[i + 1] - prefix[j]
            
            # Handle partial overlap
            if j > 0:
                curr += max(0, tiles[j-1][1] - target + 1)
            ans = max(ans, curr)
            
        return ans
