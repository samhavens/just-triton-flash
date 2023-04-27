import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='flash_attn',
    version='0.0.1',
    author='Sam Havens',
    author_email='samhavens@gmail.com',
    description='Just Tri Dao\'s Flash Attention, but easier to install',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/samhavens/just-triton-flash',
    project_urls = {
        "Bug Tracker": 'https://github.com/samhavens/just-triton-flash/issues'
    },
    license='MIT',
    packages=['flash_attn'],
    install_requires=['triton==2.0.0.dev20221202'],
)