import platform
import sys
import os

from setuptools import find_packages, setup



def findRequirements():
  """
  Read the requirements.txt file and parse into requirements for setup's
  install_requirements option.
  """
  return [
    line.strip()
    for line in open("requirements.txt").readlines()
    if not line.startswith("#")
    ]



depLinks = []



# If we wanted to use nupic
# if "linux" in sys.platform and platform.linux_distribution()[0] == "CentOS":
#  depLinks = [ "https://pypi.numenta.com/pypi/nupic",
#               "https://pypi.numenta.com/pypi/nupic.bindings" ]


def read(fname):
  """
  Utility function to read specified file.
  """
  path = os.path.join(os.path.dirname(__file__), fname)
  return open(path).read()



setup(name="cloudbrain",
      version="0.2.1",
      description="Platform for wearable data analytics.",
      author="Marion Le Borgne",
      url="https://github.com/marionleborgne/cloudbrain",
      packages=find_packages(),
      install_requires=findRequirements(),
      include_package_data=True,
      dependency_links=depLinks,
      long_description=read("README.md"),
      license='GNU Affero General Public License v3',
      classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3'
      ],
      entry_points={
        'console_scripts': [
          'cloudbrain = cloudbrain.run:main'
        ]
      })


# import os
# from setuptools import setup, find_packages
# from pip.req import parse_requirements
# 
# 
# 
# # parse_requirements() returns generator of pip.req.InstallRequirement objects
# install_reqs = parse_requirements("requirements.txt")
# 
# # reqs is a list of requirement
# # e.g. ['django==1.5.1', 'mezzanine==1.4.6']
# reqs = [str(ir.req) for ir in install_reqs]
# 
# 
# 
# def read(fname):
#   """
#   Utility function to read specified file.
#   """
#   path = os.path.join(os.path.dirname(__file__), fname)
#   return open(path).read()
# 
# 
# 
# setup(name="cloudbrain",
#       version="0.2.1",
#       description=("Platform for real-time sensor data analysis and 
#                     visualization."),
#       packages=find_packages(),
#       install_requires=reqs,
#       include_package_data=True,
#       long_description=read("README.md"),
#       license='GNU Affero General Public License v3',
#       classifiers=[
#           'License :: OSI Approved :: GNU Affero General Public License v3'
#       ],
#       entry_points = {
#         'console_scripts': [
#             'cloudbrain = cloudbrain.run:main'
#         ]
#       })
