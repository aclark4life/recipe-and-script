from setuptools import setup

setup(
    name='recipe_script',
    py_modules=[
        'recipe_script',
    ],
    entry_points={
        'console_scripts': 'script = recipe_script:script',
    }
)
