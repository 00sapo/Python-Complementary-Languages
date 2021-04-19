from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="list_rust",
    rust_extensions=[RustExtension("list_rust", binding=Binding.PyO3, debug=False)],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)


from Cython.Build import Cythonize
Cythonize.main(["*[!list_numba|main|simple_list]*.py", "-3", "--inplace"])
Cythonize.main(["*.pyx", "-3", "--inplace"])
# for path in paths:
#     Cythonize.main([path, "-3", "--inplace"])


