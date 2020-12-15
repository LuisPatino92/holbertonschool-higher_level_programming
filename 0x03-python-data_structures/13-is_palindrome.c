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
	int length, i;

	length = len(*head);

	if (length == 0)
		return (1);
	for (i = 0; i <= length / 2; i++)
		if (value(*head, i) != value(*head, length - i - 1))
			return (0);
	return (1);
}

/**
 * len - Returns the length of a singly linked list
 *
 * @head: The linked list head
 *
 * Return: The length of the list
 */

int len(listint_t *head)
{
	int length = 0;

	while (head)
		head = head->next;

	return (length);
}

/**
 * value - Return the value of a node at index
 *
 * @head: The linked list head
 * @index: Index whose valu is desired
 *
 * Return: The n value of the node
 */

int value(listint_t *head, int index)
{
	int i = 0;

	while (head && i++ < index)
		head = head->next;
	return (head->n);

}
