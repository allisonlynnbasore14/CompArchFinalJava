public class sourceCode{

    public sourceCode(){
        
        
    int[] array = {0,1,2,3,4,5,6,7,8,9,10};
    
    int adder = 3;
    
        
    for(int i =0; i<11;i++){
        array[i] = array[i] + adder;
        System.out.println(array[i]);
    }
    
    return;
        
    }
    
     public static void main(String []args){
        sourceCode sC = new sourceCode();
     }
}
