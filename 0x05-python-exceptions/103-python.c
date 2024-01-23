#include <Python.h>

void print_python_float(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_float - Function prints py float info
 * @p: pointer to Py Object
 */
void print_python_float(PyObject *p)
{
	double arr = 0;
	char *strng = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	arr = ((PyFloatObject *)p)->ob_fval;
	strng = PyOS_double_to_string(arr, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", strng);
}
/**
 * print_python_bytes - function print py bytes data
 * @p: pointer to Py Object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0;
	Py_ssize_t i = 0;
	char *strng = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	printf("  size: %zd\n", len);
	strng = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", strng);
	printf("  first %zd bytes:", len < 10 ? len + 1 : 10);
	while (i < len + 1 && i < 10)
	{
		printf(" %02hhx", strng[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - function prints py list info
 * @p: pointer to Py Object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		len = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", len);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < len)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
