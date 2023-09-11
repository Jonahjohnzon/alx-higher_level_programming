#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int the_size = PyList_Size(p);

	int count;

	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", the_size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (count = 0; count < the_size; count++)
		printf("Element %i: %s\n", count, Py_TYPE(object->ob_item[count])->tp_name);
}
