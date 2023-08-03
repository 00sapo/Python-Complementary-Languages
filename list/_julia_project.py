import os
from julia_project import JuliaProject

mymodule_path = os.path.dirname(os.path.abspath(__file__))

# This just creates an object, but does none of the steps above.
myjuliaproject = JuliaProject(
    name="list_julia",
    package_path=mymodule_path,
    version_spec="^1.9.2",
    calljulia="pyjulia",
    sys_image_dir="./sys_image",
    sys_image_file_base="list_julia"
    )
