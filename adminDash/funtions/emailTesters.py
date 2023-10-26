from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import datetime
import json




def sendTestEmailTo(recipient):
	emailData = getDataFromTheJson()

	currentTime = datetime.datetime.now()
	subject = 'Test'
	html_message = render_to_string('adminDash/mailTemplates/testmailTemplate.html', {'CurrentTime': currentTime})
	plain_message = strip_tags(html_message)
	from_email = emailData['fromMailAddr']
	to = recipient


	mail.send_mail(
		subject,
		plain_message,
		from_email,
		[to],
		fail_silently=False,
		html_message=html_message,
	)




def getDataFromTheJson():
	with open('adminDash\emailData.json', 'r') as openfile:
		emData = json.load(openfile)

	print(emData)
	print(type(emData))
	return emData



