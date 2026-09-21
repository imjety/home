def is_valid_jumin(jumin_raw):
    """주민등록번호 문자열(예: '900101-1234567')의 유효성을 검사한다."""
    jumin = jumin_raw.split('-')
    jumin = jumin[0] + jumin[1]

    j = 2
    tot = 0
    # j = 2~9까지 증가, 10이되면 다시 2로 초기화
    # tot = 각각의 숫자를 곱한 값의 총 합을 저장 할 변수
    for i in range(0, len(jumin) - 1):
        tot += int(jumin[i]) * j
        j += 1
        if j == 10:
            j = 2

    tot = 11 - (tot % 11)

    return int(jumin[-1]) == tot


if __name__ == "__main__":
    jumin = input("주민등록번호 : ")  # 주민등록번호 입력
    if is_valid_jumin(jumin):
        print("유효")
    else:
        print("유효하지 않음")
