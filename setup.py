from setuptools import setup

setup(
    name='nso_test_restconf',
    version='0.2.0',
    description='A library for testing NSO via RESTCONF',
    url='',
    author='wholechainsawit',
    author_email='',
    license='BSD 2-clause',
    packages=['nso_test_restconf'],
    install_requires=['requests'
                      ],
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
