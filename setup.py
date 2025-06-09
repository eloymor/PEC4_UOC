from setuptools import setup, find_packages

# Función para listar las dependencias desde el archivo requirements.txt
def parse_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        # Eliminamos las líneas vacías y las líneas que comienzan con #
        return [line for line in lines if line.strip()
                and not line.startswith('#')]




setup(
    name='funciones_PEC4',
    version='0.0.1',
    description='Modulo de funciones para PEC4',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=parse_requirements("requirements.txt"),
    python_requires=">=3.10",
    license='MIT License',
    author='Eloy Mor',
    author_email='emorp@uoc.edu',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eloymor/PEC4_UOC"
)
