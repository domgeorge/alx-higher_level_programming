#include <Python.h>

/**
 * print_python_list_info - Func prints info on PY list
 * @p: Obj P
 */
void print_python_list_info(PyObject *p)
{
	int u;

	printf("[*] Size of the Python List = %li\n", Py_SIZE(p));
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
	for (u = 0; u < Py_SIZE(p); u++)
		printf("Element %i: %s\n", u, Py_TYPE(PyList_GetItem(p, u))->tp_name);
}
