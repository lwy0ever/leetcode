# Read from the file file.txt and print its transposed content to stdout.
# 抄的
# NR - Number of Record - 当前处理的行是第几行（因为awk是流处理工具，一行一行处理的，所以NR在不停的自增1)
# FNR - File Number of Record - 当前处理的行是当前处理文件的第几行
# NF - Number of Fileds - 当前行有多少列数据（这个在每行都会根据设定的分割符重新计算，默认分割符是任意连续的多个空白符）
awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else{
            res[i]=res[i]" "$i
        }
    }
}END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}' file.txt