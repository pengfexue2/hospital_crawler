#!/usr/bin/env python
# encoding: utf-8
# @Time : 2020-03-22 20:50

__author__ = 'Ted'

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame


def get_hospital(zone_url, hospital_dict):
    headers2 = {"User-Agent": "", "Cookie": ""}
    zone_content = requests.get(zone_url, headers=headers2)

    # rint(zone_content.text)
    zone_soup = BeautifulSoup(zone_content.text, "html.parser")
    zone_target = zone_soup.find_all("div", class_="listItem")
    # print(zone_target)

    for item in zone_target:
        name = item.a.get_text(strip=True)
        # print(name)
        a_label = item.find_all("a")[0]
        # print(a_label['href'])
        hospital_dict[name] = a_label['href']
        # print()
    next_url = None
    next_page = zone_soup.find("div", class_="endPage")
    if next_page:
        next_link = next_page.find("a", class_="next")
        if next_link:
            next_url = next_link["href"]

    return hospital_dict, next_url


headers = {"User-Agent":"","Cookie":""}
xian_url="https://yyk.familydoctor.com.cn/area_305_0_0_0_1.html"
content = requests.get(xian_url,headers=headers)
#print(content.text)

xian_soup = BeautifulSoup(content.text,"html.parser")
target = xian_soup.find("div",class_="selection")
area_list = target.find_all("li")[1:]
area_dict={}
for area in area_list:
    area_name = area.get_text(strip=True)
    area_dict[area_name]=area.a["href"]
print(area_dict)

hospitals = {}
for zone in area_dict:
    hospitals,next_page = get_hospital(area_dict[zone],hospitals)
    while next_page:
        hospitals,next_page = get_hospital(next_page,hospitals)
    print(f"{zone} 医院信息已获取完毕...")

