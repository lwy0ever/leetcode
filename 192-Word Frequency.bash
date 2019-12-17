# Read from the file words.txt and output the word frequency list to stdout.
# 抄的
# cat表示输出文件内容
# xargs将内容分隔,-n 1表示每行一个
# sort排序
# uniq -c去重并统计次数
# sort排序,-n按照数值,-r反序
cat words.txt | xargs -n 1 | sort | uniq -c | sort -nr | awk '{print $2" "$1}'