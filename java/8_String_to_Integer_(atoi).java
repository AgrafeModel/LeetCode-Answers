class Solution {
    public int myAtoi(String s) {
        int res = 0;
        int sign = 1;
        boolean d = false;
        for(char c : s.toCharArray()){
            if(!d){
                if(c == ' '){continue;}
                if(c=='+'){
                    d=true;
                    continue;
                }
                if(c=='-'){
                    d=true;
                    sign=-1;
                    continue;
                }
            }
            int v = (int)(c - '0');
            if(v<0 || v>9){
                break;
            }
            if(res > (Integer.MAX_VALUE/10) || res == (Integer.MAX_VALUE/10) && v >7){
                return sign<0 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
            }
            d = true;
            res = res * 10 + v;
            
        }

        return res * sign;
    }
    
}
