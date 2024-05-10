#!/usr/bin/python3
import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]

    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        # help greet will show the documentation line of the function
        # but it's bette to use a special method help_greet to format the help string
        if person:
            print ("hi,", person)
        else:
            print ('hi')
    
    def help_greet(self):
        print ('\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ]))
    
    def complete_greet(self, text, line, begidx, endidx):
        # completes the command
        if not text: # if text is empty , means no letters been written
            completions = self.FRIENDS[:] # print the whole list of friends
        else:
            completions = [ f
                            for f in self.FRIENDS
                            if f.startswith(text)
                            ] # print all the names starts with the text content
        return completions
    
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print

if __name__ == '__main__':
    HelloWorld().cmdloop()
