#include <stdio.h>

int main(){
    int ar[9] = {34,35,35,33,56,78,92,34,78};
    for(int i =0; i<9; i++){
        for(int j =i+1; j<9; j++){
            if(ar[i] == ar[j]){
                printf("%d\n",ar[i]);
            }

        }
    }

}
