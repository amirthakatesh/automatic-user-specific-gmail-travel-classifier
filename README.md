# Automatic User-Specific Gmail Travel Classifier
An access script in Python to seek permission into user's gmail account and classify travel related mails based on user's preferences and dump them into a separate label called "Travel".<br />
1)Make sure you have turned on Keyboard shortcuts in your gmail settings before running the program.<br />				
2)You have to enter password alone in the browser while other inputs are given through terminal.<br /> 
3)All the travel related mails will be classified and sent to label "Travel" in the user's inbox.<br />
4)travel_data() is used to add keywords to the existing list to classify it in even better way.<br />
5)gmail(email,query) logs into the user's account and sends each keyword in query to the function move_to_travel().<br />
6)move_to_travel(katesh,query) is used to find the mails related to the query and move it to the label "Travel".<br />

