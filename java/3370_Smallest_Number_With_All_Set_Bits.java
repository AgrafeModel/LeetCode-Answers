class Solution {
    public int smallestNumber(int n) {
        int val = n;
        int res = 0;
        
        while(true){
            if(val <= 0){
                break;
            }
            val = val >> 1;
            res = (res << 1 ) +1;
        }
        return res;
    }
}
