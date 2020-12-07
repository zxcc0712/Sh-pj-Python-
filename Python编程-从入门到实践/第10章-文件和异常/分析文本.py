def count_words(filename):
    """计算一个文件中大致含有多少单词"""
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        msg = '对不起，这本'+filename+'没有找到'
        print(msg)
    else:
        #计算文件包含的单词数,split方法以空格做分割条件
        words = contents.split()
        num_words = len(words)
        print(num_words)

filename = 'pi_digi.txt'
count_words(filename)