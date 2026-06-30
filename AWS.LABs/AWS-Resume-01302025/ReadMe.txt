Resume Builder with AWS

VIDEO: https://www.youtube.com/watch?v=NiCZSdWucZE

NOTES:
- Bucket Name needs to match domain name.
- purchased tjsiwinski.com

if purchase domain name AWS creates HOSTED ZONE automatically
HOSTED ZONE - (basically) container for different records and rules that handle  traffic from the internet.

Used chatgpt to build resume placeholder HTML and style sheet CSS.Placed in S3 bucket.

We cannot apply certificate to S3 bucket.
So we apply certificate to Cloud Front distribution.

Certificate Manager
- region set N.Virginia
- N.Virginia ->compatible->CloudFront

Using certificate manager we create C-Name record in Route53
[DOMAIN SECTIN] [create record button]
Point Cloud Front distribution => S3 bucket.

0403-2025-WORK
created new certificate
- 2ccf41be-1638-459f-91bd-612ff22c59b3
new CNAME record in tjsiwinski.com 
- _3f9496594d787321a022b07fa964098d.tjsiwinski.com
created new CloudFront distribution 0403-2025
- https://d3bpixzs7i4feo.cloudfront.net
( ^  working)


[SUMMARY OF THE VIDEO]
04:48 – Creating HTML, CSS and JavaScript files-with the help of ChatGPT
06:55 – How to use the code that I provide
07:34 – Creating an S3 bucket
07:56 – Choosing a name for the S3 bucket that will work with Route 53
09:09 – Configuring the S3 bucket for static website hosting
09:52 – Creating a bucket policy to allow public read access in the S3 bucket
10:46 – Uploading resume code files to the S3 bucket
11:24 – Testing things out with the S3 bucket website endpoint
12:09 – Registering a domain name with Route 53
13:26 – How to work with domains from external providers, like GoDaddy or NameCheap
15:15 – Creating an A Record in Route 53 to point to an S3 bucket website
16:36 – Viewing the status of DNS propagation in Route 53
17:33 – Requesting a public SSL/TLS certificate in AWS Certificate Manager
19:17 – How to do DNS validation for a public SSL/TLS certificate in AWS Certificate Manager
21:14 – Using an SSL/TLS certificate for a website in AWS
21:32 – Creating a CloudFront distribution to point to our static website in S3
23:42 – Launching the CloudFront distribution domain name
24:46 – Updating the A Record in Route 53 to point to the CloudFront distribution