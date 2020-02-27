"""
Given a list of filenames, we want to rename all the files with the extension hpp to the extension h by generating a list of tuples of the form (old_name, new_name).

That is, given the following list of filenames

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

complete the starter code to generate the following newfilenames list of tuples

newfilenames = [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
"""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []

def create_new_file_name(filenames):
    new_ext = '.h'
    old_ext = '.hpp'
    
    for file in filenames:
        if old_ext in file:
            new_file = file.replace(old_ext, new_ext)
            tup = (file,new_file)
            newfilenames.append(tup,)
            
        else:
            tup2 = (file,file)
            newfilenames.append(tup2,)
        
create_new_file_name(filenames)
print (newfilenames)