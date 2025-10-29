class Solution {
    // Best version (2ms)
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> h = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int w = target - nums[i];
            if(h.containsKey(w)){
                return new int[]{ i,h.get(w) };
            }
            h.put(nums[i],i);
        }
        return new int[]{};
    };

    // Slow version (45ms)
    public int[] twoSumSlow(int[] nums, int target){
        for(int i = 0;i<nums.length;i++){
            for(int y=i+1;y<nums.length;y++){
                if(nums[i]+nums[y] == target){
                    return new int[] {i,y};
                }
            }
        }
        return new int[]{};
    }
}
