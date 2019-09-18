#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome.
 * @head: linked list
 *
 * Return: 1 if is palidrome
 */
int is_palindrome(listint_t **head)
{
    int nodes = 0, i = 0, j = 0;
    int li[200];
    listint_t *tmp;

    tmp = *head;
    if (head == NULL || *head == NULL || (*head)->next == NULL )
        return (1);

    while (tmp != NULL)
    {
        li[nodes] = tmp->n;
        tmp = tmp->next;
        nodes++;
    }

    i = nodes - 1;
    while (i >= 0 && j <= i)
    {
        if (li[i] != li[j])
            return (0);
        i--;
        j++;
    }
    return (1);
}