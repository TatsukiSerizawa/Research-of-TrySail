# Classification of TrySail

TrySailが好きすぎて気付いたら3人を分類するプログラムを作ってた。

あとナンスが可愛い。

## 手順

1. スクレイピングして画像を収集

    scraping.py

2. 顔領域を切り出し

    face_recog.py

3. 画像サイズを64✕64にリサイズ

    resize.py

4. データ拡張

    padded.py

5. CNNで顔画像を学習

    CNN.ipynb

6. テストデータを与えて認識結果を表示

    recog_trysail.ipynb

## 参考

全体的な参考: https://blog.aidemy.net/entry/2017/12/17/214715

Scraping: https://qiita.com/tsuro/items/fa7bb3015feca1212732