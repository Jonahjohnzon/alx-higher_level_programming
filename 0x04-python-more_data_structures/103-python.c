#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - print
 * @p: input
 * Return:void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, a;
	long int lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size >= 10)
	{
		lim = 10;
	}
	else
	{
		lim = size + 1;
	}
	printf("  first %ld bytes:", lim);
	for (a = 0; a < lim; a++)
		if (str[a] >= 0)
			printf(" %02x", str[a]);
		else
			printf(" %02x", 256 + str[a]);
	printf("\n");
}

/**
 * print_python_list - function list
 * @p: input
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int siz;
	long int a;

	PyListObject *lt;
	PyObject *object;

	siz = ((PyVarObject *)(p))->ob_size;
	lt = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", lt->allocated);
	for (a = 0; a < siz; a++)
	{
		object = ((PyListObject *)p)->ob_item[a];
		printf("Element %ld: %s\n", a, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
		{
			print_python_bytes(object);
		}
	}
}
