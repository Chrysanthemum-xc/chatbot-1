import re,aiml,os,random,database
os.chdir('alice')
bot_template = "BOT : {0}"

alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')

sayYou = ['goodBye','See you tomorrow','Tanke You','bye bye!!']
TellnamesTemplate = ['Which stock is it, please ','please tell me the Name of stock','Name the stock']
DateTemplate = ['Please tell me the date','date','Is it for today']
byes = ['bye','Bye','See you tomorrow','good Bye','Good bye','good bye','Good Bye','good Bye','Goodbye','goodbye','GoodBye']
secondMessage = ['price','volume','market value']
def generateOneRules():
    rules = {
             #询问股票价格
             'I want to know stocks (.*)':['price','volume','market value'],
             'Tell me today stocks (.*)':['price','volume','market value'],
             'Please tell me stocks (.*)':['price','volume','market value'],
        'i want to know stocks (.*)': ['price', 'volume', 'market value'],
        'tell me today stocks (.*)': ['price', 'volume', 'market value'],
        'please tell me stocks (.*)': ['price', 'volume', 'market value'],

             }
    return rules

def tellAlice(str):
    res =alice.respond(str)
    print(bot_template.format(res))

def bye(str):
    for item in byes:
        if str in item:
            return True
    return False
def sayBye():
    say = random.choice(sayYou)
    return bot_template.format(say)


def processPrice():
    print(bot_template.format(random.choice(TellnamesTemplate)))
    name = input('USER: ')
    print(bot_template.format(random.choice(DateTemplate)))
    date = input('USER: ')
    if date not in 'yes today':
        print(bot_template.format("Sorry, I only know today's information"))
    else:
        res = database.searchByName(name)
        print(bot_template.format(res))


def processVolume():
    print(bot_template.format(random.choice(TellnamesTemplate)))
    name = input('USER: ')
    print(bot_template.format(random.choice(DateTemplate)))
    date = input('USER: ')
    if date not in 'yes today':
        print(bot_template.format("Sorry, I only know today's information"))
    else:
        res = database.searchByNameReturnVolum(name)
        print(bot_template.format(res))

def processMarket():
    print(bot_template.format(random.choice(TellnamesTemplate)))
    name = input('USER: ')
    print(bot_template.format(random.choice(DateTemplate)))
    date = input('USER: ')
    if date not in 'yes today':
        print(bot_template.format("Sorry, I only know today's information"))
    else:
        res = database.searchByNameReturnMarket(name)
        print(bot_template.format(res))


def processRequest(message):
    response = None
    rules = generateOneRules()
    for pattern,items in rules.items():
       match =  re.search(pattern,message)
       if match is not None:
            item = match.group(1)
            response = Handler(item)
       elif message in pattern:
           print(bot_template.format("Please tell me some details Please tell me some details, such as stock price, market value,volume"))
           twoMessage = input("USER: ")
           result = In(twoMessage)
           Handler(result)
    if response is None:
        tellAlice(message)

def In(twoMessage):
    for i in secondMessage:
        if twoMessage in i:
            return i
    return None
def Handler(item):
    if item == 'price':
        processPrice()
        return "yes"
    elif item == 'volume':
        processVolume()
        return "yes"
    elif item in 'market value':
        processMarket()
        return "yes"