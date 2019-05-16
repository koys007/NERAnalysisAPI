'''
Created on 2019. 5. 16.

@author: koys007
'''

#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
accessKey = "YOUR_ACCESS_KEY" #ETRI에서 발급 받은 Access Key를 입력하세요.
analysisCode = "ner"
 
text = "윤동주(尹東柱, 1917년 12월 30일 ~ 1945년 2월 16일)는 한국의 독립운동가, 시인, 작가이다." 
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))
                                    
