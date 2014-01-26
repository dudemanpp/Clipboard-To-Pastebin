import win32clipboard
import xml.etree.ElementTree as e
from Pastebin import PastebinAPI

api_dev_key = '**********'
username = '**********'
password = '**********'

def get_clipboard():
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def set_clipboard(text):
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardText(text.encode('utf-8'),
		win32clipboard.CF_TEXT)
	win32clipboard.SetClipboardText(unicode(text),
		win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()

clipboard_text = get_clipboard()
print 'Got text from clipboard'
x = PastebinAPI()
api_user_key = x.generate_user_key(api_dev_key, username, password)
print 'Pasting to Pastebin'
x.paste(api_dev_key, clipboard_text, api_user_key, paste_name = None, paste_format = 'python', paste_private = 'unlisted', paste_expire_date = 'N')
print 'Getting URL'
my_pastes = x.pastes_by_user(api_dev_key, api_user_key, results_limit = 1)
tree = e.fromstring(my_pastes)
url = tree[8].text
set_clipboard(url)
print 'Clipboard set to URL'
