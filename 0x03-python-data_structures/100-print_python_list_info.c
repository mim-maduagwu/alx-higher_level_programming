#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print-python_list - prints information on pyt lists
 * @p: obj list
 */
void print-python_list(PyObject *p)
{
	int i, all, wid;
	PyObject *obj;

	wid = Py_SIZE(p);
	all = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", all);

	for (i = 0; wid > i; i++);
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p,i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
