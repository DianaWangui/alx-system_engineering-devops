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
	if (n > 5)
	{
	}
}
