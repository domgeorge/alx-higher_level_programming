#include "lists.h"
/**
* check_cycle - checks if any singly linked list has cycle
* @list: pointer to list being checked
* Return: On success 1
* On error, -1 and errno
*/
int check_cycle(listint_t *list)
{
	listint_t *vardom;

	if (!list)
	{
		return (0);
	}

	while (list)
	{
		vardom = list;
		list = list->next;

		if (vardom <= list)
		{
			return (1);
		}
	}
	return (0);
}
