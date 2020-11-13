import requests
import time
import json
import urllib3

urllib3.disable_warnings()

print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))))

#ck = open('DDG_Cookie.ddg','r')
#Cookie = ck.read()
#print(Cookie) cookies 用html 模拟手机登录m.jd.com 手动登录后，把cookies复制进来。手机端的cookies一般不会过期
#Cookie = '__jdu=1604386397706407879812; pinId=u_u8UHrOB6A; pin=chy386; unick=chy386; ceshi3.com=201; _tp=sdSBWFc7Pmokz1hF6%2FJBXQ%3D%3D; _pst=chy386; __jdc=76161171; areaId=2; ipLoc-djd=2-2834-0-0; shshshfpa=be1f5489-e58a-1aff-4f2a-4c0aec68a700-1604386587; shshshfpb=jRt2gxrG4hzGy8GYQWS3z7Q%3D%3D; unpl=V2_ZzNtbUYDExVwXEdTK0sLAmIFRg1LVhNHJVxBAXIQXwQyChINclRCFnQURlRnGF4UZwcZXkFcRxZFCEdkfxlZDWEzIm1BV3MURQhBVX4bVQJlCxRbQ1BGFHMBQFxyGV81VwMaWXJnHksyXAQHLEYJWlcBGl5FV0MUcw12VUsYbE4JAl9dRVZGF3wPRFx9H10CYgIUVERfShV2OEdkeA%3d%3d; __jda=76161171.1604386397706407879812.1604386398.1604386398.1604388173.2; __jdv=76161171%7Ckong%7Ct_51497_%7Ctuiguang%7C5ea14e06acf647ea80acae6d8820d81a%7C1604388173914; thor=EB7B1170439498A52C8FA160506EAA9481BC833898B93A4F23192D5B917D2011B90D6391E70C1D6D5E42EE6E4128A19C8EC31321CD79A5E076FCB9686E411517B2ED710C7B157BC6ED2F553315E40D29FAF36277CB69E6F1183178C508213833F1D7C5BA9F6B20305FC75C46BE9595B8A1E5D0AB3EAB1E028FB45703689AD78F; wxa_level=1; jxsid=16043885726556474104; webp=1; mba_muid=1604386397706407879812; visitkey=51466605196176922; 3AB9D23F7A4B3C9B=G3PEFOCCRYKKQTB5Y3BD5YD3QHWF3MHBB22ECH3MF7IJMMCX5ARJIYFNMN2GAW2XCBAQ34GGXJRVWRWUTK2VXSJ3QY; TrackerID=bUzRfghPy6GH82jek05b6t8kVlGaF1OfPOXbHhzZ8Rjbt6vC5_sei2Bd0UEBE6LpY-cE7UBrzxxhzwkzNSWvoGME0nDlj0Vau68X1veXiQPNWk2Vu6Z2KgAqgBI7VFmm; pt_key=AAJfoQd_ADCc0JQTI5FQDfddEl-r9Db1HiBiaK-48UO6VdRETNMeEPIHSPVxevAIClrjQslKn88; pt_pin=chy386; pt_token=6kzn03ti; pwdt_id=chy386; sfstoken=tk01me4c21da6a8sMisxKzF4MisyX2ha6AgvdF7tk9bp2bbIfBvdJ67tyD2dyt5KUtJnhSRczvuf7WxcvD2uLigtNg2O; retina=1; cid=9; wqmnx1=MDEyNjM1M3BobWN5ZWVpY2F1Ly8ubzEwMTJsLmkgby5lNWxBIGVpNyhMa2NDZTAwIGxmNTYzWWRmNDNWUkRGSCZS; __jdb=76161171.6.1604386397706407879812|2.1604388173; mba_sid=16043885728159883682615017426.3; __wga=1604388736687.1604388736687.1604388736687.1604388736687.1.1; PPRD_P=UUID.1604386397706407879812; jxsid_s_t=1604388736784; jxsid_s_u=https%3A//home.m.jd.com/myJd/newhome.action; sc_width=400; shshshfp=38d1fb49ecc6ab6c4bb740ae70d37278; shshshsID=14bc4d0eeb4a38a3f8db145d6fdda8e4_6_1604388737257'
Cookie=''

headers = {
    'User-Agent': 'jdapp;Mozilla/5.0 (Linux; U; Android 7.0; zh-CN; BAC-TL00 Build/HUAWEIBAC-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.6.4.950 UCBS/2.11.1.28 Mobile Safari/537.36 AliApp(TB/7.3.0.9) WindVane/8.3.0 1080X1812',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://h5.m.jd.com',
    'Referer': 'https://pro.m.jd.com/mall/active/3gSzKSnvrrhYushciUpzHcDnkYE3/index.html',
    'Cookie':Cookie
}

