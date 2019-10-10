# BeQX

Auto scripts for QuantumultX

脚本尚未稳定，功能/格式随时可能会发生变化。

## ToQX

脚本将会将远程资源中的结点添加到预设的策略组中。
而不必在每次修改后手动添加策略组

Example: [DEMO](https://github.com/0KABE/BeQX/blob/dev/demo.json)

```json
{
    "general": [
        "server_check_url=http://www.gstatic.com/generate_204",
        "network_check_url=http://baidu.com/",
        ";dns_exclusion_list=*.qq.com, qq.com",
        ";ssid_suspended_list=JO2EY",
        ";udp_whitelist=53, 123, 1900, 80-443",
        "excluded_routes= 192.168.0.0/16, 172.16.0.0/12, 100.64.0.0/10, 10.0.0.0/8",
        ";icmp_auto_reply=true"
    ],
    "dns": [
        "server=117.50.10.10",
        "server=119.29.29.29",
        "server=223.5.5.5",
        "server=114.114.114.114",
        "server=8.8.8.8"
    ],
    "policy": {
        "Hong Kong": {
            "type": "available",
            "policies": [],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Hong_Kong.png"
        },
        "Taiwan": {
            "type": "available",
            "policies": [],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Taiwan.png"
        },
        "Japan": {
            "type": "available",
            "policies": [],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Japan.png"
        },
        "Singapore": {
            "type": "available",
            "policies": [],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Singapore.png"
        },
        "America": {
            "type": "available",
            "policies": [],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/United_States.png"
        },
        "Others": {
            "type": "static",
            "policies": [
                "Policy",
                "Direct"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Final.png"
        },
        "Domestic": {
            "type": "static",
            "policies": [
                "Direct",
                "Policy",
                "Hong Kong"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Domestic.png"
        },
        "Apple": {
            "type": "static",
            "policies": [
                "Policy",
                "Direct"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Apple.png"
        },
        "Advertising": {
            "type": "static",
            "policies": [
                "Reject",
                "Direct",
                "Policy"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Advertising.png"
        },
        "Hijacking": {
            "type": "static",
            "policies": [
                "Reject",
                "Direct",
                "Policy"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Hijacking.png"
        },
        "Streaming": {
            "type": "static",
            "policies": [
                "Hong Kong",
                "Taiwan",
                "Japan",
                "Singapore",
                "America",
                "Direct"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/DomesticMedia.png"
        },
        "Bilibili&iQIYI": {
            "type": "static",
            "policies": [
                "Domestic",
                "Policy",
                "Hong Kong",
                "Taiwan"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/iQIYI&bilibili.png"
        },
        "Policy": {
            "type": "static",
            "policies": [
                "Hong Kong",
                "Taiwan",
                "Japan",
                "Singapore",
                "America",
                "Direct"
            ],
            "img-url": "https://raw.githubusercontent.com/zealson/Zure/master/IconSet/Proxy.png"
        }
    },
    "server_remote": [
        {
            "url": "https://example.com",
            "tag": "Hong_Kong",
            "type": "ssr",
            "policies": [
                "Hong Kong"
            ]
        },
        {
            "url": "https://example.com",
            "tag": "Taiwan",
            "type": "ssr",
            "policies": [
                "Taiwan"
            ]
        },
        {
            "url": "https://example.com",
            "tag": "Japan",
            "type": "ssr",
            "policies": [
                "Japan"
            ]
        },
        {
            "url": "https://example.com",
            "tag": "Singapore",
            "type": "ssr",
            "policies": [
                "Singapore"
            ]
        },
        {
            "url": "https://example.com",
            "tag": "America",
            "type": "ssr",
            "policies": [
                "America"
            ]
        }
    ],
    "filter_remote": [
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/Unbreak.list",
            "tag": "Unbreak",
            "enable": "true",
            "force-policy": "Direct"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/Advertising.list",
            "tag": "Advertising",
            "enable": "true",
            "force-policy": "Advertising"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/Hijacking.list",
            "tag": "Hijacking",
            "enabled": "true",
            "force-policy": "Hijacking"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/ForeignMedia.list",
            "tag": "ForeignMedia",
            "enabled": "true",
            "force-policy": "Streaming"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/DomesticMedia.list",
            "tag": "DomesticMedia",
            "enabled": "true",
            "force-policy": "Bilibili&iQIYI"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/Global.list",
            "tag": "Policy",
            "enabled": "true",
            "force-policy": "Policy"
        },
        {
            "url": "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Filter/China.list",
            "tag": "Domestic",
            "enabled": "true",
            "force-policy": "Domestic"
        }
    ],
    "rewrite_remote": [
        "https://raw.githubusercontent.com/ConnersHua/Profiles/master/Quantumult/X/Rewrite.conf, tag=Rewrite, enabled=true",
        "https://raw.githubusercontent.com/JO2EY/Rules/master/Quantumult/X/Script.conf, tag=Script, enabled=true"
    ],
    "server_local": [],
    "filter_local": [
        "geoip, cn, Domestic",
        "final, Others"
    ],
    "rewrite_local": [],
    "mitm": [
        "passphrase = 4B676386",
        "p12 = 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",
        ";skip_validating_cert = false",
        ";force_sni_domain_name = false",
        ";hostname = *.example.com, *.sample.com"
    ]
}
```

URL: <https://API.OKAB3.COM/json2qx>

| 参数     | 必须 | 描述         | 缺省值  |
| :------- | :--- | :----------- | :-----: |
| url      | 是   | 源文件地址   |         |
| filename | 否   | 返回的文件名 | qx.conf |

## ToClash

支持将上述json配置文件转换为ClashR配置文件

URL: <https://API.OKAB3.COM/json2clashr>

| 参数     | 必须 | 描述         | 缺省值  |
| :------- | :--- | :----------- | :-----: |
| url      | 是   | 源文件地址   |         |
| filename | 否   | 返回的文件名 | qx.yml |

## 维护

使用中遇到了BUG？欢迎在[Issues](https://github.com/0KABE/BeQX/issues)中提交问题或留言，群里的反馈的BUG我可能会忘记。

如果有大佬愿意[提交](https://github.com/0KABE/BeQX/pulls)代码或更新README文档也十分欢迎一起维护。

## 打赏

```
#吱口令#长按复制此条消息，打开支付宝给我转账ijL3kr36HM
```

### Telegram

[TG群组](https://t.me/OKAB3Script)

[TG频道](https://t.me/OKAB3_Script_Channel)
