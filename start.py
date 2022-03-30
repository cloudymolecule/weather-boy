from lib.cli import CommandLineInterface

c = CommandLineInterface()

instance = c.run_program()
while instance == 'Another': 
    # in case the user selects another location the loop starts over
    # and a new instance of the interface is created
    c = CommandLineInterface()
    instance = c.run_program()


