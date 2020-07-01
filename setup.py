import setuptools

setuptools.setup(
    name='launchctl',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
