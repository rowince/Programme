# sort the ist of dict
from operator import itemgetter

students = [{"student_name": "s4", "student_id": 24}, {"student_name": "S1", "student_id": 13}, {
    "student_name": "S2", "student_id": 19}, {"student_name": "S3", "student_id": 10}]


def sortdict(arr):
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if arr[i]['student_id'] > arr[j]['student_id']:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)


sortdict(students)


# new = sorted(students, key=lambda i: i['student_id'])
# print(new)

# new = sorted(students, key=itemgetter('student_id'))
# print(new)

# dict1 = {1: 1, 2: 9, 3: 4}
# dict1 = {'1': '1', '2': '9', '3': '4'}
# new = sorted(dict1.items())
# print(new)
