#include <stdio.h>
int fibonacci(n){
    if(n<2){
        return n;
    }
    else{
        return fibonacci(n-1)+fibonacci(n-2);
    }
}
int main() {
    int n;
    scanf("%d",&n);
    for(int i=0; i<n;i++){
        printf("%d",fibonacci(i));
    }
    return 0;
}