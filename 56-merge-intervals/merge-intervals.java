class Solution {
    public int[][] merge(int[][] intervals) {
        
        Arrays.sort(intervals,(a,b) -> Integer.compare(a[0],b[0]));
        int[] end=intervals[0];
        int n=intervals.length;

        ArrayList<int[]> ans= new ArrayList<>();

        for (int i=1;i<n;i++){

            if (intervals[i][0]<=end[1]){
                end[1]=Math.max(intervals[i][1],end[1]);
                
            }else{
                ans.add(end);
                end=intervals[i];
            }
        }
        ans.add(end);
        return ans.toArray(new int[ans.size()][]);
    }

        
    
}