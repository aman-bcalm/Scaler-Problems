package day_two;

import java.util.ArrayList;

public class Number1Bits {

	 public int numSetBits(int A) {
	        
	        ArrayList<Integer> a = new ArrayList<Integer>();
	        int digit = 0;
	        int carry = 0;
	        while(A > 0) {
	          digit = A % 2;
	          a.add(digit);
	          A = A/2;
	        }
	        
	        int counter = 0;
	        for(int i : a) {
	        	if(i ==1)
	        		counter++;
	        }
	        
	        return counter;
	    }
	 
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Number1Bits a = new Number1Bits();
		System.out.println(a.numSetBits(11));

	}

}
