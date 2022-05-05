from sys import stderr, stdin, stdout
import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#The hostname is IP address of FQDN. Use line#5 if you are logging in with user name and password
ssh.connect(hostname='1.2.3.4',username='xyz',password="testpassword",port=22)
#If using keys instead of password 

ssh.connect(hostname='1.2.3.4',username='xyz',key_filename='/path/to/private/key', port=22)

#Since the command is correct hence the valid output would go in stdout.
stdin, stdout, stderr = ssh.exec_command('whoami')

#This would be printed if the command ran successfully.
print('Output is : ')
print(stdout.readlines())

#This would print out in case if command fails, it will give the fail reason
print('Error is : ')
print(stderr.readlines())
