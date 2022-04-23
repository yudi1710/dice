import requests,json,os
url  = 'https://game.pandaever.com/'
cmd = "cls' if os.name=='nt' else 'clear"
c = requests.session()
with open('config.json', 'r') as f:
        cfg = json.load(f)
apikey = cfg['apikey']
def register():
    os.system(cmd)
    username = input('Username: ')
    pwd = input('Password: ')
    imel = input('Email: ')
    acc = c.get(url+'register?username='+username+'&pass='+pwd+'&email='+imel).text
    if 'Username Not Found/Null' in acc:
        print('Username Not Found/Null')
    elif 'Email Not Found/Null' in acc:
        print('Email Not Found/Null')
    elif 'Password Not Found/Null' in acc:
        print('Password Not Found/Null')
    elif 'Account already exists !' in acc:
        print('Account already exists !')
    else:
        accs = json.loads(acc)
        print('Please Save Apikey,Apikey Used At Playing Dice\nApikey: '+str(accs['apikey'])+'\nUsername: '+accs['username']+'\nPassword: '+pwd+'\nUserID: '+str(accs['id'])+'\nBalance: '+str(accs['balance']))
        menu()
def resetpass(email):
    code = input('Verification Code: ')
    pas = input('New Password: ')
    rescet = c.get(url+'reset?email='+email+'&code='+code+'&pass='+pas).text
    if 'Email Not Found' in rescet:
        print('Email Not Found')
    elif 'Code Not Found' in rescet:
        print('Code Not Found')
    elif 'New Password Not Found' in rescet:
        print('New Password Not Found')
    elif 'Success' in rescet:
        print('Success Update Password\nYour Apikey Is Regenerated,Please Login To See Your New Apikey')
    else:
        print('Wrong Code')
def resetcode():
    os.system(cmd)
    email = input('Email: ')
    sendc = c.get(url+"2fa?email="+email).text
    if 'Email Not Found' in sendc:
        print('Email Not Found')
    else:
        print('Success')
        resetpass(email)
def login():
    os.system(cmd)
    username = input('Username: ')
    pwd = input('Password: ')
    acc = c.get(url+'login?username='+username+'&pass='+pwd).text
    if 'Username Not Found/Null' in acc:
        print('Username Not Found/Null')
    elif 'Password Not Found/Null' in acc:
        print('Password Not Found/Null')
    elif 'Incorrect username / password !' in acc:
        print('Incorrect username / password !')
    else:
        accs = json.loads(acc)
        print('Please Save Apikey,Apikey Used At Playing Dice\nApikey: '+str(accs['apikey'])+'\nUsername: '+accs['username']+'\nUserID: '+str(accs['id'])+'\nBalance: '+str(accs['balance']))
        menu()
def check():
    os.system(cmd)
    bal = c.get(url+'balance?key='+apikey).text
    if 'Api Key Not Found' in bal:
        print('Api Key Not Found')
    elif 'Account Not Found' in bal:
        print('Wrong Api Key')
    else:
        accs = json.loads(bal)
        print('Username: '+accs['Username']+'\nUserID: '+str(accs['Userid'])+'\nBalance: '+str(accs['Balance']))
        menu()
def checkm():
    os.system(cmd)
    bal = c.get(url+'balance?key='+apikey).text
    if 'Api Key Not Found' in bal:
        print('Api Key Not Found')
    elif 'Account Not Found' in bal:
        print('Wrong Api Key')
    else:
        accs = json.loads(bal)
        print('Username: '+accs['Username']+'\nUserID: '+str(accs['Userid'])+'\nBalance: '+str(accs['Balance']))
def tip():
    checkm()
    usr = input("Tip To: ")
    bal = input("Balance: ")
    tips = c.get(url+"tip?username="+usr+"&apikey="+apikey+"&tip="+bal).text
    if 'Username Not Found' in tips:
        print('Username Not Found')
    elif 'Apikey Not Found' in tips:
        print('Apikey Not Found')
    elif 'Tip Amount Not Found' in tips:
        print('Tip Amount Not Found')
    elif 'Apikey Not Registered' in tips:
        print('Apikey Not Registered')
    elif 'Insufficient Balance' in tips:
        print('Insufficient Balance')
    elif 'Username Not Registered' in tips:
        print('Username Not Registered')
    else:
        print(tips)
        menu()
