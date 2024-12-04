def add_durations(x: list, y: list):
    tmp = [0, 0, 0]
    tmp[0] = x[0] + y[0]
    tmp[1] = x[1] + y[1]
    tmp[2] = x[2] + y[2]

    return tmp

def calculate_amount(duration: list) -> int:
    min_in_sec = duration[2] // 60
    duration[2] = duration[2] % 60
    
    duration[1] += min_in_sec
    hour_in_min = duration[1] // 60
    duration[1] = duration[1] % 60
    
    duration[0] += hour_in_min
    
    if duration[1] >= 5 and duration[2] == 0:
        return duration[1] * 150
    
    if duration[1] >= 5:
        return (duration[1] + 1) * 150
    
    return (duration[1] * 60 + duration[2]) * 3
    

def create_mobile_book(log: list):
    number_mapping = {}
    bill_amount = 0
    max_bill_amount = 0
    
    for duration in log:
        if duration[1] in number_mapping:
            number_mapping[duration[1]] = add_durations(duration[0], number_mapping[duration[1]])
        else:
            number_mapping[duration[1]] = duration[0]
    
    for number in number_mapping:
        number_bill = calculate_amount(number_mapping[number])
        max_bill_amount = max(max_bill_amount, number_bill)
        bill_amount += number_bill
    
    return bill_amount - max_bill_amount

log = []

while True:
    try:
        l = input().split(",")
        l[0] = list(map(int, l[0].split(":")))
        log.append(l)
    except:
        break

print(create_mobile_book(log))
