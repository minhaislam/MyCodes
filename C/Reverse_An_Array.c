#include <stdio.h>

int main(){
    int n;
    scanf("%d",&n);
    int ar[n];

    for(int i = 0;i<n;i++){
        scanf("%d",&ar[i]);
    }

    reverseFunc(ar,n);

}

int reverseFunc(int ar[],int n){
        for(int j = n-1;j>=0;j--){
        printf("%d\n",ar[j]);
    }

}
