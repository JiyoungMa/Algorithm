import sys

input = sys.stdin.readline

html_line = input().rstrip();

important_tags = ["main","div","p"]

answer = []

start = 0
end = 0
tag_start = 0
tag_end = 0
end_html = False
sentences = ""

now_i = 0

while now_i < len(html_line):
    if html_line[now_i] == "<":
        end = now_i
        end_html = False
        tag_start = now_i + 1
    
    elif html_line[now_i] == "/":
        tag_start = now_i+1
        end_html = True

    elif html_line[now_i] == ">":
        tag_end = now_i
        now_tag = html_line[tag_start:tag_end]
        if end_html == False:
            if "div" == now_tag.split(" ")[0]:
                start_index = now_tag.index("=")
                title = now_tag[start_index+2:-1]
                answer.append("title : "+ title)
            elif now_tag not in important_tags:
                sentences += html_line[start:end]

            start = now_i + 1
        else:
            if "p" == now_tag:
                sentences += html_line[start:end]
                str_list = sentences.rsplit(" ")
                result = ""

                for s in str_list:
                    if s != "":
                        result += s+" "

                result = result.rstrip()
                answer.append(result)
                sentences = ""
            elif now_tag not in important_tags:
                sentences += html_line[start:end]
            start = now_i + 1
    now_i += 1

print("\n".join(answer))
