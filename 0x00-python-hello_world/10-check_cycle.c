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

	while (tmp->next != NULL)
	{
		tmp = tmp->next;
	}

	if (tmp->next == list->next)
		return (1);
	return (0);
}
