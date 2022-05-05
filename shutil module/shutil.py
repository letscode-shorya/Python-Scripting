'''shutil module provides us a number of high-level operations 
on files and folders/directories like copy, move, remove and much more'''

from pydoc import describe
import shutil

#copying files with shutil using copyfile()
#If copyfile() is used then in case if the dest file is already present it will throw and error 
#also it will create a new file with a different date and diff sets of permissions
src = "/home/automation/remote_script.py"
dst = "/home/automation/remote_script.py_backup"
shutil.copyfile(src,dst)

#If copy is used then the permission of new file would be the same as the source file, although the entire metadata won't be preserved

shutil.copy(src,dst)

#If you want al metadata to be preserved including modified date hence use copy2 

shutil.copy2(src,dst)

#If you want to copy a permission of one file to another use copymode()
#Lets say if srcfile.txt has permission '700' then the destfile.txt would be given the same permission as well
#But for this to work both the src and dest files should be present
cpm_src = '/home/Shorya/srcfile.txt'
cpm_dest = '/home/Shorya/destfile.txt'

#If you want to copy entire directory structure to an other directory then use copytree() 

shutil.copytree(src='/var/log/httpd',dest='/home/Shorya/Desktop/httpd')

#If you want to remove any directory recursively then use rmtree() with desination 

shutil.rmtree('/home/Shorya/Desktop/httpd')

