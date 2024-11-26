#include <Python.h>
#include <stdio.h>
#include <string.h>

/* Function to print information about Python lists */
void print_python_list(PyObject *p)
{
	setbuf(stdout, NULL); /* Ensure unbuffered output */
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/* Function to print information about Python bytes */
void print_python_bytes(PyObject *p)
{
	setbuf(stdout, NULL); /* Ensure unbuffered output */
	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	char *string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	Py_ssize_t to_print = size < 10 ? size + 1 : 10;
	printf("  first %ld bytes: ", to_print);
	for (Py_ssize_t i = 0; i < to_print; i++)
		printf("%02x ", (unsigned char)string[i]);
	printf("\n");
}

/* Function to print information about Python floats */
void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL); /* Ensure unbuffered output */
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	double value = PyFloat_AsDouble(p);
	printf("  value: %g\n", value);
}
