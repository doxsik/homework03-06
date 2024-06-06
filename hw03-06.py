login_base = {}
admin_base = {'admin': 500}

login = str(input('Введите ваш логин: '))

def isadmin(login):
    if login in admin_base.keys():
        admin = True
    else:
        admin = False
    return admin

if isadmin(login) == False:
    login_base.update(login=0)

def admincheck(cash_func):
    def wrapper(arg):
        if isadmin(arg) == True:
            cash = cash_func(arg)
            return cash
        else:
            print("Доступ запрещен.")
    return wrapper

@admincheck
def cash(login):
    if isadmin(login) == True:
        login_cash = admin_base[login]
    else:
        login_cash = login_base[login]
    print(f'Ваш баланс: {login_cash}')
    return login_cash

cash(login)