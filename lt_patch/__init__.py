import json
from VerdictFormat.VerdictFormat import Multilaws_to_Normalize as restore_law_from_context
import pkgutil
import argparse
import os
import rglob
import re

parser = argparse.ArgumentParser()
parser.add_argument("patch_dir")
parser.add_argument("-o","--out-dir",default="patched_data",dest="out_dir")
args = parser.parse_args()
assert os.path.isdir(args.patch_dir),'path is not dir'
ori_json_file_paths=rglob.rglob(args.patch_dir, "*.json")

def main():    
    # print(data)
    law_list = pkgutil.get_data(__name__, "assets/law_list.txt").decode('utf-8').split("\n")
    for json_path in ori_json_file_paths:
        with open(json_path,"r",encoding="utf-8",newline='') as f:
            data = json.loads(f.read())
        full_doc = data["full_doc"]
        # resotre data
        for ld in data["labeled_data"]:
            for i,ld_law in enumerate(ld['laws']):
                ld['laws'][i]['content'] = restore_law_from_context(full_doc,law_list,[ld_law])[0]
        # save restart data
        if(not os.path.isdir(args.out_dir)):
            os.mkdir(args.out_dir)
        ori_file_name = os.path.basename(json_path)
        with open(re.sub(r'\\$|\/$','',args.out_dir)+ '/' + ori_file_name,'w',encoding='utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False))

        