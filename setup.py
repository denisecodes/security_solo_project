from setuptools import find_packages, setup

# are packages up to date? upgrade to latest version to make it more secure and protected from latest vulnerabilities
setup(
    name='login_form',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'seleniumbase',
        'faker'
    ],
)