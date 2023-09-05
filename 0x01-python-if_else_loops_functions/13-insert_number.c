#include "lists.h"

/**
 * insert_node - function
 * @head: pointer
 * @number: input
 * Return: listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodes = *head, *new_s;

	new_s = malloc(sizeof(listint_t));
	if (new_s == NULL)
	{
		return (NULL);
	}
	new_s->n = number;
	if (nodes == NULL || nodes->n >= number)
	{
		new_s->next = nodes;
		*head = new_s;
		return (new_s);
	}
	while (nodes && nodes->next && nodes->next->n < number)
	{
		nodes = nodes->next;
	}
	new_s->next = nodes->next;

	nodes->next = new_s;
	return (news);
}
