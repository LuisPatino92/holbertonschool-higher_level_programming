#include "lists.h"

/**
 * insert_node - Inserts a new node in a sorted Linked List
 *
 * @head: The head of the sorted list
 * @number: The number to be inserted
 *
 * Return: The addres of the node created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *current = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (head == NULL || *head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	while (current)
	{
		if (current->n <= new_node->n &&
			(current->next == NULL ||
			current->next->n >= new_node->n))
		{
			if (current == *head)
			{
				new_node->next = *head;
				*head = new_node;
			}
			else
			{
				new_node->next = current->next;
				current->next = new_node;
			}
			return (new_node);
		}
		current = current->next;
	}
	return (new_node);
}
