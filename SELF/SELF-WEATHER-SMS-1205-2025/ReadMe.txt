Goal:
- convert weather project 
- FROM: Udemy Boot Camp (35) -> TO: Lambda->automated SMS daily

PYTHON
- python stand-alone-files working (note: textbelt.com for SMS)
- copy located in 
C:\Users\TJ\source\repos\Project-Notes\SELF\SELF-WEATHER-SMS-1205-2025\pycharm-files

LAMBDA
- converted python to lambda
- copy located in
C:\Users\TJ\source\repos\Project-Notes\SELF\SELF-WEATHER-SMS-1205-2025
C:\Users\TJ\AppData\Local\Temp\aws-toolkit-vscode\lambda\us-west-1\1204-2025-Weather-SMS
- needed to add request module as [layer]
ARN: arn:aws:lambda:us-west-1:770693421928:layer:Klayers-p312-arm64-requests:19

EVENT-SCHEDULE
- https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html#eb-cron-expressions
- might be easier to create and edit in GUI since setup cryptic e.g. cron(30 13 * * ? * )

CLOUD WATCH LOGS
- https://us-west-1.console.aws.amazon.com/cloudwatch/home?region=us-west-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252F1204-2025-Weather-SMS 

0406-2026
https://us-west-1.console.aws.amazon.com/events/home?region=us-west-1#/scheduled-rule/1204-2025-Schedule-Weather-SMS-Lambda
disabled this schedule , text messages ran out $10 spent , didn't want to continue it