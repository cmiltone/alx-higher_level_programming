#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints basic info
 * about Python lists
 * @p: list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, len = PyList_Size(p);
	PyListObject *l = (PyListObject *) p;
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
	printf("[*] Allocated = %d\n", (int)l->allocated);
	while (i < len)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i += 1;
	}
}

