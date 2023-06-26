#include <Python.h>
#include "catalog_classifier.h"

static PyObject* catalog_classifier_search(PyObject* self, PyObject* args)
{
    // Parse the input arguments from Python
    const char* catalog_path;
    const char* search_term;
    if (!PyArg_ParseTuple(args, "ss", &catalog_path, &search_term)) {
        return NULL;
    }

    // Call the C++ catalog classifier function
    CatalogClassifier classifier(catalog_path);
    std::vector<std::string> results = classifier.search(search_term);

    // Convert the C++ results to a Python list
    PyObject* py_results = PyList_New(results.size());
    for (size_t i = 0; i < results.size(); i++) {
        PyList_SetItem(py_results, i, PyUnicode_FromString(results[i].c_str()));
    }

    // Return the Python list of results
    return py_results;
}

static PyMethodDef catalog_classifier_methods[] = {
    {"search", catalog_classifier_search, METH_VARARGS, "Search the catalog for a term."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef catalog_classifier_module = {
    PyModuleDef_HEAD_INIT,
    "catalog_classifier",
    "Catalog classifier module",
    -1,
    catalog_classifier_methods
};

PyMODINIT_FUNC PyInit_catalog_classifier(void)
{
    return PyModule_Create(&catalog_classifier_module);
}
