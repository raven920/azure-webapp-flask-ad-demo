
import io

from setuptools import find_packages
from setuptools import setup

setup(
    name="lamejorwebapp",
    version="1.0.0",
    url="http://lamejor.ideashock.net/",
    license="BSD",
    maintainer="Christian Delany",
    maintainer_email="raven@ideashock.net",
    description="Aplicación que demuestra el uso de Azure AD",
    #long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask", "werkzeug", "flask-session", "requests", "msal"],
    extras_require={},
)