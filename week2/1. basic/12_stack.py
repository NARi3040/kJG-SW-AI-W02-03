"""
[스택 - 괄호 짝 맞추기]

문제 설명:
- 스택(Stack)을 사용하여 괄호가 올바르게 짝지어져 있는지 확인합니다.
- LIFO (Last In First Out) 구조를 활용합니다.

입력:
- s: 괄호 문자열 (예: "(())", "(()")

출력:
- True: 올바른 괄호
- False: 잘못된 괄호

예제:
입력: "(())"
출력: True

입력: "(()"
출력: False

힌트:
- 여는 괄호 '('는 스택에 push
- 닫는 괄호 ')'를 만나면 스택에서 pop
- 마지막에 스택이 비어있으면 True
"""

def is_valid_parentheses(s):
    """
    괄호 짝이 맞는지 확인
    
    Args:
        s: 괄호 문자열
    
    Returns:
        올바른 괄호면 True, 아니면 False
    """
    stack = []
    
    # TODO: 문자열의 각 문자를 순회
    ## : 여는 괄호 '('면 스택에 추가
    ## : 닫는 괄호 ')'면
    ## 스택이 비어있으면 False 반환
    ## 아니면 스택에서 pop
    # 지적 3: n = len(s) 는 아래에서 쓰이지 않는 변수라 삭제
    for item in s:
        if (item == "("):
            # 지적 1: stack.append("s") -> stack.append(item)
            #   지금은 개수만 세면 되니 "s"를 넣어도 결과가 같지만,
            #   괄호가 {} [] 로 늘어나면 "무엇이 열렸는지"를 스택에 담아야 함
            stack.append(item)
        # 지적 2: 조건 순서 - "닫는 괄호일 때" 안에서 "스택이 비었는지"를 확인
        #   기존: elif not stack -> elif item == ")" (괄호만 들어와서 우연히 맞았음)
        elif (item == ")"):
            if (not stack):
                return False
            stack.pop()
    
    # TODO: 반복이 끝나면 스택이 비어있는지 확인
    if (stack):
        return False
    else:
        return True
    # 지적 3: 위 if/else 에서 항상 return 하므로 뒤의 pass 는 도달 불가 -> 삭제

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    test1 = "(())"
    result1 = is_valid_parentheses(test1)
    print(f"입력: {test1}")
    print(f"결과: {result1}")
    print()
    
    # 테스트 케이스 2
    test2 = "(()"
    result2 = is_valid_parentheses(test2)
    print(f"입력: {test2}")
    print(f"결과: {result2}")
    print()
    
    # 테스트 케이스 3
    test3 = "()(())"
    result3 = is_valid_parentheses(test3)
    print(f"입력: {test3}")
    print(f"결과: {result3}")
    print()
    
    # 테스트 케이스 4
    test4 = "())("
    result4 = is_valid_parentheses(test4)
    print(f"입력: {test4}")
    print(f"결과: {result4}")


