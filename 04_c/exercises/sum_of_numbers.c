#include<stdio.h>

int main() 
{ 
    int maxVal = 20;
    int sum = 0;
    
    for (double i=1; i<=maxVal; i++)  {
        sum = sum + i;
    }

    printf("Sum: %d\n", sum);
}