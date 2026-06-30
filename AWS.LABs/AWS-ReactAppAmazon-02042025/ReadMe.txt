AWS-ReactLab

SUMMARY
-You have deployed a React application in the AWS Cloud by integrating with GitHub and using AWS Amplify. 
With AWS Amplify, you can continuously deploy your application in the Cloud and host it on a globally available CDN.

URL
- https://aws.amazon.com/getting-started/hands-on/build-react-app-amplify-graphql/module-one/

NOTES
npm create vite@latest notesapp -- --template react
cd notesapp
npm install
npm run dev
[at this point react app is working: http://localhost:5173/]

[navigate to C:\Users\TJ\notesapp]
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/tjsiwinski2000/notesapp.git
git branch -M main
git push -u origin main

[navigate to C:\Users\TJ\notesapp]
npm create amplify@latest -y
// when completes
git add .
git commit -m 'installing amplify'
git push origin main

[Connect the GitHub repository you just created to AWS Amplify. This will enable you to build, deploy, and host your app on AWS.]
- create new Amplify app / take defaults /give amplify permission to GIT repository / test app matches http://localhost:5173/
- make a change to App.tsx file / go back to ampify console [NOTE: reddeploying]