print(hospitals)
#hospitals={'西安市红会医院': 'https://yyk.familydoctor.com.cn/17097/', '陕西省中医医院': 'https://yyk.familydoctor.com.cn/16920/', '西安市第五医院': 'https://yyk.familydoctor.com.cn/16808/', '西安莲湖华中医院': 'https://yyk.familydoctor.com.cn/17002/', '陕西西京中医医院': 'https://yyk.familydoctor.com.cn/16999/', '西安莲湖中童儿童康复医院': 'https://yyk.familydoctor.com.cn/16929/', '陕西省皮肤性病防治所': 'https://yyk.familydoctor.com.cn/16909/', '西安北方中医皮肤病医院': 'https://yyk.familydoctor.com.cn/20508/', '西安莲湖长城医院': 'https://yyk.familydoctor.com.cn/21384/', '西安中际中西医结合脑病医院': 'https://yyk.familydoctor.com.cn/20871/', '西安莲湖大唐医院(男科)': 'https://yyk.familydoctor.com.cn/20909/', '西安莲湖国豪医院': 'https://yyk.familydoctor.com.cn/20534/', '西安莲湖生殖医院': 'https://yyk.familydoctor.com.cn/20994/', '西安市莲湖区红十字会医院': 'https://yyk.familydoctor.com.cn/16933/', '西安市莲湖区妇幼保健站': 'https://yyk.familydoctor.com.cn/16959/', '西安市莲湖区中医院': 'https://yyk.familydoctor.com.cn/16968/', '西安市立山医院': 'https://yyk.familydoctor.com.cn/16973/', '西安市莲湖区庙后街医院': 'https://yyk.familydoctor.com.cn/16993/', '西安市莲湖区青年路医院': 'https://yyk.familydoctor.com.cn/16995/', '西安莲湖华西医院': 'https://yyk.familydoctor.com.cn/20531/', '西安莲湖京科医院': 'https://yyk.familydoctor.com.cn/21062/', '西安市莲湖区西关医院': 'https://yyk.familydoctor.com.cn/16990/', '陕西地质矿产局职工医院': 'https://yyk.familydoctor.com.cn/16946/', '西安莲湖北大医院': 'https://yyk.familydoctor.com.cn/21291/', '西安市莲湖区红庙坡医院': 'https://yyk.familydoctor.com.cn/16936/', '西安远东医院': 'https://yyk.familydoctor.com.cn/16970/', '西安炎黄中医专科医院': 'https://yyk.familydoctor.com.cn/16997/', '西安冶金机械厂职工医院': 'https://yyk.familydoctor.com.cn/16976/', '陕西省第一建筑工程公司职工医院': 'https://yyk.familydoctor.com.cn/16982/', '西安市莲湖区北关医院': 'https://yyk.familydoctor.com.cn/16985/', '西安市莲湖区桃园路医院': 'https://yyk.familydoctor.com.cn/16988/', '陕西省邮电医院': 'https://yyk.familydoctor.com.cn/16949/', '西安市第二医院': 'https://yyk.familydoctor.com.cn/16955/', '西安新城仁爱皮肤病医院': 'https://yyk.familydoctor.com.cn/20710/', '陕西省地方病防治研究所': 'https://yyk.familydoctor.com.cn/16915/', '庆安宇航设备厂职工医院': 'https://yyk.familydoctor.com.cn/16942/', '西安都市医院': 'https://yyk.familydoctor.com.cn/20853/', '西安市中医医院': 'https://yyk.familydoctor.com.cn/17013/', '西安市第四医院': 'https://yyk.familydoctor.com.cn/17011/', '西安市中心医院': 'https://yyk.familydoctor.com.cn/16918/', '陕西省妇幼保健院': 'https://yyk.familydoctor.com.cn/16791/', '西安交通大学口腔医院': 'https://yyk.familydoctor.com.cn/17016/', '陕西省第二人民医院': 'https://yyk.familydoctor.com.cn/17008/', '中国人民解放军三二三医院': 'https://yyk.familydoctor.com.cn/17102/', '西电集团医院': 'https://yyk.familydoctor.com.cn/17018/', '西安圣和医院': 'https://yyk.familydoctor.com.cn/17088/', '西安新城中大耳鼻喉医院': 'https://yyk.familydoctor.com.cn/17618/', '西安古城医院肿瘤防治分院': 'https://yyk.familydoctor.com.cn/17024/', '西安市新城区中医院': 'https://yyk.familydoctor.com.cn/17029/', '西安市新城区胡家庙医院': 'https://yyk.familydoctor.com.cn/17072/', '陕西省西铁肿瘤医院': 'https://yyk.familydoctor.com.cn/17076/', '西安市按摩医院': 'https://yyk.familydoctor.com.cn/17080/', '西安市东方医院': 'https://yyk.familydoctor.com.cn/17052/', '西安武仁医院': 'https://yyk.familydoctor.com.cn/17039/', '西安市北方医院': 'https://yyk.familydoctor.com.cn/17045/', '西安市东郊第一职工医院': 'https://yyk.familydoctor.com.cn/17048/', '西安市东郊第二职工医院': 'https://yyk.familydoctor.com.cn/17065/', '西安新城白癫风专科医院': 'https://yyk.familydoctor.com.cn/17083/', '西安市昆仑医院': 'https://yyk.familydoctor.com.cn/17059/', '西安市第六医院': 'https://yyk.familydoctor.com.cn/17027/', '西安市新城区兴庆医院': 'https://yyk.familydoctor.com.cn/17034/', '西安市华山中心医院': 'https://yyk.familydoctor.com.cn/17036/', '西安市东郊第三职工医院': 'https://yyk.familydoctor.com.cn/17067/', '西安市东郊第四职工医院': 'https://yyk.familydoctor.com.cn/17071/', '西安仁爱白癜风医院': 'https://yyk.familydoctor.com.cn/20938/', '西安黄河医院': 'https://yyk.familydoctor.com.cn/17042/', '陕西省建材医院': 'https://yyk.familydoctor.com.cn/17051/', '西安市新城区第二医院': 'https://yyk.familydoctor.com.cn/17056/', '西安市新城区妇幼保健院': 'https://yyk.familydoctor.com.cn/17021/', '西安太华医院': 'https://yyk.familydoctor.com.cn/17062/', '西京医院': 'https://yyk.familydoctor.com.cn/21413/', '西安远大中医皮肤病医院': 'https://yyk.familydoctor.com.cn/20901/', '西安交通大学医学院第二附属医院': 'https://yyk.familydoctor.com.cn/17584/', '陕西省人民医院': 'https://yyk.familydoctor.com.cn/17095/', '西安市第一医院': 'https://yyk.familydoctor.com.cn/17113/', '西安市第九医院': 'https://yyk.familydoctor.com.cn/17352/', '中国人民解放军四五一医院': 'https://yyk.familydoctor.com.cn/17111/', '西安胃泰消化病医院': 'https://yyk.familydoctor.com.cn/21442/', '陕西远大男病专科医院': 'https://yyk.familydoctor.com.cn/21436/', '西安学典医院': 'https://yyk.familydoctor.com.cn/17092/', '西安慈爱妇产医院': 'https://yyk.familydoctor.com.cn/21033/', '西安生殖保健院': 'https://yyk.familydoctor.com.cn/17572/', '陕西省老医协生殖医学医院妇科': 'https://yyk.familydoctor.com.cn/20747/', '西安协同医院': 'https://yyk.familydoctor.com.cn/17198/', '陕西省老医协生殖医学医院': 'https://yyk.familydoctor.com.cn/17118/', '西安华仁医院': 'https://yyk.familydoctor.com.cn/21249/', '西安市碑林区东大街医院': 'https://yyk.familydoctor.com.cn/17127/', '西安市碑林区中医院': 'https://yyk.familydoctor.com.cn/17179/', '西安市碑林区红十字会医院': 'https://yyk.familydoctor.com.cn/17137/', '陕西省交通医院': 'https://yyk.familydoctor.com.cn/17139/', '西安宇恒医院': 'https://yyk.familydoctor.com.cn/17151/', '西安华夏医院': 'https://yyk.familydoctor.com.cn/17162/', '西安市碑林区口腔医院': 'https://yyk.familydoctor.com.cn/17175/', '西安市碑林区南大街医院': 'https://yyk.familydoctor.com.cn/17180/', '西安市碑林区东关医院': 'https://yyk.familydoctor.com.cn/17187/', '西安肝硬化医院': 'https://yyk.familydoctor.com.cn/17122/', '西安市眼科医院': 'https://yyk.familydoctor.com.cn/17123/', '西安市红十字会医院骨伤分院': 'https://yyk.familydoctor.com.cn/17116/', '陕西省公路局职工医院': 'https://yyk.familydoctor.com.cn/17143/', '西安市皇城医院': 'https://yyk.familydoctor.com.cn/17147/', '西安南关医院': 'https://yyk.familydoctor.com.cn/17149/', '西安华佗医院': 'https://yyk.familydoctor.com.cn/17159/', '西安民建中医院': 'https://yyk.familydoctor.com.cn/17168/', '西安市红缨路医院': 'https://yyk.familydoctor.com.cn/17146/', '西安工程科技大学医院': 'https://yyk.familydoctor.com.cn/17154/', '西安华医医院': 'https://yyk.familydoctor.com.cn/17169/', '西安精英医院': 'https://yyk.familydoctor.com.cn/17131/', '陕西省康复中心': 'https://yyk.familydoctor.com.cn/17194/', '西安市碑林区妇幼保健站': 'https://yyk.familydoctor.com.cn/17186/', '西安大同医院': 'https://yyk.familydoctor.com.cn/17156/', '西安友谊中医院': 'https://yyk.familydoctor.com.cn/17133/', '西安市南天医院': 'https://yyk.familydoctor.com.cn/17135/', '西安唐都医院': 'https://yyk.familydoctor.com.cn/17204/', '陕西省纺织医院': 'https://yyk.familydoctor.com.cn/17203/', '西安市灞桥区人民医院': 'https://yyk.familydoctor.com.cn/17210/', '西安市灞桥区红十字会医院': 'https://yyk.familydoctor.com.cn/17230/', '西安市灞桥区中医院': 'https://yyk.familydoctor.com.cn/17226/', '西安市灞桥区精神病院': 'https://yyk.familydoctor.com.cn/17219/', '西安市灞桥区妇幼保健站': 'https://yyk.familydoctor.com.cn/17221/', '西安市亚西光电仪器厂职工医院': 'https://yyk.familydoctor.com.cn/17233/', '西安长安医院': 'https://yyk.familydoctor.com.cn/17241/', '西安古城眼科医院': 'https://yyk.familydoctor.com.cn/17325/', '西安市康复医院': 'https://yyk.familydoctor.com.cn/17331/', '西安市未央区第一人民医院': 'https://yyk.familydoctor.com.cn/17244/', '西安惠仁医院': 'https://yyk.familydoctor.com.cn/17287/', '西安市未央区二府庄医院': 'https://yyk.familydoctor.com.cn/17315/', '西安市未央区草滩医院': 'https://yyk.familydoctor.com.cn/17317/', '西安郭家村工商公司医院': 'https://yyk.familydoctor.com.cn/17324/', '西安市未央区大明宫骨科医院': 'https://yyk.familydoctor.com.cn/17259/', '西安协和医院': 'https://yyk.familydoctor.com.cn/17277/', '西安太和医院': 'https://yyk.familydoctor.com.cn/17286/', '西安阳光医院': 'https://yyk.familydoctor.com.cn/17293/', '西安交通大学第二附属医院皮肤病院': 'https://yyk.familydoctor.com.cn/16859/', '西安华山中医皮肤病医院': 'https://yyk.familydoctor.com.cn/21131/', '西安市未央区第二人民医院': 'https://yyk.familydoctor.com.cn/17248/', '西安航空发动机公司职工医院': 'https://yyk.familydoctor.com.cn/17269/', '西安张家堡肛肠医院': 'https://yyk.familydoctor.com.cn/17304/', '陕西第十棉织厂医院': 'https://yyk.familydoctor.com.cn/17312/', '西安市唐城医院': 'https://yyk.familydoctor.com.cn/17267/', '西安市未央区未央宫医院': 'https://yyk.familydoctor.com.cn/17281/', '西安未央康乐医院': 'https://yyk.familydoctor.com.cn/17292/', '西安市未央区谭家医院': 'https://yyk.familydoctor.com.cn/17321/', '西安西郊纺织医院': 'https://yyk.familydoctor.com.cn/17274/', '第四军医大学西京医院': 'https://yyk.familydoctor.com.cn/17356/', '西安交通大学第一医院': 'https://yyk.familydoctor.com.cn/17347/', '陕西省肿瘤医院': 'https://yyk.familydoctor.com.cn/17342/', '西安市精神卫生中心': 'https://yyk.familydoctor.com.cn/17366/', '西安高新医院': 'https://yyk.familydoctor.com.cn/17473/', '西安市第八医院': 'https://yyk.familydoctor.com.cn/17494/', '西安天佑医院': 'https://yyk.familydoctor.com.cn/17483/', '西安藻露堂中医医院': 'https://yyk.familydoctor.com.cn/17478/', '西安雁塔友好医院': 'https://yyk.familydoctor.com.cn/21514/', '西安神龙中医院': 'https://yyk.familydoctor.com.cn/17467/', '西安市雁塔截瘫康复医疗中心': 'https://yyk.familydoctor.com.cn/17397/', '西安同仁医院': 'https://yyk.familydoctor.com.cn/17399/', '陕西省新安中心医院': 'https://yyk.familydoctor.com.cn/17401/', '西安雁塔曙光医院': 'https://yyk.familydoctor.com.cn/20620/', '西安市雁塔区等驾坡医院': 'https://yyk.familydoctor.com.cn/17451/', '西安市安康医院': 'https://yyk.familydoctor.com.cn/17413/', '西安公路交通大学医院': 'https://yyk.familydoctor.com.cn/17415/', '西安交通大学医院': 'https://yyk.familydoctor.com.cn/17423/', '西安建筑科技大学医院': 'https://yyk.familydoctor.com.cn/17375/', '陕西省钢厂职工医院': 'https://yyk.familydoctor.com.cn/17445/', '西安市雁塔区中医肿瘤医院': 'https://yyk.familydoctor.com.cn/17430/', '西安二六二医院': 'https://yyk.familydoctor.com.cn/17459/', '西安电力中心医院': 'https://yyk.familydoctor.com.cn/17378/', '西安康太医院': 'https://yyk.familydoctor.com.cn/17411/', '西安电子科技大学医院': 'https://yyk.familydoctor.com.cn/17417/', '西安市雁塔区肿瘤医院': 'https://yyk.familydoctor.com.cn/17427/', '西安中华医院': 'https://yyk.familydoctor.com.cn/17392/', '西安市朱雀医院': 'https://yyk.familydoctor.com.cn/17393/', '陕西博爱医院': 'https://yyk.familydoctor.com.cn/17370/', '西安雁塔区精神病院': 'https://yyk.familydoctor.com.cn/17438/', '西安市雁塔区疑难病医院': 'https://yyk.familydoctor.com.cn/17449/', '陕西正和医院': 'https://yyk.familydoctor.com.cn/17381/', '西安仁芳医院': 'https://yyk.familydoctor.com.cn/17463/', '西安市阎良区铁路医院精神病分院': 'https://yyk.familydoctor.com.cn/17517/', '西安市阎良区中医院': 'https://yyk.familydoctor.com.cn/17503/', '西安阎良精神病医院': 'https://yyk.familydoctor.com.cn/17532/', '西安一四一医院': 'https://yyk.familydoctor.com.cn/17509/', '西安市阎良区人民医院': 'https://yyk.familydoctor.com.cn/17535/', '西安市阎良铁路医院': 'https://yyk.familydoctor.com.cn/17511/', '西安一四一医院分院': 'https://yyk.familydoctor.com.cn/17526/', '西安市阎良区妇幼保健站': 'https://yyk.familydoctor.com.cn/17540/', '第四军医大学口腔医院': 'https://yyk.familydoctor.com.cn/17548/', '临潼县人民医院': 'https://yyk.familydoctor.com.cn/17566/', '临潼县中医院': 'https://yyk.familydoctor.com.cn/17556/', '临潼职业病医院': 'https://yyk.familydoctor.com.cn/17562/', '临潼妇幼保健院': 'https://yyk.familydoctor.com.cn/17557/', '陕西省结核病防治院': 'https://yyk.familydoctor.com.cn/17578/', '西安市结核病胸部肿瘤医院': 'https://yyk.familydoctor.com.cn/17616/', '长安县医院': 'https://yyk.familydoctor.com.cn/17606/', '西安市长安区妇幼保健院': 'https://yyk.familydoctor.com.cn/17614/', '西安长安龙泉医院': 'https://yyk.familydoctor.com.cn/17600/', '西安市长安区精神病院': 'https://yyk.familydoctor.com.cn/17602/', '西安尚德医院': 'https://yyk.familydoctor.com.cn/17595/', '西安类风湿康复中心': 'https://yyk.familydoctor.com.cn/17598/', '西安市长安区中医院': 'https://yyk.familydoctor.com.cn/17611/', '西安长安秦通医院': 'https://yyk.familydoctor.com.cn/17589/', '周至县妇幼保健院': 'https://yyk.familydoctor.com.cn/17647/', '周至县人民医院': 'https://yyk.familydoctor.com.cn/17652/', '周至县会仁医院': 'https://yyk.familydoctor.com.cn/17662/', '周至县镇东联合医院': 'https://yyk.familydoctor.com.cn/17663/', '周至县中医院': 'https://yyk.familydoctor.com.cn/17658/', '高陵县中医院': 'https://yyk.familydoctor.com.cn/17706/', '高陵县妇幼保健院': 'https://yyk.familydoctor.com.cn/17712/', '高陵县医院': 'https://yyk.familydoctor.com.cn/17702/', '高陵县光达眼病医院': 'https://yyk.familydoctor.com.cn/17709/'}


