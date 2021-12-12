#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


typedef struct list_node
{
    char napis[20];
    struct list_node *prev, *next;
} Node;

typedef struct Lista 
{
    Node* head;
    Node* wartownik;
}Lista;

Node* buduj_wezel(char napis[]) {
    Node* new = (Node*)malloc(sizeof(Node));

    strcpy(new->napis, napis);
    new->next = new->prev = NULL;
    
    return new;
}

void wstaw(char napis[], Lista *lista) {
    Node *nowy = buduj_wezel(napis);

    nowy->next = lista->wartownik->next;
    nowy->prev = lista->wartownik;
    lista->wartownik->next->prev = nowy;
    lista->wartownik->next = nowy;

    lista->head = nowy;
}

Node *inicjalizacja() {
    Node *wartownik = buduj_wezel("");
    wartownik->next = wartownik->prev = wartownik;

    return wartownik;
    
}

void drukuj(Lista *lista) {
    Node* printNode = lista->head;

    do
    {
        printf("%s\n", printNode->napis);
        printNode = printNode->next;
    } while (strcmp(printNode->napis, "") != 0);

    
    
}

Node* szukaj(char napis[], Lista *lista) {
    Node* searchNode = lista->head;

    do
    {
        if(strcmp(searchNode->napis, napis) == 0) {
            return searchNode;
        }
        searchNode = searchNode->next;
    } while (strcmp(searchNode->napis, "") != 0);

    return NULL;
}

void usun(char napis[], Lista *lista) {
    Node *deleteNode = lista->head;

    do
    {
        if(strcmp(deleteNode->napis, napis) == 0) {
            deleteNode->prev->next = deleteNode->next;
            deleteNode->next->prev = deleteNode->prev;
        }
        deleteNode = deleteNode->next;
    } while (strcmp(deleteNode->napis, "") != 0);
}

void kasuj(Lista *lista) {
    Node* current = lista->head;
    Node* next;

    while (strcmp(current->napis, "") != 0) 
    {
        next = current->next;
        free(current);
        current = next;
    }
    free(current);
}


int dlugosc(Lista *lista) {

    Node *current = lista->head;
    int n = 0;

    while(strcmp(current->napis, "") != 0) {
        n++;
        current = current->next;
    }
    return n;
}

void bezpowtorzen(Lista *lista) {
    int dlugoscListy = dlugosc(lista);

    char *napisy[dlugoscListy];
    Node *current = lista->head;
    Lista *nowa_lista;
    int iter = 0;

    while(strcmp(current->napis, "") != 0) {
        napisy[iter] = current->napis;
        current = current->next;
        iter++;
    }

    int count = 0;

    for (size_t i = 0; i < dlugoscListy; i++)
    {
        for (size_t j = i + 1; j < dlugoscListy; j++)
        {
            if(strcmp(napisy[i], napisy[j]) == 0) {
                count++;
                break;
            }
        }
    }

    int newLength = dlugoscListy - count;

    Node* wartownik = inicjalizacja();
    nowa_lista->wartownik = wartownik;


    current = lista->head;
    Node *currentNew = nowa_lista->wartownik;
    while (strcmp(current->napis, "") != 0) 
    {
        while (strcmp(currentNew->napis, "") != 0) 
        {
            if(strcmp)
        }
        
    }
    

    
}
}
int main() {

    Lista *lista;
    Node *wartownik = inicjalizacja();
    lista->wartownik = wartownik;

    wstaw("First", lista);
    wstaw("Second", lista);
    wstaw("Third", lista);
    wstaw("Third", lista);
    wstaw("Third", lista);
    wstaw("First", lista);







    return 0;
}