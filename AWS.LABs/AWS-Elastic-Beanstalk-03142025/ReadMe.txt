03-14-2025 Elastic Beanstalk

https://www.youtube.com/watch?v=Ht1COADOsNI

Notes
- APPLICATION
basically a FOLDER ~ kind of 
inlcudes EC2 instances, LB, ASG
can have many [versions] / can have many saved [configurations]
code stored S3

==KEY CONCEPTS==
APPLICATION
- create from left menu
- then create application
- single instance (free tier eligible) ~ one VM

SERVICE ROLE 
- an IAM role that Elastic Beanstalk assumes to interact with other AWS services [e.g. EC2, ASG, LB]
- created a role my-new-aws-beanstalk-role [applied 3x policies]

EC2 INSTANCE PROFILE
- an IAM role that is attached to an EC2 instance in the Elastic Beanstalk environment
- Purpose: Application [on EC2 instance] => interact => [other AWS services]


MISC Notes
Video mentioned using CMD line to determine [below maybe correct]
[ aws iam list-instance-profiles-for-role --role-name aws-elasticbeanstalk-service-role ]

Launched python application
- default app "baked in"
- after creating the Beanstalk there is a link to the DOMAIN

Auto Scaling Group Created 
awseb-e-8p34n7psah-stack-AWSEBAutoScalingGroup-C3vhJQeNmW1J
^ note: awseb
