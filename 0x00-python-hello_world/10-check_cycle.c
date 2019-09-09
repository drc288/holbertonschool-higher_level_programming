#include "lists.h"

/**
 * check_cycle - check if the simple list are a cycle list.
 * list: the single list.
 *
 * Return: 1 if the single list are a cycle list.
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;
	int value = 1;

	if (list == NULL)
		return (0);
	ptr = list;
	while (list)
	{
		if (list->next == NULL)
		{
			value = 0;
			break;
		}
		if (list->next == ptr)
		{
			break;
		}

		list = list->next;
	}

	return (value);
}
