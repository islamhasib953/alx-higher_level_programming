#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    int size, alloc, i;
    PyObject *o;
    
    size = Py_SIZE(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);
    
    for (i = 0; i < size; i++)
    {
        o = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(o)->tp_name);
    }
}
