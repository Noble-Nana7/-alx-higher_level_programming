#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * 
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0); /* No cycle if list is empty or has one node */

	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1); /* Cycle detected */

		slow = slow->next;       /* Move slow by one */
		fast = fast->next->next; /* Move fast by two */
	}

	return (0); /* No cycle found */
}
