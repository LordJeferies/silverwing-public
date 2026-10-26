"""Release gate: paths, scripts, translations and immutable offer boundaries."""
from pathlib import Path
import json,re,subprocess,sys
from html.parser import HTMLParser
r=Path(__file__).resolve().parent.parent
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key not in ['src','href'] or not value or value.startswith(('#','http:','https:','mailto:','data:','blob:','tel:')):continue
   target=value.split('#')[0].split('?')[0]
   if target and not (r/target).exists():raise ValueError(f'Missing asset: {target}')
for path in r.glob('*.html'):Links().feed(path.read_text())
for path in r.glob('*.js'):subprocess.run(['node','--check',str(path)],check=True,capture_output=True)
d=json.loads((r/'translations.json').read_text());assert all(isinstance(v.get('es'),str)and isinstance(v.get('en'),str)for v in d.values())
# Evaluate only definitions from our app, in a locked-down VM with no browser APIs.
js="""const fs=require('fs'),vm=require('vm');const app=fs.readFileSync(process.argv[1]+'/app.js','utf8');const start=app.slice(0,app.indexOf('const $='));const scope={};vm.createContext(scope);vm.runInContext(start+';this.offer={PLAN,SOURCE,STYLE}',scope);const{PLAN,SOURCE,STYLE}=scope.offer;let count=0;for(const[p,price,total]of [['stay',399,12],['daily',799,28],['maximum',999,64]]){if(PLAN[p].total!==total||PLAN[p].reels+PLAN[p].carousels+PLAN[p].memes!==total)throw Error('Mix');if(PLAN[p].price!==price)throw Error('Price');for(const s of Object.keys(SOURCE))for(const q of Object.keys(STYLE)){if(!Number.isFinite(PLAN[p].price+SOURCE[s].price+STYLE[q].price))throw Error('Total');count++}}if(SOURCE.own.price!==0||SOURCE.guided.price!==500||SOURCE.interview.price!==1000||STYLE.clean.price!==0||STYLE.dynamic.price!==199||STYLE.cinematic.price!==399)throw Error('Addons');console.log(count+' quote combinations verified');"""
subprocess.run(['node','-e',js,str(r)],check=True)
if (r/'catalog.json').exists():
 c=json.loads((r/'catalog.json').read_text());assert c['status']=='approved'and c['period']=='4-weeks'and c['currency']=='USD'and c['version']==1
 for group,keys in [('plans',['stay','daily','maximum']),('sources',['own','guided','interview']),('styles',['clean','dynamic','cinematic'])]:
  assert sorted(c[group])==sorted(keys)
  for v in c[group].values():assert isinstance(v['price'],(int,float))and 0<=v['price']<=100000
 assert c['sources']['own']['price']==0 and c['styles']['clean']['price']==0
 for k,counts in {'stay':(6,4,2),'daily':(12,8,8),'maximum':(24,20,20)}.items():
  p=c['plans'][k];assert tuple(p[x]for x in ['reels','carousels','visuals'])==counts and p['pieces']==sum(counts)
 assert c['limits']=={'periodWeeks':4,'guidedScripts':8,'remoteInterviews':2,'interviewMinutes':[45,60],'enhancedReels':4,'innerCircleIncluded':True,'benefitsSubjectToAvailability':True}
 assert set(c)<=set(['version','status','currency','period','plans','sources','styles','limits','approval'])
 assert not (r/'catalog-review.js').exists(),'Commercial package must not contain Studio tooling'
print('PASS: local paths, JS syntax, translations and offer invariants')
