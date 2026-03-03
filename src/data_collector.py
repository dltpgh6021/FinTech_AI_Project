# src/data_collector.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_naver_news(keyword, max_items=10):
    '''
    네이버 통합검색 뉴스 탭에서 특정 키워드의 최신 뉴스 제목을 크롤링하여 
    판다스 DataFrame으로 반환하는 함수

    :param keyword: 검색할 검색어
    :param max_items: 가져올 뉴스 기사의 최대 개수
    :return: 뉴스 제목이 담긴 DataFrame
    '''
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # 접속 불량 시 에러
        soup = BeautifulSoup(response.text, 'html.parser')

        # F12로 찾아낸 이름표
        titles = soup.select('span.sds-comps-text-type-headline1')

        news_list = []
        for title in titles[:max_items]:
            clean_title = title.get_text().strip()
            if clean_title:
                news_list.append(clean_title)

        # 리스트를 DataFrame으로 변환
        df_news = pd.DataFrame(news_list, columns=['Title'])
        return df_news
    
    except Exception as e:
        print(f"크롤링 중 에러발생: {e}")
        return pd.DataFrame()
    
# 다른 파일에서 import data_collector를 할때는 조용히 함수만 빌려줌
# 파일 자체를 실행시킬 때는 테스트용 코드가 작동하게 하는 중요한 구조. 
# C언어의 main 함수 역할
if __name__ == "__main__":
    print("--- data_collector.py 모듈 테스트 시작 ---")
    df_samsung = get_naver_news('삼성전자', 5)
    print(df_samsung)

    # 현대차 뉴스도 잘 나오는지 테스트 가능