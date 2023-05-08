#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - check if list has cycle
 * @list: the list
 * Return: 1 if there is a cyle or
 * 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *t = list;

	while (tmp && t && t->next != NULL)
	{
		tmp = tmp->next;
		t = t->next->next;
		if (tmp == t)
			return (1);
	}

	return (0);
}
