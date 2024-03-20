# mineMap크기 받기
print("Game Setting")
width,length = map(int,input("Enter Width,Length : ").split())

print("Enter mine map (0: no mine, 1: mine)")
col = 4
row = 4;
# 공행렬 만들기(결과가 되는 행렬) / arr이 직관적이지 않아 이름 바꿨습니다.
mine_map = []   #arr = [[0 for y in range(col)] for x in range(row)]
arr = [[0 for y in range(col)] for x in range(row)]
'''
for y in range(length) : # length 세로길이 만큼 반복
        mine = input(":")    # 각 행의 지뢰를 0 또는 1로 입력 받으기 ex)'0' '1' '1' '0' 입력
        mine_map.append(list(map(int,mine.split())))  #append는 공행렬에 값을 추가해줌 ex) [ ] -> [ 0 1 1 0 ]
#10-12 3줄을 요약하면 15번 된다함.... 리스트컴프리헨션 공부 [표현식 for 요소 in 시퀀스 if 조건]
'''
#각 행의 지뢰를 0 또는 1로 입력 하면 mine_map 공행렬에 추가 ex)'0' '1' '1' '0' 입력 - [ 0 1 1 0 ]
mine_map = [list(map(int, input(":").split())) for y in range(length)]


# 앞에 받은 mine_map리스트 중 요소 1을 *로 대체함
for i in range(len(mine_map)):
    for j in range(len(mine_map[i])):
        if mine_map[i][j] == 1:
            mine_map[i][j] = '*'
'''
이해 (질문)
1. len은 리스트 내 요소의 개수를 카운팅하는 함수
2. mine_map에 포함된 요소의 개수만큼 반복하는 루프를 생성
3. mine_map[i]은 mine_map 리스트에서 i번째 행을 나타냄 즉 i가 계산된 리스트로 적용된다는거
'''

# 각 요소의 주변 8방향의 지뢰 개수 카운트하고 mine_map에 구현
for i in range(length):
    for j in range(width):
        # 각 요소가 지뢰인 경우 스킵
        if mine_map[i][j] == '*':
            continue

        # 각 요소 주변의 8방향을 검사하여 지뢰 개수 세기
        mine_count = 0 #지뢰 개수 초기화
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = i + dx, j + dy
                # 주변 위치가 지도 안에 있고, 그곳에 지뢰가 있으면 지뢰 개수 증가
                if 0 <= nx < length and 0 <= ny < width and mine_map[nx][ny] == '*':
                    mine_count += 1
        # 현재 위치에 지뢰 개수를 기록
        mine_map[i][j] = mine_count

# 결과 확인, mine_map 출력
for row in mine_map :
   print(' '.join(str(cell) for cell in row))

print(mine_map) #이건 뭐 어떻게 나오는거죠 ㅠ

    #print(arr.count(1))    #나중에 지뢰 몇개인지 설정하는거 만들고싶어서 1개수 카운트