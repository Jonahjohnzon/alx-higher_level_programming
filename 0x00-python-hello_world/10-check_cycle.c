#include "lists.h"
/**
 * check_cycle : function
 * Description: check for cycle
 * @list: input
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_speed;

	listint_t *fast_speed;

	if(!list)
	{
		return (0);
	}
	
	slow_speed = list;
	fast_speed = list->next;
	while (fast_speed && slow_speed && fast_speed->next)
	{
		if (slow_speed == fast_speed)
		{
			return (1);
		}
		slow_speed = slow_speed->next;
		fast_speed = fast_speed->next->next;
	}
	return (0);

}
