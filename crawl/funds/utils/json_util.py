import json

def format_json(jsonstr):
    try:
        # 格式化json数据，先load再dump
        return json.dumps(json.loads(jsonstr), indent=2, ensure_ascii=False)
    except Exception as e:
        print('格式化json出错：%s' % e)