#from scraping import get_url, get_entry_list, scraping
from scraping import get_entry_list,  get_text

name_list = {"Asakura_Momo": "asakuramomoblog", "Amamiya_Sora": "amamiyasorablog",
             "Natukawa_Shiina": "natsukawashiinablog"}
blog_id = name_list["Natukawa_Shiina"]
url = "http://ameblo.jp/{0}/entrylist.html".format(blog_id)
BASE_DIRE = "../../data/{0}/".format("Natukawa_Shiina")
txt_path = "../../data/blog/Natukawa_Shiina/text.txt"

# get all entry list
all_entry_list = get_entry_list(url)

# get sentence from blog
sentence = get_text(all_entry_list)
sentence = str(sentence)
print(sentence)

# write sentence
with open(txt_path, mode='w') as f:
    f.writelines(sentence)