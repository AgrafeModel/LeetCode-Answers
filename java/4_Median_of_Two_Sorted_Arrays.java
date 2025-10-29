class Solution {
    //Simple solution (2ms)
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> merged = new ArrayList();
        int x = 0;
        int y = 0;

        while(x<nums1.length && y<nums2.length){
            if(nums1[x]<nums2[y]){
                merged.add(nums1[x]);
                x++;
            } else {
                merged.add(nums2[y]);
                y++;
            }
        }

        while(x<nums1.length){
            merged.add(nums1[x]);
            x++;
        }

        while(y<nums2.length){
            merged.add(nums2[y]);
            y++;
        }

        int mid = (merged.size() -1 )/ 2  ;
        if(merged.size()%2 == 0){
            return ((double)(merged.get(mid) + merged.get(mid+1))) / 2;
        } else {
            return merged.get(mid);
        }

    }
}
