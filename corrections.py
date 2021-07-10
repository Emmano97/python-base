
with open("corrections.txt", encoding='utf-8') as corrections:
    content = str(corrections.read())
    print(type(content))
    corrections_list = content.split("@end")
    for text in corrections_list:
        filename = "corrections/"+text.split("!@")[0]
        file_content = text.split("!@")[1]
        f = open(filename, 'x')
        f.write(file_content)
        f.close()
corrections.close()