#include "lists.h"

/**
 * check_cycle - Checks if a Linked List has a loop
 *
 * @list: The linked to be checked
 *
 * Return: 0 if there is no loop, 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = NULL, *turtle = NULL;

	hare = list;
	turtle = list;

	if ((hare == NULL) || (turtle == NULL))
		return (0);

	do {
		if ((hare->next == NULL) || (hare->next->next == NULL))
			return (0);

		hare = hare->next->next;
		turtle = turtle->next;
	} while (hare != turtle);

	return (1);
}
