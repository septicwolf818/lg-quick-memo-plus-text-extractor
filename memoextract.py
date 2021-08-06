#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import io
file_path = input('Enter file path: ')
with io.open(file_path, mode='rb') as file:
    for (index, line) in enumerate(file):
        try:
            line_string = str(line)
            if 'memoinfo.jlqm' in line_string:
                json_list = file.readlines()[:-1]
                json_object = json.loads('{'
                        + ''.join([str(line.decode('utf-8')) for line in
                        json_list]) + '}')
                for memo_object in json_object['MemoObjectList']:
                    if "DescRaw" in memo_object:
                        print(memo_object["DescRaw"])
                break
        except Exception as e:
            print(e)
