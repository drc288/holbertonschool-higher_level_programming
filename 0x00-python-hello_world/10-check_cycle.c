#include "lists.h"

/**
 * check_cycle - check if the simple list are a cycle list.
 * list: the single list.
 *
 * Return: 1 if the single list are a cycle list.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp1 = NULL, *tmp2 = NULL;
	int value = 0, id = 0;

	if (list == NULL)
		return (0);
	tmp1 = list;
	tmp2 = list;
	while (tmp2)
	{
		if (tmp1 == tmp2 && id != 0)
		{
			return (1);
		}

		tmp2 = tmp2->next->next;
		tmp1 = tmp1->next;
		id++;
	}

	return (value);
}
