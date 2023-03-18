numberss = [1,2,2,1,3,3,85,3,2,72,27,37,2,72,337,2,3]

def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        print(f'{name} + plays banjo', name[0])
    else:
        print(f'{name} does not play banjo')


def count_by(x, n):
    arr = []
    a = x
    for i in range(n):
        arr.append(x)
        x += a
    return arr


def switch_it_up(number):
    nums = {
        1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9:'Nine'
    }
    if number in nums:
        print(nums.get(number))

def quit_sort(arr):
    if len(arr) <= 1:
        return arr
    item = arr[0]
    left = list(filter(lambda x: x < item, arr))
    center = [x for x in arr if x == item]
    right = list(filter(lambda x: x > item, arr))
    return quit_sort(left) + center + quit_sort(right)


def hero(bullets, dragons):
    if bullets >= (dragons * 2):
        return True
    else:
        return False


def reverse_words(text):
    arr = []
    text = text.split(' ')
    for i in text:
        arr.append(list(reversed(i)))
    arr2 = []
    for j in arr:
        j = ','.join(j)
        arr2.append(j.replace(',', ''))
    return ' '.join(arr2)

nums = [6, 0, 1, 10, 10]

def sum_array(arr):
    if arr:
        arr = sorted(arr)
        del arr[0]
        del arr[-1]
        return (arr)
    else:
        return 0


def sum_two_min():
    arr = [1,2,3,4,5]
    min1 = arr.pop(min(arr))
    min2 = arr.pop(min(arr))
    print(min1 + min2)

sum_two_min()