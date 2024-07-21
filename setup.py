import os

# Define the package structure
structure = {
    "mypackage": {
        "__init__.py": "",
        "module.py": "def hello():\n    print('Hello, world!')"
    },
    "setup.py": """\
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add command line scripts here
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
""",
    "LICENSE": "MIT License\n\n(Your license text here)",
    "README.md": "# MyPackage\n\nThis is a simple Python package.",
    "requirements.txt": "# Add your dependencies here"
}

# Create the directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

base_path = "mypackage"
create_structure(base_path, structure)

print(f"Skeleton package created at: {os.path.abspath(base_path)}")
