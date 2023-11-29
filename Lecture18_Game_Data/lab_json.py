import json

number = [1,2,3,4]
# number 리스트를 문자열로 덤프, json 이용
number_string = json.dumps(number)
print(type(number_string))
print(number_string)

value_string = '{"x":10, "y":20, "size":4.5}'
value = json.loads(value_string)
print(type(value))
print(value)