# 파일이름 : 사용자 입력 기반 날씨와 활동유형 맞춤 옷차림 추천 시스템
# 작 성 자 : 60251763김수빈

# 변수 선엄
version = 1.0
total_days = 0
program_name = 0
codi_score = 0
cold_sensitivity = 0.0

print(f'{program_name} V{version}')
print('날씨와 활동 유형에 맞는 옷차림을 추천해드리겠습니다.')

# 사용자 기본 정보 입력
user_name = input('이름을 입력하세요 : ')
user_age = int(input('나이를 입력하세요: ')
cold_sensitivity = float(input('추위 민감도를 입력하세요(1.0~5.0) : '))

# 입력 횟수 지정
day_count = int(input('몇 일치 날씨 데이터를 입력하시겠습니까? (최소 3일) : '))
if day_count < 3:
  day_count = 3
  print('최소 3일 이상의 날짜 데이터를 받습니다. 3일치 날짜 데이터로 설정합니다.')

# 리스트 초기화
temperatures = []
activities = []
rainfalls = []

print('< 날씨 및 활동 정보 입력 >')

# for문으로 데이터 입력, append
for i in range(day_count):
  print(f'[ {i+1}일차 ]')
  temp = float(input('기온(℃) : '))
  rainfall = int(input('강수량(mm) : '))
  activity = input('활동 유형 (실내 / 실외 / 운동) : ')
  
  temperatures.append(temp)
  rainfalls.append(rainfall)
  acivities.append(activity)

# 리스트 조작 4종 이상
temperatures.insert(0, 0.0)
temperatures.remove(0.0)
max_temp = max(temperatures)
min_temp = min(temperatures)
avg_temp = sum(temperatures)/len(temperatures)
temperatures.sort()

print(f'< {user_name}님 날씨 분석 결과 >')
print(f'나이: {user_age}세 | 추위 민감도: {cold_sensitivity}')
print(f'최고 기온: {max_temp}℃ | 최저 기온: {min_temp}℃ | 평균기온: [avg_temp: .1f}℃')

# 일별 옷차림 추천 + 코디 등급
print('< 일별 옷차림 및 코디 추천 >')

for i in rage(day_count):
  temp = temperatures[i]
  rain = rainfalls[i]
  act = activities[i]
  
  # 복합 대입 연산자
  total_days += 1
  codi_score += int(temp)
  
  # 연속 if-elif-else + 비교 연산자 - 기온 지수 판독기, 코디 부여
  if temp >= 28:
    outfit = '반팔 + 반바지'
    grade = '여름 코디'
  elif temp >= 20:
    outfit = '얇은 긴팔 + 면바지'
    grade = '봄/가을 코디'
  elif temp >=12:
    outfit = '맨투맨 + 청바지'
    grade = '신선한 날 코디'
  elif temp >= 0:
    outfit = '코트 + 히트텍'
    grade = '겨울 코디'
  else:
    outfit = '패딩 + 기모 내의'
    grade = '한겨울 코디'
    
  # 논리 연산자 and, or + 문자열 비교로 활동 유형 반영
   if rain > 10 and act == '실외':
     extra = '우산 필수 + 방수 재킷 추천'
   elif rain > 0 or act == '운동':
     extra = '모자 또는 가벼운 방풍 재킷 추천'
   else:
     extra = '기본 착장으로 충분해요'
     
     # 추위 민감도 반영 - 중첩 if문
     if cold_sensitivity >= 4.0:
       if temp < 20:
         outfit += '+ 얇은 조끼 추가'

  # 독립적인 if문 - 특별 코디 칭호 부여
    title = ''
    if temp >= 28 and act == '실외':
      title = '여름 완벽 코디 달성!'
  
    print(f' [{total_days}일차] 기온: {temp}℃ | 활동: {act}')
    print(f' 추천 옷차림: {outfit}')
    print(f' 코디: {grade}')
    print(f' 액세서리: {extra}')
    if tile:
      print(f' {title}')

# 최종 요약
print(f'< 최종 요약 >')
print(f'{user_name}님 ({user_age}세) | 추위 민감도: {cold_sensitivity}')
print(f'총 {total_days}일 분석 | 평균 기온: {ave_temp:.1f}℃')

# 독립적인 if문 - 전체 날씨 총평
if ave_temp >= 25:
  print('전반적으로 더운 날씨입니다. 수분 보충 잊지 마세요.')
if ave_temp < 10:
  print('전반적으로 추운 날씨입니다. 따뜻하게 입으세요.')

   

  
    
