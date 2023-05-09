#include "lists.h"

/**
 * insert_node - inserts node to sorted list
 * @head: list
 * @number: data
 * Return: pointer to newly inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *tmp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;

	if (head == NULL || (*head)->n >= number)
	{
		node->next = *head;
		*head = node;
	} else
	{
		tmp = *head;
		while (tmp->next != NULL && tmp->next->n < node->n)
		{
			tmp = tmp->next;
		}
		node->next = tmp->next;
		tmp->next = node;
	}
	return (tmp->next);
}
