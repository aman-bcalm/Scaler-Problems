import java.util.*;

public class practise {

	
	public int[][] solve(int A) {
        int res[][] = new int[A][A];
		for(int i=1; i<= A; i++) {
			for(int j=1; j<=A; j++) {
				if(i>=j) {
					res[i-1][j-1] = j;
				} else {
					res[i-1][j-1] = 0;
				}
			}
		}
		
		return res;
        
    }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		practise a = new practise();
		int A = 3;
		
		int res[][] = a.solve(A);
		
		for(int i =0; i<3; i++) {
			for(int j=0; j<3; j++) {
				System.out.print(res[i][j]);
			}
			System.out.println();
		}
		
	}

}
