int main() {
    
    int ar[6] = {45,67,23,54,69,76};
    int n = 6,j=ar[0],k=ar[0];
    for (int i=1;i<n;i++)
    {
        if(ar[i]>j){
            j=ar[i];
        }
    }
    for (int l=1;l<n;l++)
    {
        if(ar[l]<j && ar[l]>k){
            k=ar[l];
        }
    }
    printf("%d",k);

}