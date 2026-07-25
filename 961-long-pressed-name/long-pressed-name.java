class Solution {
    public boolean isLongPressedName(String name, String typed) {
        int i=0;
        int j=0;
        int m=name.length();
        int n=typed.length();
        boolean fl=true;
        while (j<n){
            if (i<m  && name.charAt(i)==typed.charAt(j)){
                i+=1;
                j+=1;
            }else{
                if(i>0 && name.charAt(i-1)==typed.charAt(j)){
                    j+=1;
                }else{
                    return false;
                }

                }
            
            }
            if(i==m && j==n){
            return true;
            }
            else{
                return false;
            }
        }
  
    }
