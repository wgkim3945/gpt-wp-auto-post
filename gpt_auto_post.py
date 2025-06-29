
import requests
from datetime import datetime
import os

# 환경 변수에서 불러오기
WP_USER = os.getenv("WP_USER")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")
WP_API_URL = "https://smartinfonow.com/wp-json/wp/v2/posts"

# 예시용 자동 생성 글 (실제 사용 시 GPT API 연동 필요)
today = datetime.now().strftime("%Y년 %m월 %d일")
title = f"{today} 최신 복지정책 요약"
content = f"""
✅ {today} 기준 최신 민생 정책 소식입니다.

1. 기초생활수급자 생계급여 인상 검토
2. 청년월세지원금 3차 접수 시작
3. 노인 돌봄바우처 신청기간 연장 안내

자세한 정보는 복지로 또는 정부24를 확인하세요.
"""

# API 요청
response = requests.post(
    WP_API_URL,
    auth=(WP_USER, WP_APP_PASSWORD),
    json={
        "title": title,
        "content": content,
        "status": "publish"
    }
)

# 결과 확인
if response.status_code == 201:
    print("✅ 글 발행 성공:", title)
else:
    print("❌ 글 발행 실패:", response.status_code, response.text)
