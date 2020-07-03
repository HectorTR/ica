def on init(t) :
	gridlabd.output("timestamp,x")
	return True

def on_sync(t) :
	gridlabd.output("%s,%s"%(gridlabd.get_global("clock"),gridlabd.get_object("my_test")["x"]))
	return gridlabd.NEVER

def commit(obj,t) : 
	gridlabd.debug("%s.commit(obj='s%',t=%d) ok" % (gridlabd.__name__,obj,t))
	return gridlabd.NEVER
	


