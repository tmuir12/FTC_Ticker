import requests
    #returns current feathercoin value in Australian Dollars
    #To change currency change 'aud' in code below to one of the option 
    #below
    #aud = (Australia), eur = Euro, gbp = Great Britain 
    #nzd = New Zealand, usd = United Sates
    #thanks to Uncle_Muddy on the feathercoin forum for the API call code
    
def toFTC(v,c='aud',j='0'):
    payload = {'output': c, 'amount': v, 'json': j}
    to_ftc_url = 'http://api.feathercoin.com/'
    ftotal=-1
    try:
        r = requests.get(to_ftc_url, params=payload)
        
        if r.status_code == 200:
            ftotal = round(float(r.text) ,4)
    except:
        pass
    return ftotal
