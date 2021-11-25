char = {
    'name' : 'tuly',
    'test' : 'python'
}
# print(char)
# print(char['name'])
# print(char['what'])#will throw error
# print(char.get('doesnotexist'))#will return none
print(char.get('doesnotexist','customizedMessage : Not Found'))
