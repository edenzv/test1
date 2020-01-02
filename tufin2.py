# nested_list = []
#
# try:
#     file = open("testfile.txt","r")
#
#     line = file.readline()
#     while line:
#         print(line.strip())
#         nested_list.append(line.strip().split(' '))
#         line = file.readline()
#
# finally:
#     file.close()
#
# print(nested_list)

# filepath = 'testfile.txt'
# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        print("Line {}: {}".format(cnt, line.strip()))
#        line = fp.readline()
#        cnt += 1


alkaline_metals = []
for line in open('testfile.txt'):
    alkaline_metals.append(line.strip().split(' '))
print(alkaline_metals)