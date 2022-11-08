package day_two;

import java.util.HashMap;

public class SingleNumber {

	public int singleNumber(final int[] A) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int toReturn = -1;
        for(int i: A) {
        	if(map.containsKey(i)) {
        		map.put(i, map.get(i)+1);
        	} else {
        		map.put(i, 1);
        		
        	}
        }// end of for
     
        for(int key: map.keySet()) {
        	if(map.get(key) ==1 ) {
        		toReturn = key;
        		break;
        	}
        }
        	
        return toReturn;
    }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SingleNumber obj = new SingleNumber();
		int[] array = {1,2,2,3,1};
		System.out.println(obj.singleNumber(array));
	}

}
