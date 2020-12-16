#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info -  prints info about Python lists, in a format.
 * @list: The pointer to PyObject
 */
void print_python_list_info(PyObject *list)
{
	PyObject *element;
	int i;

	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(list));
	printf("[*] Allocated = %li\n", (PyListObject *)list->allocated);

	for (i = 0; i < PyList_Size(list); i++)
	{
		element = PyList_GetItem(list, i);

		if (PyFloat_Check(element))
			printf("Element %d: float\n", i);
		if (PyTuple_Check(element))
			printf("Element %d: tuple\n", i);
		if (PyList_Check(element))
			printf("Element %d: list\n", i);
		if (PyLong_Check(element))
			printf("Element %d: int\n", i);
		if (PyUnicode_Check(element))
			printf("Element %d: str\n", i);
	}
}
