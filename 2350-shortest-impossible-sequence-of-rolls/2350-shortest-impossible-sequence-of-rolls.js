/**
 * @param {number[]} rolls
 * @param {number} k
 * @return {number}
 */
var shortestSequence = function(rolls, k) {
    
    
    
    var visited = new Set()
    var ans = 1
    
    for (var num of rolls) {
        visited.add(num)
        
        if (visited.size == k) {
            visited.clear()
            ans += 1
        }
    }
    
    return ans
    
    
};