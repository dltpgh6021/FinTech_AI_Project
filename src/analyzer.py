import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from transformers import pipeline

def generate_wordcloud(csv_path, font_path='C:/Windows/Fonts/malgun.ttf'):
    '''
    뉴스 제목이 담긴 csv 파일 읽어옴
    워드 클라우드 생성 후 화면에 보여줌

    :param csv_path: 읽어올 CSV 파일 경로
    :param font_path: 한글 깨짐 방지를 위한 폰트 경로 (기본 : 윈도우 맑은 고딕)
    '''
    try: 
        df = pd.read_csv(csv_path)
        # 텍스트 하나로 뭉치기
        text = " ".join(title for title in df['Title'].astype(str))

        # 워드클라우드 생성
        wordcloud = WordCloud(
            font_path=font_path,
            width=800, 
            height=400,
            background_color='white', 
            colormap='Blues'
        ).generate(text)

        # 화면에 출력
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title("뉴스 핵심 키워드 워드클라우드", fontsize=15)
        plt.show()

    except FileNotFoundError:
        print(f"에러: {csv_path} 파일을 찾을 수 없습니다. ")
    except Exception as e:
        print(f"워드 클라우드 생성 중 에러 발생: {e}")

def analyze_sentiment(csv_path):
    '''
    뉴스 제목이 담긴 csv 파일을 읽어 AI(KR-FinBert)로 긍정/부정/중립을 분석한 뒤, 
    결과가 추가된 DataFrame 반환
    '''
    try: 
        df = pd.read_csv(csv_path)

        print("AI 모델 불러오는 중")
        analyzer = pipeline("text-classification", model="snunlp/KR-FinBert-SC")

        titles = df['Title'].tolist()
        ai_result = analyzer(titles)

        # 결과를 DataFrame에 추가
        df['감성_판단'] = [result['label'] for result in ai_result]
        df['AI_확신도'] = [round(result['score'] * 100, 2) for result in ai_result]

        return df
    except FileNotFoundError:
        print(f"에러: {csv_path} 파일을 찾을 수 없습니다. ")
        return pd.DataFrame()
    
if __name__ == "__main__":
    test_csv_path = 'data/samsung_news.csv'

    print("--- 1. 워드클라우드 테스트 시작 ---")
    generate_wordcloud(test_csv_path)

    print("\n--- 2. AI 감성 분석 테스트 시작 ---")
    result_df = analyze_sentiment(test_csv_path)

    if not result_df.empty:
        print(result_df.head())