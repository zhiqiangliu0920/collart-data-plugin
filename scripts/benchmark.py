"""Compare fixed CLI search/read flows. Characters and wall time are not model token usage."""
import argparse,json,statistics,subprocess,sys,time
from pathlib import Path

CASES=[
 ('Android 收入','collart_android','android.revenue','android-revenue-trend'),
 ('免费看广告按钮点击率','collart_android','android.ads','android-reward-ad-click'),
 ('Web 画像登录号','collart_web','web.identity','collart_web-identity'),
 ('Fashion 收入与 Web 交集','collart_fashion','fashion.revenue','collart_fashion-revenue-boundary'),
 ('ASA 关键词归因','collart_ios','ios.asa','collart-ios-asa-history-boundary'),
 ('成熟留存','collart_android','shared.activity','shared-core-metrics'),
 ('ADS无法使用回退原始埋点',None,'shared.routing','shared-table-routing'),
 ('没有连接只读权限',None,'shared.access','shared-data-access-policy'),
 ('Web 用户价值分层','collart_web','web.value','collart-web-user-value-tiers'),
]

def run(root,args):
    t=time.perf_counter();p=subprocess.run([sys.executable,'-B','-X','utf8',str(root/'scripts/kb.py'),*args],capture_output=True,text=True,encoding='utf-8',timeout=45)
    if p.returncode:raise RuntimeError(p.stdout[:500]+p.stderr[:500])
    json.loads(p.stdout)
    return len(p.stdout), (time.perf_counter()-t)*1000

def benchmark(old,new,repeats=3):
    rows=[]
    for question,project,new_id,old_id in CASES:
        search=['search',question]+(['--project',project] if project else [])
        row={'question':question,'project':project}
        for label,root,id in [('before',old,old_id),('after',new,new_id)]:
            sizes=[];times=[]
            for _ in range(repeats):
                a,b=run(root,search);c,d=run(root,['read',id]);sizes.append(a+c);times.append(b+d)
            row[label]={'commands':2,'read_commands':1,'output_characters':int(statistics.median(sizes)),'elapsed_ms_median':round(statistics.median(times),2)}
        rows.append(row)
    before=sum(r['before']['output_characters'] for r in rows);after=sum(r['after']['output_characters'] for r in rows)
    return {'method':'Same 9 questions, default CLI search then known topic read; sequential subprocesses; no model or database invocation. Not an end-to-end model-agent benchmark.','repeats':repeats,'actual_token_usage':None,'rows':rows,'totals':{'before_characters':before,'after_characters':after,'character_reduction_percent':round((1-after/before)*100,2),'before_ms':round(sum(r['before']['elapsed_ms_median'] for r in rows),2),'after_ms':round(sum(r['after']['elapsed_ms_median'] for r in rows),2),'commands_each_version':18,'read_commands_each_version':9}}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--before',type=Path,required=True);p.add_argument('--after',type=Path,default=Path(__file__).resolve().parents[1]/'plugins/collart-data-assistant');p.add_argument('--output',type=Path,required=True);p.add_argument('--repeats',type=int,default=3);a=p.parse_args()
    if not 1<=a.repeats<=10:p.error('repeats must be 1..10')
    r=benchmark(a.before,a.after,a.repeats);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r['totals'],ensure_ascii=False))
if __name__=='__main__':main()
