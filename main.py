# 파일이름 : 사용자 입력 기반 날씨와 활동유형 맞춤 옷차림 추천 시스템
# 작 성 자 : 60251763김수빈

# 전역변수 선언
version = 2.0
program_name = '날씨 맞춤 옷차림 추천 시스템'

temperatures = []
activities = []
rainfalls = []

# 사용자 정보 전역변수
user_name = ''
suer_age = 0
cold_sensitivity = 0.0
total_days = 0

# 함수 정의
#[함수1] 메인 메뉴 출력 함수
def print_menu():
    print()
    print(f'======{program_name}V{version}======')
    print('1. 날씨 데이터 입력')
    print('2. 날씨 데이터 조회')
    print('3. 통계 분석')
    print('4. 옷차림 추천')
    print('5. 종료')
    print('========================')
# [함수2] 사용자 기본 정보 입력 함수
def input_user_info():
    global user_name, user_age, cold_sensitivity
    print('\n[사용자 기본 정보 입력]')
    user_name = input('이름을 입력하세요 : ')
    user_age = int(input('나이를 입력하세요: ')
    cold_sensitivity = float(input('추위 민감도를 입력하세요(1.0~5.0) : '))
    print(f'\n{user_name}님, 반갑습니다!')
# [함수3] 날씨 데이터 입력 함수
def input_weather_data():
    global total_days, temperatures, activities, rainfalls
    if user_name =='':
      print('\n먼저 사용자 정보를 입력해주세요. (메뉴 1번 선택)')
      return
    day_count = int(input('몇 일치 날씨 데이터를 입력하시겠습니까? (최소 3일) : ')

    if day_count <3:
      day_count = 3
      print('최소 3일 이상의 데이터를 입력해야 합니다. 3일로 설정합니다.')
    print('\n< 날씨 및 활동 정보 입력 >')

    for i in range(day_count):
      print(f'\n[ {total_days + i + 1}일 차 ]')
      temp = float(input('기온(℃) : '))
      rainfall = int(input('강수량(mm) :'))
      activity = input('활동 유형 (실내/실외/운동) : ')

      temperatures.append(temp)
      rainfalls.append(rainfall)
      activities.append(activity)

    total_days += day_count
    print(f'\n총 {total_days}일치 데이터가 저장되었습니다.')

# [함수4] 날씨 데이터 조회 함수
def show_weather_data():
    if total_days == 0:
      print('\n저장된 날씨 데이터가 없습니다. 먼저 데이터를 입력해주세요.')
      print(f'\n<{user_name}님의 날씨 데이터 조회>')
      print(f'{'일차':<6} {'기온(℃)':<10} {'강수량(mm)':<12} {'활동 유형'}')
      print('-'*40)

      # for문으로 저장된 데이터 순서대로 출력
      for i in range(total_days):
        print(f'{i+1}일차 {temperatures[i]:<10} {rainfalls[i]:<12} {activities[i]}')

# [함수5] 통계 분석 함수
def analyze_statistics():
    if tatal_days == 0:
      print('\n저장된 데이터가 없습니다. 먼저 데이터를 입력해주세요.')
      return

    max_temp = max(temperatures)
    min_temp = min(temperatures)
    avg_temp = sum(temperatures)/len(temperatures)

    print(f'\n< {user_name}님의 날씨 통계 분석 결과 >')
    print(f'분석 일수 : {total_days}일')
    print(f'최고 기온 : {max_temp}℃')
    print(f'최저 기온 : {min_temp}℃')
    print(f'평균 기온 : {avg_temp:.1f}℃')

    if avg_temp >= 25:
        print('\n전반적으로 더운 날씨입니다. 수분 보충 잊지 마세요.')
    if avg_temp <10:
        print('\n전반적으로 추운 날씨입니다. 따뜻하게 입으세요.)
    return avg_temp

# [함수6] 옷차림 추천 함수 
def recommend_outfit(cold_sens):
    if total_days == 0:
      print('\n저장된 데이터가 없습니다. 먼저 데이터를 입력해주세요.')
      return

    print(f'\n< {user_name}님의 일별 옷차림 추천 >')
    print(f'추위 민감도: {cold_sens}')

    for i in range(total_days):
        temp = temperatures[i]
        rain = rainfalls[i]
        act = activities[i]

    # if-elif-else + 비교 연산자 - 기온에 따른 옷차림 판정
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

      # 논리 연산자 and, or + 문자열 비교 - 강수량/활동 유형 반영
        if rain > 10 and act == '실외':
         extra = '우산 필수 + 방수 재킷 추천'
        elif rain > 0 or act == '운동':
         extra = '모자 또는 가벼운 방풍 재킷 추천'
        else:
         extra = '기본 착장으로 충분해요'

      # 중첩 if문 - 추위 민감도 높으면 추가 옷차림 반영
      if cold_sens >= 4.0:
          if temp < 20:
            outfit += '+얇은 조끼 추가'

      # 독립적인 if문 - 특별 코디 칭호 부여
      title = ''
      if temp >= 28 and act == '실외':
         title = '여름 완벽 코디 달성!'

      print(f'\n[{i+1}일차] 기온 : {temp}℃ | 활동: {act}')
      print(f'추천 옷차림 : {outfit}')
      print(f'코디 : {grade}')
      print(f'액세서리 : {extra}')
      if title:
        print(f'{title}')

# 메인 로직
print(f'{program_name}V{version}')
print('날씨와 활동 유형에 맞는 옷차림을 추천해드리겠습니다.')
input_user_info()

while True:









   

  
    
