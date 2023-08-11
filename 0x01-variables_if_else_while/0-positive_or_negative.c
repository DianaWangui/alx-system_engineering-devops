#include <stdio.h>
#include <stdlib.h>
#include <time.h>
/**
 * main - This is the entry point to the program
 *
 * This function prints random number, stores it in the variable 'n',
 *and then prints whether the number is positive, negative or zero.
 * Return: :0 (Success)
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	printf("Random number: %d\n", n);

	if (n > 0)
	{
		printf("%d is positive\n", n);
	}
	else if (n < 0)
	{
		printf("%d is negative\n", n);

	}
	else
	{
		printf("%d is zero\n", n);
	}
	return (0);
}
