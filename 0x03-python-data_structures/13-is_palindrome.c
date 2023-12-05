#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL)
    return (1);
    return (check(head, *head));
}

/**
 * check - checks if a singly linked list is a palindrome
 * @left: pointer to left side of list
 * @right: pointer to right side of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int check(listint_t **left, listint_t *right)
{
    if (right == NULL)
    return (1);
    if (check(left, right->next) && (*left)->n == right->n)
    {
        *left = (*left)->next;
        return (1);
    }
    return (0);
}
