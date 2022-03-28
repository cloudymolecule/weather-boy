from lib.cli import CommandLineInterface

c = CommandLineInterface()

instance = c.run_program()
while instance == 'Another':
    c = CommandLineInterface()
    instance = c.run_program()


