# -------------------------------------
# category :
# Q : 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
#     "()()" 또는 "(())()" 는 올바른 괄호입니다.
#     ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
#     '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고,
#     올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
#
# url : https://programmers.co.kr/learn/courses/30/lessons/12909
# 설명 : deque를 사용해야 효율성 테스트를 통과할 수 있다
# --------------------------------------
# space complexity : O(n)
# time complexity : O(n)
from collections import deque

def solution(s):
    s = deque(list(s))
    stack = deque([s.popleft()])

    while s:
        t = s.popleft()

        if t == "(":
            stack.append(t)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(t)

    return len(stack) == 0