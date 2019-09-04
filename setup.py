from setuptools import setup, find_packages

version = "1.0.1"


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="mini-multisafepay",
    version=version,
    description="Multisafepay integration",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="",
    author="Jan Murre",
    author_email="jan.murre@catalyz.nl",
    url="https://github.com/jjmurre/mini-multisafepay",
    license="Apache",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=["requests"],
    extras_require={"testing": ["pytest", "Otto"]},
    entry_points={
        "console_scripts": ["msp_serve=multisafepay.testhttpserver:main"],
        "paste.app_factory": ["main=multisafepay.testhttpserver:app_factory"],
    },
)
