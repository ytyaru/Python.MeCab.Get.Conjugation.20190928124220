#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import sys

def _csv_files():
    # 用言（動詞、形容詞、助動詞）
    return ('Verb.utf8.csv', 'Adj.utf8.csv', 'Auxil.utf8.csv')

def show_help():
    import os
    this_file_name = os.path.basename(__file__)
    doc = '''\
概要        : 入力した用言の活用形一覧を返す。
使い方      : 第一引数に用言の基本形を入力する。
コマンド書式: python3 {0} 用言 (デリミタ)"
コマンド例  : python3 {0} '動く'"
            : python3 {0} '動く' ','"
            : python3 {0} '動く' $'\\n'"
            : python3 {0} '動く' $'\\t'"
            : python3 {0} '楽しい'"
            : python3 {0} '如し'"
必要なもの  : 辞書ファイル {1}\
'''.format(this_file_name, _csv_files())
    print(doc)

# 入力した用言（基本形）における他の活用形名を出力する
def list_conjugation():
    if 2 > len(sys.argv):
        show_help()
        sys.exit()
    conjugations = _read_csv(sys.argv[1])
    if 0 == len(conjugations):
        print("ERROR: 用言「{}」は辞書にありませんでした。".format(sys.argv[1]), file=sys.stderr)
        sys.exit()
    show_list(conjugations)

# 入力した基本形に一致するレコードをCSVから取得する
def _read_csv(word):
    res = []
    filenames = _csv_files()
    for filename in filenames:
        if 0 < len(res): return res
        reader = csv.reader(open(filename, "r", encoding="utf-8"))
        for row in reader:
            if word == row[10] and row[9] not in res: 
                res.append(row[9])
    return res

def show_list(conjugations):
    delimiter = "\n"
    if 2 < len(sys.argv): delimiter = sys.argv[2]
    print(delimiter.join(conjugations))


if __name__ == '__main__':
    list_conjugation()

