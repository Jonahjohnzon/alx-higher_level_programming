#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - PyFloatObject
 * @p: PyObject
 */
void print_python_float(PyObject *p)
{
	double v = 0;

	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - function
 * @p:  PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0;
	Py_ssize_t x = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);

	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (x < size + 1 && x < 10)
	{
		printf(" %02hhx", string[x]);
		x++;
	}
	printf("\n");
}
/**
 * print_python_list - function
 * @p: PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t siz = 0;
	PyObject *x;
	int i = 0;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		siz = PyList_GET_SIZE(p);

		printf("[*] Size of the Python List = %zd\n", siz);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < siz)
		{
			x = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, x->ob_type->tp_name);
			if (PyBytes_Check(x))
			{
				print_python_bytes(x);
			}
			else if (PyFloat_Check(x))
			{
				print_python_float(x);
			}
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
