"""
This script demonstrates how to create a bare-bones, fully functional
chatbot using PyAIML.
"""
from __future__ import print_function

import os.path
import sys
import argparse

import aiml


if sys.version_info[0] == 3:
    raw_input = input


def read_args():
    '''
    Read command-line arguments
    '''
    parser = argparse.ArgumentParser(description='Simple interactive bot')

    g1 = parser.add_argument_group( 'Bot definition' )
    g11 = g1.add_mutually_exclusive_group( required=True )
    g11.add_argument( '--standard', '-s', action='store_true',
                      help='Load the Standard AIML Set' )
    g11.add_argument( '--aiml', nargs='+', help='Load AIML file(s)' )
    g11.add_argument( '--brain', metavar='BRAINFILE',
                      help='Load a dumped brain file' )

    g2 = parser.add_argument_group( 'Options' )
    g2.add_argument( '--chdir', metavar='DIRECTORY',
                     help='Directory to change to before loading AIML files' )
    g2.add_argument( '--commands', '-c', metavar='COMMAND', nargs='+',  
                     default=[],
                     help='Optional command(s) to send to kernel after data loading' )

    g3 = parser.add_argument_group( 'Actions' )
    g3.add_argument( '--save', metavar='FILENAME',
                     help='Dump the loaded brain to a file' )
    g3.add_argument( '--interactive', '-i', action='store_true',
                     help='Enter interactive mode' )

    return parser.parse_args()


def main():
    args = read_args()

    # Create a Kernel object. No string encoding (all I/O is unicode)
    kern = aiml.Kernel()
    kern.setTextEncoding( None )

    # Use the Kernel's bootstrap() method to initialize the Kernel. The
    # optional learnFiles argument is a file (or list of files) to load.
    # The optional commands argument is a command (or list of commands)
    # to run after the files are loaded.
    # The optional branFile argument specifies a brain file to load.
    if args.standard:
        chdir = os.path.join( aiml.__path__[0],'botdata','standard' )
        kern.bootstrap(learnFiles="startup.xml", commands="load aiml b",
                       chdir=chdir)
    elif args.aiml:
        kern.bootstrap(learnFiles=args.aiml, commands=args.commands,
                       chdir=args.chdir)
    elif args.brain:
        kern.bootstrap(brainFile=args.brain)

    if args.save:
        kern.saveBrain(args.save)
    if args.interactive:
        # Enter the main input/output loop.
        print( "\nINTERACTIVE MODE (ctrl-c to exit)" )
        try:
            while True:
                print( kern.respond(raw_input("> ")) )
        except KeyboardInterrupt:
            print( 'Interrupted!' )


if __name__ == '__main__':
    main()
