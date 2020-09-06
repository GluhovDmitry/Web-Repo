def wsgi_application(environ, start_response):
	status = '200 OK'
	headers = [('Content-Type','text/plain')]
	return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding = "utf-8")]
	
