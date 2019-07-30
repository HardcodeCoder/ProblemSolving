/** Program to find the number of perfect squares between a given range.
This logic is better than checking for each number from a to b, whether it's a perfect square or not,
as the time complexity is O(1) compared to O(n)
*/

#include<stdio.h>
#include<math.h>
int main(){
	int a,b,count = 0;
	printf("Enter the lower range : ");
	scanf("%d", &a);
	printf("\nEnter the upper range : ");
	scanf("%d", &b);
	
	count = floor(sqrt(b)) - ceil(sqrt(a)) + 1;
	printf("Number of perfect squares between %d and %d = %d", a,b,count);
	
}