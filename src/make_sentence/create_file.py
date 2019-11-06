from scraping import get_url, get_entry_list, scraping

name_list = {"Asakura_Momo": "asakuramomoblog", "Amamiya_Sora": "amamiyasorablog",
             "Natukawa_Shiina": "natsukawashiinablog"}
blog_id = name_list["Natukawa_Shiina"]
url = "http://ameblo.jp/{0}/entrylist.html".format(blog_id)
BASE_DIRE = "../../data/{0}/".format("Natukawa_Shiina")
all_entry_list = get_entry_list(url)
print(all_entry_list)
page_list = get_url(all_entry_list)
print(page_list)
scraping(page_list, BASE_DIRE)