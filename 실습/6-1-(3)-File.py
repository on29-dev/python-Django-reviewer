import pprint

store = [
    {
        "title": "1st", 
        "coke": "500",
        "soda": "400"
    },
    {
        "title": "auction",
        "coke": "600",
        "soda": "300"
    },
    {
        "title": "gmarket",
        "coke": "450",
        "soda": "550"
    }
]

def to_csv(value):
    # 키값
    keys = []
    for el in value[0]():
        keys.append(el)
    # keys  = ["title", "coke", "soda"]
    # 밸류값
    results = []
    for d in value:
        result = []
        for el in d.values():
            result.append(el)
        results.append(result)
    # 조합
    content = ', '.join(key) + '\n'
    for result in results:
        content += ', '.join(result) + '\n'
    f = open('./csv_file.txt', 'w')
    f.write(content)
    f.close()

to_csv(store)