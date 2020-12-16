#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info -  Prints some data about A list python object.
 *
 * @list: The pointer to PyObject, is spected and its casted to list object
 */
void print_python_list_info(PyObject *list)
{
	int i;

	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(list));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)list)->allocated);

	for (i = 0; i < PyList_Size(list); i++)
	{
		if (PyFloat_Check(PyList_GetItem(list, i)))
			printf("Element %d: float\n", i);
		if (PyTuple_Check(PyList_GetItem(list, i)))
			printf("Element %d: tuple\n", i);
		if (PyList_Check(PyList_GetItem(list, i)))
			printf("Element %d: list\n", i);
		if (PyLong_Check(PyList_GetItem(list, i)))
			printf("Element %d: int\n", i);
		if (PyUnicode_Check(PyList_GetItem(list, i)))
			printf("Element %d: str\n", i);
	}
}
