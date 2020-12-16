#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 *
 * @head: The linked list head
 *
 * Return: 1 if the linked list is a palindrome, 0 if it is not.
 */

int is_palindrome(listint_t **head)
{
	int length, i = 0, int_buff[2048];
	listint_t *walker = *head;

	if (!walker || !walker->next)
		return (1);

	while (walker)
	{
		int_buff[i] = walker->n;
		i++;
		walker = walker->next;
	}
	length = i;
	for (i = 0; i <= length / 2; i++)
		if (int_buff[i] != int_buff[length - i - 1])
			return (0);
	return (1);
}