def get_starId():
    url = 'https://urvsaggpt.m.jd.com/guardianstar/getFrontConfig?t=&starId=fangtai'
    response = requests.get(url,verify=False).json()
    if response.get('code','') == 200:
        res = response.get('data','').get('shareInfo','').get('shareMessage','')
        starIds = []
        for i in res:
            starIds.append(i.get('starId',''))
        print(starIds)
        return starIds
    else:
        print('其他')

def add_jd(starId,types,ids,status):
    url = 'https://urvsaggpt.m.jd.com/guardianstar/doTask'
    data = 'starId=%s&type=%s&id=%s&status=%s' % (starId,types,ids,status)
    try:
        response = requests.post(url,data=data,headers=headers,verify=False).json()
        if response.get('code','') == 200 and status == 1:
            print('店铺：%s进入成功' % ids)
            return 0
        elif response.get('code','') == 200 and status == 2:
            bean_num=response.get('data','').get('bean','')
            star_num=response.get('data','').get('star','')
            print('领取成功，获得{}个京豆,{}守护星'.format(bean_num,star_num))
            return bean_num
        else:
            print(response.get('msg',''))
            return 0
    except:
        print('其他')

def get_task(starId):
    # url1 = 'https://urvsaggpt.m.jd.com/guardianstar/getFrontConfig?t=%s&starId=%s' % (int(round(time.time() * 1000)),starId)
    # url2 = 'https://urvsaggpt.m.jd.com/guardianstar/getPrizeNotice?t=%s&starId=%s' % (int(round(time.time() * 1000)+10),starId)
    # url3 = 'https://urvsaggpt.m.jd.com/guardianstar/getActivityConfig?t=%s&starId=%s' % (int(round(time.time() * 1000)+20),starId)
    # url4 = 'https://urvsaggpt.m.jd.com/guardianstar/getRule?t=%s&starId=%s' % (int(round(time.time() * 1000)+30),starId)
    bean_num =0
    url = 'https://urvsaggpt.m.jd.com/guardianstar/getHomePage?t=%s&starId=%s' % (int(round(time.time() * 1000)+40),starId)
    try:
        # resp = requests.get(url1,verify=False,headers=headers).json()
        # resp = requests.get(url2,verify=False,headers=headers).json()
        # resp = requests.get(url3,verify=False,headers=headers).json()
        # resp = requests.get(url4,verify=False,headers=headers).json()

        response = requests.get(url,verify=False,headers=headers).json()
        if response.get('code','') == 200:
            res = response.get('data','')[0]
            venueIdlist = []
            productIdlist = []
            #任务2
            for i in res.get('venueList',''):
                if i.get('venueStatus','') != 3:
                    venueId = i.get('venueId','')
                    bean_num+=add_jd(starId, 'venue',venueId, 1)
                    venueIdlist.append(venueId)
                    time.sleep(1)
            #任务3
            for j in res.get('productList',''):
                if j.get('productStatus') != 3:
                    productId = j.get('productId','')
                    bean_num+=add_jd(starId, 'product',productId, 1)
                    productIdlist.append(productId)
                    time.sleep(1)
            lens = len(venueIdlist) + len(productIdlist)
            if lens > 10:
                pass
            elif lens == 0:
                pass
            else:
                len_num = 10 - lens
                print('等%s秒在继续' % len_num)
                time.sleep(len_num)
            #领取
            for i in res.get('venueList',''):
                if i.get('venueStatus','') != 3:
                    venueId = i.get('venueId','')
                    bean_num+=add_jd(starId, 'venue',venueId, 2)
                    time.sleep(1)
            for j in res.get('productList',''):
                if j.get('productStatus') != 3:
                    productId = j.get('productId','')
                    bean_num+=add_jd(starId, 'product',productId, 2)
                    time.sleep(1)
            return bean_num
        else:
            print(response.get('msg',''))
            return  bean_num
    except:
        print('其他')
        return bean_num

starIds = get_starId()
beanm_num_total=0
for starId in starIds:
    beanm_num_now=get_task(starId)
    beanm_num_total=beanm_num_total+beanm_num_now
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))))
print('领取成功，共获得{}个京豆'.format(beanm_num_total))
f = open('/python_project/jd/log.txt', 'a+')
f.write('{}领取成功，共获得{}个京豆'.format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(time.time()))),beanm_num_total))
