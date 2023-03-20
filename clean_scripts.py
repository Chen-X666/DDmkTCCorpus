from tqdm import tqdm


def read_corpus(path):
    f = open(path, encoding="utf-8")
    sentences = f.readlines()
    sentences = [sentence.strip("\n") for sentence in tqdm(sentences)]
    return sentences


def del_repeat(document_list):
    print("去重前数据量：{}".format(len(document_list)))
    unique_corpus = list(set(document_list))
    print("去重后数据量：{}".format(len(unique_corpus)))
    return unique_corpus


corpus_path = "guichuBullet-screenText.txt"
doc_list = read_corpus(corpus_path)
print(doc_list[:10])
doc_list = del_repeat(doc_list)
print(doc_list[:10])
sorted_docs = sorted(doc_list, key=lambda x: len(x), reverse=True)

with open("sorted_danmaku.txt", "w", encoding="utf-8") as f:
    for line in tqdm(sorted_docs):
        f.write(line)
        print(line)
        f.write("\n")

print("完成！ 数据存储于：{}".format("sorted_danmaku.txt"))
