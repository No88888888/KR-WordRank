def get_texts_scores(fname):
    # 튜토리얼에서 이용하는 `fname` 파일은 영화평과 평점이 \t 으로 구분된 two column tsv 파일입니다.
    # 예시는 이 cell 의 output 을 참고하세요.
    with open(fname, encoding='utf-8') as f:
        docs = [doc.lower().replace('\n','').split('\t') for doc in f]
        docs = [doc for doc in docs if len(doc) == 2]

        if not docs:
            return [], []

        texts, scores = zip(*docs)
        return list(texts), list(scores)

# La La Land
fname = '../data/134963.txt'
texts, scores = get_texts_scores(fname)

with open(fname, encoding="utf-8") as f:
    for _ in range(5):
        print(next(f).strip())