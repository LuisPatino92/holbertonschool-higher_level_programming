#include <stdio.h>
#include <listobject.h>

void print_python_list_info(PyListObject list)
{
	int i;

	printf("[*] Size of the Python List = %d\n", (int)list.ob_size);
	printf("[*] Allocated = %d\n", (int)list.allocated);
	for (i = 0; i < (int)list.ob_size; i++)
		printf("Element %d: %s\n", i, (char *)Py_TYPE(list));
}