SUMMARY
- continuous deployment pipeline
- [code pipeline]::[source code in GITHUB ]=> S3
- any update to GITHUB triggers pipeline to update S3
- can watch [source] : [build] : [deploy] on pipleline page 
- S3 configured to host 

VIDEO
- https://www.youtube.com/watch?v=biYVW1TMYAU&t=0s

S3 bucket
- [uncheck] block public access
- properties (*) enable website hosting ; index.html
- edit bucket policy (see JSON)

GITHUB
- forked repo, created: https://github.com/tjsiwinski2000/codepipeline-s3-game
- create Pipeline , connected to forked repo ^
- issue with permission to github 
- - ugh downloaded to C:\Users\TJ\source\repos\codepipeline-s3-game
- accidentally create a repo w/in repo but decided simplifiy is best 

NOTES
- pretty straight forward project 
- 0211-2025 trying to adjust style.css so game playable on iPhone [TRYING]
- you can run the project for debbuging locally w/o internet deployment
- NOT DONE 
- - - delete pipeline
- - - delete S3 bucket
- - -



***JSON below for Bucket Policy***
meme-game-02102025
{
    "Version": "2012-10-17",
    "Statement": [
    	{
        	"Sid": "PublicReadGetObject",
        	"Effect": "Allow",
        	"Principal": "*",
        	"Action": [
            	"s3:GetObject"
        	],
        	"Resource": [
                "arn:aws:s3:::Bucket-Name/*"
        	]
    	}
    ]
}
