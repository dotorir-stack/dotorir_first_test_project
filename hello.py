import requests  # uv add로 설치한 도구를 불러옵니다.
import json

def main():
    print("인터넷에서 정보를 가져오는 중...")
    
    # 웹사이트에 요청을 보냅니다.
    response = requests.get("https://api.ipify.org?format=json")
    
    # 가져온 정보에서 IP 주소만 뽑아냅니다.
    data = response.json()
    
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("성공! 'result.json' 파일에 저장되었습니다.")
    print("힘들었다")

if __name__ == "__main__":
    main()