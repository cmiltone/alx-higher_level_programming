#include <stdio.h>
#include <python.h>
/**
 * print_python_list_info - prints basic info
 * about Python lists
 * @PyObject: list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	printf("%s", p);
}
