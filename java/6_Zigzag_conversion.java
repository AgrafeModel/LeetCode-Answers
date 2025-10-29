class Solution {
    public String convert(String s, int numRows) {
        int direction = -1;
        List<Character>[] arr = new ArrayList[numRows];
        for(int j=0;j<numRows;j++){
            arr[j] = new ArrayList();
        }


        int row = 0;
        for(char c : s.toCharArray()){
            arr[row].add(c);
            if(row == numRows -1){
                direction = -1;
            } else if(row == 0){
                direction = 1;
            }
            row += direction;
        }

        StringBuilder res = new StringBuilder();
        for(List<Character> r : arr){
            for(char c : r){
                res.append(c);
            }
        }

        return res.toString();
    }
}
