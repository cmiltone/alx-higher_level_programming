#include "lists.h"

/**
 * is_palindrome - checks if
 * list is a palindrome
 * @head: the list
 * Return: 1 if its a palindrome,
 * or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int start = 0, end, i = 0, integers[100];

	if (*head == NULL)
		return (1);
	while (*head != NULL)
	{
		integers[i] = (*head)->n;
		*head = (*head)->next;
		i += 1;
	}
	end = i - 1;
	while (start < end)
	{
		if (integers[start] != integers[end])
			return (0);
		start += 1;
		end -= 1;
	}
	return (1);
}
