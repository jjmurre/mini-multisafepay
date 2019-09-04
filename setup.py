from setuptools import setup, find_packages

version = "0.1.6"

setup(
    name="mini-multisafepay",
    version=version,
    description="Multisafepay integration",
    long_description="""This package enables you to talk to a multisafepay
      payment provider. It uses the old deprecated XML API.
      There is not much documentation at the moment. In the
      package are tests that give you a good starting point.
""",
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
