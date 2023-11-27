#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle- check if a singly linked list has a sycle or not
 * @list: pointer a head of list
 * Return 1 if has a cycle, 0 if has not cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *slow = list, *fast = list;

    while(fast && fast->next)
    {
        fast = fast->next->next;
        slow = slow->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}
