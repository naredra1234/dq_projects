from collections import Counter
from read import load_data

if __name__ == "__main__":
    data = load_data()
    result = data["headline"].tolist()
    result_con = ''
    for i in result:
        result_con = result_con + str(i)
    result_con_list =  result_con.split(" ")
    result_con_list = [i.lower() for i in result_con_list]
    cnt = Counter()
    for word in result_con_list:
        cnt[word] += 1
        
    sorted(cnt.items(), key=lambda x: x[1])
    print (list(cnt)[0:100])
