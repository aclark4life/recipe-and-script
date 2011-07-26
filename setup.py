from setuptools import setup

setup(
    name='recipe_script',
    entry_points={
#        'console_scripts': 'script = recipe_script:script',
        'zc.buildout': 'default = recipe_script:Recipe',
    },
    py_modules=[
        'recipe_script',
    ],
)
