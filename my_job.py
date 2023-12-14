import min_max    # 모듈명으로 호출하는 것이 더 나음
import sum

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
if __name__ == '__main__':
    print(min_max.find_min_max(data)) # 외부 함수 호출 시 '.' dot 이 꼭 들어가야 함
    print(sum.sum_range(1, 11))


# from min_max import find_min_max    # 함수 이름 호출 (모듈 x)
# from sum import sum_range

# data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
# if __name__ == '__main__':
#     print(find_min_max(data)) # 외부 함수 호출 시 '.' dot 이 꼭 들어가야 함
#     print(sum_range(1, 11))