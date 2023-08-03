import os

# shutup prompts
os.environ["JULIA_PROJECT_INSTALL_JULIA"] = "y"
os.environ["JULIA_PROJECT_COMPILE"] = "y"
os.environ["JULIA_PROJECT_DEPOT"] = "y"
import shutil

# downloaidng Julia, updating packages, and compiling
from _julia_project import myjuliaproject

myjuliaproject.ensure_init()
myjuliaproject.update()
shutil.copy("Project.toml", "sys_image/Project.toml")
myjuliaproject.compile()

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
