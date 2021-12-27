char = {
    'name' : 'tuly',
    'test' : 'python',
    'id' : {10,22}
}
# print(char)
# print(char['name'])
# print(char['what'])#will throw error
# print(char.get('doesnotexist'))#will return none
# print(char.get('doesnotexist','customizedMessage : Not Found'))
# print(char.get('firstName','Not Found'))
# print('test')

# char['firstName']='tamanna'
# print(char.get('firstName'))
# print(char)

char.update({
    'name' : 'modon',# if we use same parameter then it will be replaced like currently the name will be modon and if there are new entries they will be joined and print everything
    'lastName' : 'tulytest',
    'testUpdate' : 'pythonProject',
    'idUpdated' : {10,22,1402037}
})
char['firstName']='tamanna'
print(char.get('firstName'))
print(char)
name = char.pop('name')#will delete name but save the name value in variable name
# del char['name']#delete name
print(char)
print(name)
