import java.util.*;

public class practise {

	
	public ArrayList<Integer> solve(ArrayList<Integer> A) {
		
		ArrayList<Integer> B = new ArrayList<Integer>(A);
		Collections.sort(A);
		ArrayList<Integer> C = new ArrayList<Integer>();
		for(int i: B) {
			if(i != A.get(A.size()-1) && i != A.get(A.size()-2)) {
				C.add(i);
			}
		}
		
		return C;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		practise a = new practise();
		ArrayList<Integer> arr = new ArrayList<Integer>();
		Collections. addAll(arr, 11,17,100,5);
		System.out.println(a.solve(arr));
		
	}

}
