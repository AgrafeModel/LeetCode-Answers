class Solution {
    public String longestPalindrome(String s) {
        
        int start = 0;
        int end = 0;


        for(int i=0;i<s.length();i++){
            int odd = this.findSize(s,i,i);
            int even = this.findSize(s,i,i+1);
            
            int max = Math.max(odd,even);

            if(max>end-start){
                start = i - (max -1) / 2;
                end = i + (max) / 2;
            }

        }
        
        return s.substring(start,end+1);
    }

    public int findSize(String s,int left, int right){
        while(left >= 0 && right <s.length() && s.charAt(left) ==s.charAt(right)){
            left--;
            right++;
        }
        return right - left -1;
    }
}
