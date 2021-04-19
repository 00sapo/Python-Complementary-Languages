from setuptools import setup, Extension
from setuptools_rust import Binding, RustExtension

setup(
    name="list_rust",
    rust_extensions=[RustExtension("list_rust", binding=Binding.PyO3, debug=False)],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)

setup(name="list_cy",
      ext_modules=[
        Extension('list_cy',
                  sources=['list_cy.pyx'],
                  extra_compile_args=['-O3', '-fopenmp'],
                  extra_link_args=['-fopenmp'])
      ]
)

from Cython.Build import Cythonize
Cythonize.main(["*[!list_numba|main|simple_list]*.py", "-3", "--inplace"])
#Cythonize.main(["*.pyx", "-3", "--inplace"])
# for path in paths:
#     Cythonize.main([path, "-3", "--inplace"])


