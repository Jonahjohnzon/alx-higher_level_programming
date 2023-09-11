#include "lists.h"

/**
 * reverse_list - linked reverse
 * @head: pointer
 * Return: void
 */
void reverse_list(listint_t **head)
{
	listint_t *pre = NULL;
	listint_t *curr = *head;
	listint_t *next = NULL;

	while (curr)
	{
		next = curr->next;
		curr->next = pre;
		pre = curr;
		curr = next;
	}

	*head = pre;
}

/**
 * is_palindrome - function
 * @head: input
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl = *head, *fast = *head, *tmp = *head;
	listint_t *dp = NULL;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dp = sl->next;
			break;
		}
		if (!fast->next)
		{
			dp = sl->next->next;
			break;
		}
		sl = sl->next;
	}
	reverse_list(&dp);
	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
		{
			return (0);
		}
	}
	if (!dp)
		return (1);

	return (0);
}
