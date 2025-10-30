class Solution {
    public boolean isPalindrome(int x) {
        int x1 = x;
        int x2 = 0;

        while(x>0){
            x2=x2 * 10 + x%10;
            x/=10;
        }

        return x1 == x2;
    }
}
