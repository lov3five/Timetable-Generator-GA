import itertools
import random


def generate_random_combinations(lst, n):
    """
    Hàm tạo ra tất cả các tổ hợp không trùng nhau có n phần tử từ danh sách lst.
    """
    combinations = set()
    for i in range(20):  # Thực hiện 1000 lần để tạo ra nhiều tổ hợp hơn
        selected_items = random.sample(lst, n)
        selected_items.sort()
        combinations.add(tuple(selected_items))
        if len(combinations) == len(list(itertools.combinations(lst, n))):
            break  # Khi đã tạo ra tất cả các tổ hợp có thể, thì dừng lại.
    return combinations

# Sử dụng hàm để tạo ra 7 phần tử ngẫu nhiên từ danh sách 30 phần tử:
lst = list(range(30))
selected_items = random.sample(lst, 7)
print(selected_items)

# Tạo ra tất cả các tổ hợp không trùng nhau có 7 phần tử từ danh sách 30 phần tử:
combinations = generate_random_combinations(lst, 7)
print(combinations)