def depo():
    os.system(cmd)
    wal = c.get(url+"deposit?key="+apikey).text
    if 'Api Key Not Found' in wal:
        print('Api Key Not Found')
    elif 'Account Not Found' in wal:
        print('Account Not Found')
    else:
        walle = json.loads(wal)
        print("\n\nAddress: "+walle['wallet']+"\nMin Deposit: "+ walle['Min']+"\nNetwork Shasta Testnet\n\n")
        menu()
def verify():
    os.system(cmd)
    cseed = input("ClientSeed: ")
    serverseed = input("ServerSeed: ")
    nonce = input('nonce: ')
    verif = c.get(url+'verify?clientseed='+cseed+'&serverseed='+serverseed+'&nonce='+nonce).text
    if "ClientSeed Not Found" in verif:
        print('ClientSeed Not Found')
    elif 'ServerSeed Not Found' in verif:
        print('ServerSeed Not Found')
    elif 'nonce Not Found' in verif:
        print('nonce Not Found')
    else:
        os.system(cmd)
        jsn = json.loads(verif)
        print('ClientSeed: '+ str(jsn['clientSeed'])+'\nServerSeed: '+str(jsn['serverSeed'])+'\nResult: '+str(jsn['result'])+'\n')
        menu()
def play():
    os.system(cmd)
    hilo = input('Hi/LO (IF RANDOM TYPE RND): ')
    chance = input('Chance: ')
    playmany = int(input('Play Many Time: '))
    bets = float(input('Bet: '))
    bet = bets
    iflose = int(input('If Lose percent: '))
    ifwin = int(input('If Win percent: '))
    gacha = c.get(url+'result?key='+apikey+'&chance='+chance+'&bet=0&net=1').text
    if 'Api Key Not Found' in gacha:
        print('Apikey Not Found')
    elif 'Insufficient Balance' in gacha:
        print('Insufficient Balance')
    elif 'Chance Not Found' in gacha:
        print('Chance Not Found')
    elif 'chance cannot be less than 5' in gacha:
        print('chance cannot be less than 5')
    elif 'chance cannot be greater than 90' in gacha:
        print('chance cannot be greater than 90')
    elif 'Account Not Found' in gacha:
        print('Wrong Account Apikey')
    else:
        count = 0
        while (count < playmany):
            validations = c.get(url+'result?key='+apikey+'&chance='+chance+'&bet='+str(bet)+'&hilo='+hilo).text
            if 'Insufficient Balance' in validations:
                print('Insufficient Balance')
                break
            acc = json.loads(validations)
            print('HI/LO: '+str(acc['HI/LO'])+'  Status: '+ str(acc['player'])+'  Total Win: '+ str(acc['TotalWin'])+ '  Balance: '+str(acc['Balance'] ))
            if str(acc['player']) == 'LOSE':
                bet = bet * (100 + iflose) / 100
            elif str(acc['player']) == 'WIN ':
                if ifwin == 0:
                    bet = bets
                else:
                    bet = bet * (100 + ifwin) / 100
            count = count + 1 
        menu()
os.system(cmd)
def menu():
    print('1). Register\n2). Login\n3). Check Balance\n4). Play Dice\n5). Reset Password\n6). Tip User\n7). Deposit\n8). Verify Hash')
    choices = int(input('Enter You Choice: '))
    if choices == 1:
        register()
    elif choices == 2:
        login()
    elif choices == 3:
        check()
    elif choices == 4:
        play()
    elif choices == 5:
        resetcode()
    elif choices == 6:
        tip()
    elif choices == 7:
        depo()
    elif choices == 8:
        verify()
    else:
        os.system(cmd)
        print('Invalid Choice')
        menu()
menu()