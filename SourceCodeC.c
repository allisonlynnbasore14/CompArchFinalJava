
#include <stdio.h>

int main()
{
    int array[11] = {0,1,2,3,4,5,6,7,8,9,10};
    
    int adder =3;
    
    int i = 0;
    
    for(i;i<11;i++){
        
        array[i] = array[i] + adder;
    }

    return 0;
}
