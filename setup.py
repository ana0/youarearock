from distutils.core import setup
import py2exe

setup(console=['main.py'])from distutils.core import setup
import py2exe

# setup(console=[{
#             "script": "main.py",                    ### Main Python script    
#             "icon_resources": [(1, "icon.ico")]     ### Icon to embed into the PE file.
#         }])

setup_dict = dict(
    console = [{'script': "youarearock.py",
                "icon_resources": [(1, "icon.ico")]}],
)

setup(**setup_dict)
setup(**setup_dict)