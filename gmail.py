import csv
import getpass
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


#############################################################################################################################
#INSTRUCTIONS
#############################################################################################################################
#1)Make sure you have turned on Keyboard shortcuts in your gmail settings before running the program.				
#2)You have to enter password alone in the browser while other inputs are given through terminal. 
#3)All the travel related mails will be classified and sent to label "Travel" in the user's inbox.
#4)travel_data() is used to add keywords to the existing list to classify it in even better way.
#5)gmail(email,query) logs into the user's account and sends each keyword in query to the function move_to_travel().
#6)move_to_travel(katesh,query) is used to find the mails related to the query and move it to the label "Travel".
#############################################################################################################################

def move_to_travel(katesh,query):
	emailElem = katesh.find_element_by_id('gbqfq')
	emailElem.send_keys(query+" category:updates"+Keys.ENTER)
	delay = 10000
	try:
		myElem = WebDriverWait(katesh, delay)
		eEm = katesh.find_element_by_id('gbqfqw')			
		eEm.send_keys("*a")
		eEm.send_keys(Keys.SHIFT+"*a")
		myElem = WebDriverWait(katesh, delay)
		eEm.send_keys(Keys.SHIFT+"*a")
		myElem = WebDriverWait(katesh, delay)
		eEm.send_keys("l")
		myElem = WebDriverWait(katesh, delay)
		eEm.send_keys("travel"+Keys.ENTER)
		myElem = WebDriverWait(katesh, delay)
		emailElem = katesh.find_element_by_id('gbqfq')
		emailElem.send_keys(Keys.CONTROL+"a")
		myElem = WebDriverWait(katesh, delay)
		emailElem.send_keys(Keys.DELETE)		
			 												
	except TimeoutException:
		print("Loading took too much time!")

def gmail(email,query):
	print("Opening your browser...")
	global driver
	katesh = webdriver.Firefox()#Enter executable path	
	katesh.get('https://accounts.google.com/ServiceLogin')	
	emailElem = katesh.find_element_by_id('identifierId')
	emailElem.send_keys(email+Keys.ENTER)
	print("Have you entered your password?(yes/no)[Press ENTER after the page is completely loaded]")
	pas=raw_input()
	k=[]
	for j in query:
		k.append(katesh)
	if pas=="yes":
		print("Opening your mail...")
		emailElem = katesh.find_element_by_css_selector('.WaidBe').click()
		print("Yaay! We have entered your mail I guess?(yes/no)[Press ENTER after the page is completely loaded]")
		pas=raw_input()
		if pas=="yes":
			delay=2000
			for i in range(len(query)):
				myElem = WebDriverWait(katesh, delay)
				
				move_to_travel(k[i],query[i])

def travel_data():
	ss=[]
	L=[]
	R=[]
	res=''
	with open('travel_data_set.csv','rb') as csvfile:
		spamwriter = csv.reader(csvfile, delimiter=' ',quotechar='|')
		for row in spamwriter:
			R.append(row[0])
	print("Want to add any keyword for categorising your travel related mails?(yes/no)")
	ifs=raw_input()

	while ifs=='yes':
		s=raw_input()
		if s not in R:
			ss.append(s)
			L.append(ss)
			with open('travel_data_set.csv', 'ab') as csvfile:
				spamwriter = csv.writer(csvfile, delimiter=' ')
				for i in L:
		    			spamwriter.writerow(i)
		else:
			print("Your keyword is already present in our dataset! Anyway thanks for helping us out!")
		ifs=raw_input("Want to add more?(yes/no)")
	R=[]
	with open('travel_data_set.csv','rb') as csvfile:
		spamwriter = csv.reader(csvfile, delimiter=' ',quotechar='|')
		for row in spamwriter:
			for i in range(len(row)):
				res+=row[i]+' '
			R.append(res.strip())
			res=''
	R.append('  ')
	return R


email = raw_input("Enter gmail : ")
query=travel_data()
gmail(email,query)







