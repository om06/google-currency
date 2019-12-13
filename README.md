# Google currency  

**Disclaimer:** This package fetch the result from Google using web scrapping. 
Owner will not be responsible for any misuse of this package. This is solely for 
the purpose of learning.   

A very simple currency converter.  
  
It can convert the currency of **153 codes.**  
  
Since the results are fetched from ``Google`` directly, you can trust the results :-D  
  
  
## Installation  
  
To install the library run the below command (This will also install ``requests``)  
  
* ``pip install google-currency``  
  
  
## Usage  
```  
from google_currency import convert  
  
convert('usd', 'inr', 1)  
```  
  
This will return a JSON response like below  
  
```  
{  
	 "converted": true, 
	 "from": "USD", 
	 "to": "INR", 
	 "amount": "68.56"
 }  
```  
  
  
## Response description  
  
* converted: Boolean indicating whether the amount is converted or not, if this is ``false`` than it means the  
currency code is not valid and the amount is not converted and it will be equal to ``0``.  
  
* amount: Converted amount  
  
* from: Currency code from which the amount is converted.  
* to: Currency code to which the amount is converted.