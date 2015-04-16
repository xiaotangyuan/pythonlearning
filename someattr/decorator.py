#coding=utf-8
#def foo(x):
#	x['age']=x['age']+1
#	print 'functon foo iner:',locals(),globals()
#
#x={'age':1}
#foo(x)
#print x['age']
#print 'foo outer:',locals(),globals()

def d(func):
	def _deco():
		print '---'
		func()
		print '+++'
		#return func
	return _deco
@d
def func(x):
	print locals()

#d(func)
x=1
func(x)
