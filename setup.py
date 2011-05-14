from setuptools import setup
 
version = '0.0.1'
 
LONG_DESCRIPTION = """
=====================================
django-masked-forms (Django masked_forms)
=====================================

"""
 
setup(
    name='django-masked-forms',
    version=version,
    description="django masked forms",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='jQuery,django,mask,form fields',
    author='Mateus Lorandi dos Santos',
    author_email='mcomogo@gmail.com',
    license='MIT',
    packages=['masked_forms'],
    url='https://github.com/comogo/django-masked-forms',
    include_package_data=True,
    exclude_package_data={'': ['example']},
    zip_safe=False,
)
