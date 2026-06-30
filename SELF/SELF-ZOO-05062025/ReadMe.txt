GOAL
- animal pictures; click animal-> query dynamo db -> display info

URL:
https://staging.d1x2d6helm022y.amplifyapp.com/

ToDo:
fix smileyrachel.com -> website

0506-2025
PROOF-OF-CONCEPT
- created lambda: 0506-2025
- assigned ^ [permissions tab] ExecutionPolicy0506-2025.txt [see separate file]
- test event ^ needs ID e.g. {"ID": "8.0","key2": "value2","key3": "value3"}
- successfully returned data from table 0502-2025
=======================
(/) GOAL: 12:20
- (/) make animal table with one entry and lambda to return data 
table:Animal_05062025
- arn:aws:dynamodb:us-west-1:396913707603:table/Animal_05062025
lambda: Animal_Query_05062025 [USE:LambdaProof_of_Concept05062025.txt as model]
- (/) put correct table name in lambda
- (/) add policy=> [configuration] : [permissions] : [click default role created]
- - - -[add permissions|create inline|JSON|paste template|update template with ARN]
=======================
GOAL:
- make API Gateway
Animal_API_05062025
- (/) https://x6z0c0wpih.execute-api.us-west-1.amazonaws.com/dev

(x)index.html to return and display tiger fact
Amplify WebSite
- https://staging.d33b3xpg5kysw8.amplifyapp.com/
- 12:55pm 05062025 not working 

Add to animal website
0508-2025
() goal fix issue from 0506-2025
() add to animal website
() interesting CORS discussion
- https://nodeployfriday.com/posts/cors-cyber-attacks/
- https://www.serverless.com/framework/docs/providers/aws/events/apigateway
- API, Lambda access works, website X

0509-2025
- NEXT (digest and apply) : https://repost.aws/questions/QU635rwTypSkGxh1SOmhpahA/preflight-issue-with-aws-api-gateway-and-lambda-function