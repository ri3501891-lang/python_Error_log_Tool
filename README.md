# CSV Error Log Tool　　（生成AI利用）


## 概要

このツールは、CSV形式のログファイルから `status` 列が `ERROR` の行だけを抽出し、
`error.log` に書き出すためのスクリプトです。

- 入力: input.csv（id, status, message などの列を持つCSV）
- 出力: error.log（ERROR行のみを1行1レコードで出力）
- 実行すると、全体の行数とERROR行数をターミナルに表示します。

## 追加した機能

このバージョンでは、最初の ERROR 抽出機能に次の機能を追加した。

- WARNING 行も抽出して `warning.log` に保存する機能
- `date` 列を追加し、日付ごとにログを集計する機能
- 日付ごとの `error_count` と `warning_count` を `summary.csv` に出力する機能



## 学び・振り返り

- csv.DictReader を使って、ヘッダ付きCSVを1行ずつ辞書として扱う方法を学んだ
- ループの中で全行数をカウントしつつ、status が "ERROR" の行だけを別リストに集める処理を書けるようになった
- with open(..., "r"/"w") を使ったファイル入出力の基本的なパターンを復習できた
- CSVの入力 → 条件抽出 → ログファイルへの出力という、シンプルなETL処理の流れを体験できた



今回（2回目）の実装では、特に `csv.DictReader` と `csv.DictWriter` の使い方で最初つまずいた。

- `csv.DictReader` を使うと、CSVの1行を辞書として扱えることを学んだ
- `row["date"]` や `row["status"]` は、1行分の辞書から列名を指定して値を取り出していることを理解した
- `summary` のような辞書を使うことで、日付ごとの件数をまとめて管理できることを学んだ
- `summary.items()` を使うと、辞書のキーと値をセットで取り出せることを理解した
- `csv.DictWriter` を使うと、辞書の内容をCSVとして1行ずつ書き出せることを学んだ
- `writer.writeheader()` はCSVのヘッダ行を書き込む処理であることを理解した
- `writer.writerow(...)` は、辞書1件をCSVの1行として出力する処理だと分かった

