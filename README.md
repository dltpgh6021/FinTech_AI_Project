# 한국 주식 시게열 분석 및 AI 예측 파이프라인 (FinTech AI Project)

 > 금융 데이터 파이프라인 구축부터, AI 주가 예측, 자동화 대시보드까지 전 과정을 직접 구현하는 프로젝트

## 프로젝트 목표
 - 증권 데이터를 자동으로 수집 & 정제하는 **데이터 파이프라인** 구축
 - 슬라이딩 윈도우 및 통계적 기법을 활용한 **시계열 데이터 탐색 및 시각화**
 - 딥러닝/LLM 기반의 **주가 추세 예측 및 경제 뉴스 감성 분석** 모델링
 - 분석 결과를 제공하는 **웹 서비스 및 자동화 알림 봇** 개발

## 기술 스택 (Tech Stack)
 - **Language** : Python
 - **Data Analysis & Visualization** : Pandas, Matplotlib, FinanceDataReader
 - **Envrionment** : VS Code, Jupyter Notebook, Virtual Envrionment (venv)
 - *(추가 예정: Node.js, React, Scikit-learn, Tensorflow/PyTorch)*

## 프로젝트 구조 (Dictionary Structure)
```text
FinTech_AI_Project
├──data/                # 수집된 주가 및 금융 데이터 (.csv)
├──notebooks/           # 데이터 탐색(EDA), 시각화 및 모델 실험용 주피터 노트북
├──src/                 # 실제 서비스 구동을 위한 모듈화된 파이썬 스크립트 (.py)
├──requirements.txt     # 프로젝트에 필요한 파이썬 라이브러리 목록
└──README.md
```

## 진행상황 및 로드맵

Phase 1. 데이터 파이프라인 구축

- [x] FinanceDataReader를 활용한 국내 대형주(삼성전자, 현대차)주가 데이터 수집
- [x] 수집된 데이터의 로컬 DB(.csv) 저장 및 관리
- [X] 웹 크롤링을 통한 경제 뉴스 텍스트 데이터 수집

Phase 2. 데이터 탐색 및 통계 분석 (EDA)

- [x] 주피터 환경에서 Pandas를 활용한 시계열 데이터 결측치 확인 및 전처리
- [x] Matplotlib을 활용한 주가 추세선 시각화
- [x] rolling 함수를 이용한 이동평균선(20일, 60일) 도출
- [x] 스케일이 다른 다수 종목의 누적 수익률 정규화 및 비교 분석

Phase 3. AI 모델링(AI Modeling) - 진행 예정

- [ ] 딥러닝(CNN/LSTM 등)을 활용한 주가 패턴 인식 및 예측 모델 설계
- [X] LLM을 활용한 금융 뉴스 긍정/부정(호재/악재) 김성 분석

Phase 4. 자동화 서비스 구축 (Service Architecture) - 진행 예정

- [ ] Node.js 기반 백엔드 API 서버 구축
- [ ] React를 활용한 분석 결과 대시보드 UI 개발
- [ ] 메신저 봇을 통한 일일 종목 분석 자동 알림 시스템 연동

## 학습 노트 (TIL)
- [Day 1: Pandas 기초 (iloc, rolling) 및 시각화](docs/01_pandas_개념정리.md)
- [Day 2: 네이버 경제 뉴스 크롤링 및 리팩토링](docs/02_뉴스_크롤링_및_리팩토링.md)
- [Day 3: 워드클라우드와 감성분석](docs/03_워드클라우드와_감성분석.md)