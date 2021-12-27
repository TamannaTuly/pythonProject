char = {
    'name' : 'tuly',
    'test' : 'python',
    'id' : {10,22}
}
# print(char)
# print(char['name'])
# print(char['what'])#will throw error
# print(char.get('doesnotexist'))#will return none
print(char.get('doesnotexist','customizedMessage : Not Found'))
print(char.get('firstName','Not Found'))
print('test')

char['firstName']='tamanna'
print(char.get('firstName'))
print(char)