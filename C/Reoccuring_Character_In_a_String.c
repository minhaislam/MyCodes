#include<stdio.h>

int main(){
    int i;
    char str[] = {NULL};
    printf("Enter String: ");
    scanf("%s",&str);
    int s = strlen(str);
    printf("%d",s);
    for(i = 0;i<s;i++){
        printf("%s",str[i]);
    }



}
