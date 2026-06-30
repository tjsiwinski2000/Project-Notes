CONCEPT:
- use python api to create interactive GRID 
- users can add / edit / delete entries and display all such 

0708-2025
MAIN   -  https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev
GET ALL - https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/all        (/) works in POSTMAN
CREATE  - https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/create     (/) works in POSTMAN
DELETE - https://497...aws.com/dev/posts/delete/b1c58e68-ca33-4dff-b3af-4b05e2b8373c  (/) in POSTMAN

UPDATE
https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/update/639a86ed-2612-47ab-8f31-80a5cc7e0632
{
  "content" : "updated 825pm",
  "author" : "TJ"
}
(/)in POSTMAN after adding auth token and set fields "content" , "author"

ACTIVATED Access key ID
- AKIAVY2PGRJJZ2GNMDZX 245pm IAM serverless

TODAY-GOAL
- amplify website
- pull all entries and display as table

NOTE:
- how do i test javascript locally?
1.create javascript function =>filename.js
2.cmd prompt [node filename.js]
3.make sure you console output as last step

(/) 4:50pm - ran JS local to return https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/all'
(x) integration with amplify website odd errors / kasparsky lab text in console()
CORS Warning (Browser Limitation)

If the AWS API isn’t configured for CORS (Cross-Origin Resource Sharing), the browser will block the request
- API works local JS (4:50pm)
- API works POSTMAN
- API works direct call via browser
- (x) API fail for call within amplify site calling JS 
(Reason: CORS header ‘Access-Control-Allow-Origin’ missing)
FIX [proposed by chatgpt]
You need to make sure your API returns CORS headers like this
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type

0710-2025
- (/) retested all API endpoints in POSTMAN [attn to detail important]
- (/) retest node .\callAwsApi.js
- (/) CORS addressed for ALL function by adding headers 
NOTE: manually updated in Lambda UserInterface 
===
line #89 in handler.py (in Lambda NOT github)
response = {
"statusCode": 200,
 "headers": {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type"
},
"body": json.dumps(posts)
}
===
  ACCOMPLISHED
 - https://staging.d1hiux42cwg1mp.amplifyapp.com/
 - JS function: callAWSapi -> index.html 

 0715-2025
 - today's goal create edit screen
 - (/) load edit screen with appropriate values
 - (/) headway on how to save
 - (x) Errors -> CORS likely still a snake in the grass

 0716-2025
 -AM  tested changes from 0715-2025 no joy
 -    updated index.html for CORS headers 190-192 still no joy
 -  The Same Origin Policy disallows reading the remote resource at https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/update/639a86ed-2612-47ab-8f31-80a5cc7e0632. (Reason: CORS preflight response did not succeed). Status code: 403

 [network tab] 820pm
 - missing allow header errors
 - added CORS updates to handler.py 91-94 , 136-139

 0717-2025
 index.html
 const updatedData = {
  author: updatedAuthor,
  content: updatedContent
};
index.html
//"Access-Control-Allow-Methods": "PUT,GET,POST,OPTIONS"

Reason: header ‘access-control-allow-origin’ is not allowed according to header ‘Access-Control-Allow-Headers’ from CORS preflight response).
- [ In other words, the client is (or the browser is) asking permission to send a header your server didn't allow.]

Access-Control-Allow-Headers: In its response to the preflight request, the server sends this header to tell the browser which request headers are allowed in the actual request.

[Gemini] You should never send Access-Control-Allow-Origin from the client.
[updated] index.html simplifying headers sent (see below)
headers: {
  'Content-Type': 'application/json',
}

const result = await response; [response.JSON caused failure since didn't return JSON ]
=================================
=================================
0717-2025
- GRID (/) show all  (/) edit SUCCESS !
--------------------------------------------------------
[RESOLUTION SUMMARY]
- CORS does preflight request browser->API; API->browser; 
---Access-Control-Allow-Headers must ~match [action attempted PUT,GET etc. must be in the API]

- Updating Lambda in management console 0710-2025 works but NOT good idea long term.
--- suck it up and update handler.py and [sls deploy]

[Gemini] You should never send Access-Control-Allow-Origin from the client.

- const result = await response.JSON 
--- provide by AI but JSON wasn't being returned so this line would cause FALSE ERROR 

TROUBLESHOOTING FLOW
- does it work in management console (Lambda), mc (API gateway) , POSTMAN, (o)(o) read cloud watch logs, 
- console on web UserInterface / [console], [network]
- JS testing cmd prompt [node filename.js]
--------------------------------------------------------
0720-2025
- add entry form added ; shows on click [add entry] ;  un-shows [cancel]
NEXT
- [submit] on add-entry =>updates dynamoDB

- careful clean up messy code

0721-2025 [error 1:30pm]
XHROPTIONS
https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/create
CORS Preflight Did Not Succeed
OPTIONS
	https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/create
Status
403
blah..blah
[Gemini]You need to configure your AWS API Gateway so that the OPTIONS method for the /dev/posts/create resource does NOT require authorization. This allows the browser's preflight request to succeed, after which it can send the actual POST request (which will then include your authentication token).
>> 155pm API gateway in Management Console didn't require authentication.
>> 155pm added CORS to gateway but got same error.

[error] CORS Preflight Did Not Succeed
- tested in different browser different message lead to update below
"Access-Control-Allow-Origin": "https://staging.d1hiux42cwg1mp.amplifyapp.com",
"Access-Control-Allow-Methods": "PUT,GET,POST,OPTIONS",
"Access-Control-Allow-Headers": "Authorization,Content-Type",
"Access-Control-Allow-Credentials": "true"

0727-2025
[belated update] 
- (/) show all entries  (/) edit an entry (/) add an entry all working
- [ideas] order by a column likely this can be done by JS
-         delete an entry
-         cancel edit button doesn't do anything 

=====================
=====================
 HELPFUL POSH
Remove-Item .\index.zip
Compress-Archive .\index.html index.zip
