# Stock Parsing

ver 0.0

## 필터링 정보
* 주당 순 자산 500억이상
* 시가총액 1000억 이상
* 상장 주식수 1000만개 이상

이 항목들은 건전한 기업 판단하기 위해서는 필수!


## Outline data
* 시가총액 
* PER (계산)
* ROE 증가율 관한 그래프도 있으면 좋을 것 같다는 생각이 듬. 1년 내에서도 증가하는 추세인지 감소하는 추세인지 그래프를 준다거나, 수치를 주면 훌륭함.
* 배당률 
* 주가 

### Outline view



ver 1.0

* 고정


## 일정 
* 데이터를 받아오기 -> DB 저장 
* 보여주는 간단 
* 

우리나라의 경우 미국에 비해 PER이 좀 더 낮아도 오르지 않는 경우가 많아서 5, 10, 15로 잡고, 좀 더 저평가된 주식 찾으면 좋음. 다만 5 이하인 경우 유의해서 살펴 볼 필요가 있음. 그리고 니가 지난번에 이야기했던 PER 한 분기만 계산하면 업황이 계절에 따라 바뀌는 경우도 많고, 표본이 너무 작다는 생각이 들어서 1년정도는 봐야 될 것 같음. 



PBR 1.5, 2.0미만(최근 4분기로 계산. 역시 마찬가지)
PER 1.5, 2.0정도까지 괜찮은 것 같아서 1.5, 2.0정도로 보면 좋을 것 같음.
Psr pbr 1.0이하로 설정하는게 좋을것같다.

PERxPBR 22보다 적음
사실상 저 조건에 맞으면 들어옴....

배당률 1, 2%초과
배당률 항목은 인철이는 많이 밀고, 워렌 버핏이나 여러 투자자들도 강조 하고, 내가 보낸 사진 보면 3%초과인 경우가 있는데, 이런 것들을 적용을 해 본 결과 우리나라에서 내 생각에 배당을 많이 안 주는 경향이 있음. 그래서 배당으로 판단하다보면 좋은 기업, 그리고 고성장 기업을 놓치는 경우가 많아서 내 투자기준에서 필수항목에 넣기는 좀 그런 것 같음.
선택 항목 1%, 2% 이상으로 해서 넣으면 괜찮을 것 같음.

업종 PER
업종 PER은 연별로 평균 추세를 그래프로 볼 수 있으면 좋을 것 같은데, 숫자로만 봐도 괜찮음.

금융, 보험업종 제외라는 항목은 경기를 타고, 부채비율이 높아서 그런 것 같음. 일단은 제외할 필요는 없을듯.

EPS나 ROE, ROA의 경우에는 나는 잘 보지 않음. 지금 재무재표 복습중인데 공부해보고 필요하다 생각이 들면 추가적으로 조건 넣겠음.


# 참고 사이트 
* http://media.kisline.com/highlight/mainHighlight.nice?nav=1&paper_stock=005930
* https://minjejeon.github.io/learningstock/2017/09/07/download-krx-ticker-symbols-at-once.html

# 용어
market_capitalization: '시가총액'
sales: '매출액(억원)'
operating_profit: '영업이익(억원)'
operating_margin: '영업이익율(%)'
net_income: '당기순이익(억원)'
net_profit_rate: '순이익율(%)'
assets: '자산총계(억원)'
liabilities: '부채총계(억원)'
capitals: '자본총계(억원)'
retention_rate: '유보율(%)'
return_on_equity: 'ROE' ( net_income/assets )
price_earning_ratio: 'PER' 
price_book-value_ratio: 'PBR'
: 'PSR', 13: 'EPS(원)', 14: 'BPS(원)', 15: 'SPS(원)', 16: 'EBITDA(억원)', 17: 'EV/EBITDA'}
