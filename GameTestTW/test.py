#!/usr/bin/env python
# coding:utf-8

# Author:TiFity
import requests,sys
import json
from utils.logConfig import *


def lagou(page=2):
	url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
	headers = {
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Cookie": "user_trace_token=20190820151838-dd10dc91-c5b5-4cf2-85c5-b8e02ed7c9f1; _ga=GA1.2.762176976.1566285519; LGUID=20190820151838-bb3f81f7-c31a-11e9-8add-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cade4a111a5f-095d53677965f7-37657c05-2073600-16cade4a11297b%22%2C%22%24device_id%22%3A%2216cade4a111a5f-095d53677965f7-37657c05-2073600-16cade4a11297b%22%7D; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=34; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; gate_login_token=d1ea4d7f6f10e90721a20f5866971365a06267e8fe4d2147; LG_LOGIN_USER_ID=9d7e29b87a0b82fff177f1ddf63ee3d9b1b3632e044a5264; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571725678,1571987106; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0PpN-0FNkUsaxMoFI00000AZkiNC00000xNufhL.THL0oUhY1x60UWdBmy-bIfK15H9WPHTvrHF9nj0snj9-PvD0IHYvrjF7njNjfHmvnDDvnDuafH9AnRfYn1DdPbf3wj9KfsK95gTqFhdWpyfqn1c4Pj6krHfvPBusThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUA78uA-8uzdsmyI-QLKWQLP-mgFWpa4CIAd_5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqPWndn0%26tpl%3Dtpl_11534_19968_16032%26l%3D1514795361%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3294819466_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D219%26ie%3Dutf-8%26f%3D3%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn%26inputT%3D2952%26prefixsug%3Dlagou%26rsp%3D0; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGSID=20191025150506-c60d6ca8-f6f5-11e9-a07e-525400f775ce; _putrc=2C63525040A6E1E1; JSESSIONID=ABAAABAAAGFABEF0706187CFBCA64A8A2C27EE1202C5992; login=true; unick=%E5%8D%93%E8%89%B3; WEBTJ-ID=20191025150517-16e01bbd63057b-08ec24475af2a5-123e6a5d-2073600-16e01bbd6329f8; _gid=GA1.2.1747340993.1571987118; SEARCH_ID=dfde39a50fd446f887361464ad46033c; X_HTTP_TOKEN=1716868b2e12cc2571478917512fd1b2555eae86fb; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571987418; LGRID=20191025151017-7fa7a6e2-f6f6-11e9-a07e-525400f775ce",
		"Referer": "https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95",
		"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
	}
	data = {
		"first": "false",
		"pn": 2,
		"kd": "自动化测试工程师",
		"sid": "2a1aad1f2e9d40f9bfd22fb994684a4b"
	}
	data["pn"] = page
	req = requests.post(url=url, headers=headers, data=data)
	# print(req.status_code)
	print(req.text)
	logger.info("sdjfljslfj")
	
	# rs = [["公司名称","城市","地区","薪资","工作年限","公司福利","工作标签"]]
	# rs = []
	# for i in range(0, 15):
	# 	companyFullName = req.json()["content"]["positionResult"]["result"][i]["companyFullName"]
	# 	city = req.json()["content"]["positionResult"]["result"][i]["city"]
	# 	district = req.json()["content"]["positionResult"]["result"][i]["district"]
	# 	workYear = req.json()["content"]["positionResult"]["result"][i]["workYear"]
	# 	salary = req.json()["content"]["positionResult"]["result"][i]["salary"]
	# 	positionAdvantage = req.json()["content"]["positionResult"]["result"][i]["salary"]
	# 	positionLables = req.json()["content"]["positionResult"]["result"][i]["positionLables"]
	#
	# 	position = {
	# 		"公司名称": companyFullName,
	# 		"城市": city,
	# 		"地区": district,
	# 		"薪资": salary,
	# 		"工作年限": workYear,
	# 		"公司福利": positionAdvantage,
	# 		"工作标签": positionLables
	# 	}
	# 	print(position)
	# 	# rs.append([companyFullName,city,district,salary,workYear,positionAdvantage,positionLables])
	# 	rs.append(position)


if __name__ == '__main__':
	# logger.critical('等级我是天下第一，不服来辩!')
	# logger.error('呦呦呦，我说自己是第二，没人敢说自己是第一!')
	# logger.warning('前面两个别吵了，让我这第三情何以堪！')
	# logger.info('各位少侠，别来无恙，区区第四，不值一提!')
	# logger.debug('我排名第五，不接受反驳！我不会说自己是倒数第一的，哼!')
	# lagou()
	pass

	l = [['zy-gs01p2', 'zy-fgs01p2', 'zy-dzj01p2', 'zy-zj01p2'], [680, 681, 682, 683]]
	l2 = [['zy680-1', 'zy681-1', 'zy682-1', 'zy683-1'], [16, 17, 18, 19]]
	
	l3=[['zy-gs01p3', 'zy-fgs01p3', 'zy-dzj01p3', 'zy-zj01p3'], [684, 685, 686, 687]]
	l4=[['zy684-1', 'zy685-1', 'zy686-1', 'zy687-1'], [20, 21, 22, 23]]