excel_dict={}
df = DataFrame(columns=["医院名称","医院类型","医院等级","医院地址","咨询电话"])
for hospital in hospitals:
    print("医院名称：",hospital)
    hospital_link=hospitals[hospital]
    headers = {"User-Agent":"","Cookie":""}
    hospital_info = requests.get(hospital_link,headers=headers)

    hospital_soup = BeautifulSoup(hospital_info.text,"html.parser")
    temp = hospital_soup.find_all("div",class_="introPic")
    if temp:
        hospital_intro = temp[0]
        #print(hospital_intro)
        detail = hospital_intro.find_all("dl")
        #print(detail)
        temp_dict={}
        for subitem in detail:
            title = subitem.dt.get_text(strip=True)
            if "医院地址" in title:
                answer = subitem.dd.get_text(strip=True)[:-4]
            else:
                answer = subitem.dd.get_text(strip=True)
            temp_dict[title]=answer
            print(title,answer)
    excel_dict[hospital]=temp_dict
    print(temp_dict)
    df=df.append([{"医院名称":hospital,"医院类型":temp_dict["医院类型："],"医院等级":temp_dict["医院等级："],"医院地址":temp_dict["医院地址："],"咨询电话":temp_dict["咨询电话："]}],ignore_index=True)
    print("======================")


df.to_excel("result.xls")
print("结果写入 result.xls")