import sys,re,collections,json
def run(t):
 rows=[re.match(r'([^:]+):\s*(.*)',x) for x in t.splitlines()]; rows=[x.groups() for x in rows if x]; c=collections.Counter(a for a,_ in rows); qs=sum('?' in m for _,m in rows)
 return {'messages':len(rows),'messages_by_speaker':dict(c),'questions':qs,'avg_words':round(sum(len(m.split()) for _,m in rows)/max(1,len(rows)),1)}
if __name__=='__main__': print(json.dumps(run(open(sys.argv[1]).read() if len(sys.argv)>1 else input('Speaker: message')),indent=2))