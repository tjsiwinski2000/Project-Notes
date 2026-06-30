SUMMARY
- Integrate QuickSight, dynamoDB, Athena, 
- 02192025 couldn't finish but got close try in a week; good experience overall tho.
- left arn:aws:dynamodb:us-east-1:396913707603:table/02192025quicksite in place [us east1]

VIDEO
- https://www.youtube.com/watch?v=d1ZsTwR7cB8

NOTES
- created QuickSight account name:tjcloud1965 username:joseph1967
- Athena X[connect] directly to DynamoDB
[Athena]->[Lambda]->[DynamoDB] ::  (*) (*) Visualize w. QuickSight (got that working)

KEY CONCEPT
- Automatically created [Lambda function] turns SQL queries into DynamoDB API calls
- Created everything in US West1 region ; QuickSight <> US West1 , so could NOT (*) (*) anything !
- 02192025 could not create QuickSight run query [permissions ! ugh , S3 buckets may be MONKED]
- Lambda needs SPILL LOCATION due to 6MB limit

Need Three buckets in s3 in us-east-1
go slow and do it one more time

STRUCTURES
[DynamoDB] - 02192025quicksite 
[Athena DataSource] - 02192025-Athena-DS
[Athena Query S3 bucket] - 02192025-queryresults
[ Policy QS->L] - 02192025-QSinvokeLambda
[ Policy QS->B] - 02192025-S3-Spill
[QS DS] - 02192025-Athena


(/) delete QuickSight account [02192025]
