# Command to build:
from distutils.core import setup
import glob

package_prefix = "Lib/site-packages/aiml"

setup(name="python-aiml",
    version="0.9.0",
    author="Paulo Villegas",
    author_email="paulo.vllgs@gmail.com",
    
    description="An interpreter package for AIML, the Artificial Intelligence Markup Language",
    long_description="""PyAIML implements an interpreter for AIML, the Artificial Intelligence
Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation.
It can be used to implement a conversational AI program.

Forked from PyAIML 0.8.6 (https://github.com/cdwfs/pyaiml)
PyAIML by Cort Stratton (cort@cortstratton.org)
""",
    url="https://github.com/paulovn/python-aiml",
    platforms=["any"],
    classifiers=["Development Status :: 3 - Alpha",
                 "Environment :: Console",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Operating System :: OS Independent",
                 "Topic :: Communications :: Chat",
                 "Topic :: Scientific/Engineering :: Artificial Intelligence"
                 ],
      
    packages=["aiml"],
    package_dir={'aiml': 'aiml'},
    package_data={'aiml': ['standard/*.aiml',
                           'standard/*.xml',
#                           'alice/*.aiml',
#                           'alice/*.xml',
                           '*.txt']},

    data_files=[
        (package_prefix, glob.glob("aiml/self-test.aiml")),
        (package_prefix, glob.glob("*.txt")),
    ],
)
