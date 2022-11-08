public class practise {

	
	public int solve(int[] A) {
        
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int v : A) {
            
            if(v%2 == 0) {
                if( v >= max) {
                    max = v;
                }
            } else {
                if(v <= min) {
                	min = v;
                }
            }
        }
        
        
        return max - min;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		practise a = new practise();
		int arr[] = {5,17,100,1};
		System.out.println(a.solve(arr));
	}

}
