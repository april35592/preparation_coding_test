# https://school.programmers.co.kr/learn/courses/30/lessons/169198

def solution(m, n, startX, startY, balls):
    answer = []
    # (0, 0), (m, 0), (0, n), (m, n) 4점 직사각형 당구대
    # 1번 경로 (ballX - startX) ** 2 + (ballY + startY) ** 2 아래변 부딧침
    # 2번 경로 (ballX + startX) ** 2 + (ballY - startY) ** 2 좌측변 부딧침
    # 3번 경로 (ballX - startX) ** 2 + (2n - ballY - startY) ** 2 위측변 부딧침
    # 4번 경로 (2m - ballX - startX) ** 2 + (ballY - startY) ** 2 우측변 부딧침
    for (ballX, ballY) in balls :
        distance = []
        if ballX != startX :
            distance.append((ballX - startX) ** 2 + (2 * n - ballY - startY) ** 2) #위측변 부딧침
            distance.append((ballX - startX) ** 2 + (ballY + startY) ** 2) #아래변 부딧침
        elif ballY < startY :
            distance.append((ballX - startX) ** 2 + (2 * n - ballY - startY) ** 2) #위측변 부딧침
        else :
            distance.append((ballX - startX) ** 2 + (ballY + startY) ** 2) #아래변 부딧침
        if ballY != startY :
            distance.append((2 * m - ballX - startX) ** 2 + (ballY - startY) ** 2) #우측변 부딧침
            distance.append((ballX + startX) ** 2 + (ballY - startY) ** 2) #좌측변 부딧침
        elif ballX < startX :
            distance.append((2 * m - ballX - startX) ** 2 + (ballY - startY) ** 2) #우측변 부딧침
        else :
            distance.append((ballX + startX) ** 2 + (ballY - startY) ** 2) #좌측변 부딧침
        distanceMin = distance[0]
        for di in distance :
            if distanceMin > di :
                distanceMin = di
        answer.append(distanceMin)
    return answer