#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - function prints Python strings
 * @p: pointer PyObject
 */

void print_python_string(PyObject *p)
{
	long int ln;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	ln = ((PyASCIIObject *)(p))->ln;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", ln);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &ln));
}
