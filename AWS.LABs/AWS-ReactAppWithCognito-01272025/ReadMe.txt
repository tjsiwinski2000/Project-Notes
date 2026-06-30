01-27-2025 Building a React App with Amplify

https://www.youtube.com/watch?v=ma1FA2be8Ac
https://github.com/tinytechnicaltutorials/amplify-cognito-quiz

REPO: 
- https://github.com/tjsiwinski2000/amplify-cognito-quiz

SUMMARY:
- Use of React code / libraries to build Quiz App [Q/A in quizData , quiz engine in Quiz.js]
- Ran cmds to install amplify to AWS cli and created profile 
- Cognito was used for account login very very cool.
- GitHub promotion troublesome at first resolved by using [C:\Users\TJ\Documents\GitHub] as a base
- Minor deviations from steps provided necessary but not major drama 
- NOTE: Tested continuous integration continuous deployment (CI/CD) with a GitHub commit which cues automatic update on Amplify hosting backend.

OVERVIEW



0128-2025
- could not push changes to my github
- https://github.com/tjsiwinski2000/amplify-cognito-quiz2.git
- other drama also, deleted and started over 0129-2025

0129-2025
[commands from google doc]
(/) npm install -g @aws-amplify/cli
(/) amplify configure 
- [us-west-1] 
- [access keys from SECURITY TAB of amplify-dev user created in Amplify]
- creating local profile  amplify-dev-local ["dont have to do this every time"]
npx create-react-app <my-quiz-app>
- moved code to [C:\Users\TJ\Documents\GitHub] [very important change]
(/) cd <name of your app>
(/) amplify init
(/) amplify add auth
(/) amplify push
(/) npm install aws-amplify @aws-amplify/ui-react
(/) npm start
- starts the react app local
- added quizData.js , Quiz.js [using VSCodium program]
- npm install --save-dev web-vitals [this fixed an issue, not mentioned in the video]
- at this point everything works localhost ; 
- remainder of this is to promote to AWS cloud

[git commands, slight deviation from tutorial, not her fault]
git init
git add .
git commit –m "Initial commit"
git branch –M main
git remote add origin <repository URL>
git push –u origin main
--this ^ is monk. this [git push --set-upstream origin main] worked


tjsiwinski_2000@yahoo.com
strongpassword

