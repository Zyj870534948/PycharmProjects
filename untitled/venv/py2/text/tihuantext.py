import json
# f = open("new.txt","w+")
# with open("filename3.txt") as file_object:
#     lines=file_object.readlines()
#     for line in lines:
#         a = line.replace("python","C")
#         f.write(a)
#         print(line)
#


a = '{"sys":[0.2,0.5],"hys":[1,-1]}'
print type(a),a
a = json.loads(a)
print type(a),a