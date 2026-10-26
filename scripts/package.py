"""Explicit runtime allowlist; documentation and development files are not hosted."""
from pathlib import Path
import shutil
r=Path(__file__).resolve().parent.parent;out=r/'_site'
if out.exists():shutil.rmtree(out)
out.mkdir()
common=['index.html','app.js','design.css','components.css','i18n.js','translations.json','release.js','sw.js','glass-module.js','manifest.webmanifest','offline.html','playground.html','playground.js','product-pages.css']
extra=['inner-circle.html','member-demo.js','catalog.json']if(r/'catalog.json').exists()else['theme.css','commercial.html','catalog-review.js']
for name in common+extra:shutil.copy2(r/name,out/name)
for name in ['assets','licenses']:shutil.copytree(r/name,out/name)
(out/'.nojekyll').touch()
print('Packaged',len(list(out.rglob('*'))),'public runtime entries')
