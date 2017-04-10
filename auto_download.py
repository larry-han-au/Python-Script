import urllib
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


class GetDataInstance:
	def __init__(self):
		self.isDownloaded = False
		self.hour = 19
		self.minutes_lower = 14
		self.minutes_uppper = 59
		self.reset_hour = 1

	def sendEmail(self, name):

		msg = MIMEMultipart()
		att1 = MIMEText(open(name, 'rb').read(), 'base64', 'gb2312')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = 'attachment; filename="' + name + '"'
		msg.attach(att1)

		msg['to'] = 'sherryxie@rmhedge.com'
		msg['from'] = 'hanliang512288@gmail.com'
		msg['subject'] = name
		try:
			server = smtplib.SMTP_SSL()
			server.connect('smtp.gmail.com')
			server.login('hanliang512288@gmail.com','woaixieshiyi1314')
			server.sendmail(msg['from'], msg['to'],msg.as_string())
			server.quit()
			print "Mail: "+ name + " has been sent."
		except Exception, e:
			print "Fail: " + str(e)

	def download(self,timestamp):
		seq = [timestamp.year , timestamp.month , timestamp.day , timestamp.hour , timestamp.minute]
		seq = list(map(lambda x: str(x), seq))
		url = 'https://www.emcsg.com/marketdata/priceinformation?downloadRealtime=true'
		name = "-".join(seq) + ".csv"
		urllib.urlretrieve(url, name)
		print name + " is downloaded."
		self.sendEmail(name)

	def loopRun(self):
		while True:
			now = datetime.datetime.now()
			hour = now.hour
			minute = now.minute
			print "TimeStamp:" + " " + str(hour)  + "-" + str(minute)
			if hour == self.hour and minute > self.minutes_lower and minute < self.minutes_uppper and (not self.isDownloaded):
				self.download(now)
				self.isDownloaded = True

			time.sleep(60*5)

			if hour == self.reset_hour and self.isDownloaded:
				self.isDownloaded = False
				print "Reset: It's a new day, reset timer."

			print "Bad Time: not time for downloading."



if __name__ == "__main__":
	instance = GetDataInstance()
	instance.loopRun()