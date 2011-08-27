from distutils.core import setup

long_description = open('README.md').read()

setup(name="python-crunchbase",
      version="1.0.2",
      py_modules=["crunchbase"],
      description="Libraries for interacting with the Crunchbase API",
      author="Apurva Mehta <mehta.apurva@gmail.com>",
      author_email = "mehta.apurva@gmail.com",
      license="WTFPL",
      url="http://github.com/amehta/crunchbase",
      long_description=long_description,
      platforms=["any"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
       install_requires=["simplejson >= 1.8"]
      )

