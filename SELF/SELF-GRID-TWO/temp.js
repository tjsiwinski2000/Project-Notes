const stemp='[{"createdAt": "2025-08-19T20:50:22.302321", "id": "df79c4b2-e4dd-49b6-bfa7-70f9c431c054", "image": "s3", "animalname": "tiger-mammal-hero", "updatedAt": "2025-08-20T22:45:08.422937"}, {"createdAt": "2025-08-20T22:42:11.112952", "id": "2249ac35-00f5-44cc-911d-7d78304a7681", "image": "s3 location", "animalname": "squirrel-mammal"}, {"createdAt": "2025-08-19T20:33:33.408631", "id": "883c6620-3ca6-4661-a093-95734f843f15", "image": "s3", "animalname": "monkey-mammal", "updatedAt": "2025-08-21T14:28:53.091651"}, {"createdAt": "2025-08-19T20:31:37.276786", "id": "de15cee6-102e-4f55-9827-b588ad10de35", "image": "s3", "animalname": "elephant-mammal-hero"}, {"createdAt": "2025-08-17T02:10:44.432391", "id": "f749eeb3-89e9-4737-be4c-e487b1d63e0e", "image": "s3//path/there", "animalname": "frog-reptile-hero", "updatedAt": "2025-08-19T20:21:14.936015"}, {"createdAt": "2025-08-20T22:30:00.625761", "id": "aba37768-450b-4750-b214-ead7f92e5102", "image": "s3://path here", "animalname": "preyingmantis-insect-hero"}, {"createdAt": "2025-08-19T20:22:31.917533", "id": "38b30d1b-4185-4e85-80f2-bd800e570f77", "image": "s3", "animalname": "lion-mammal", "updatedAt": "2025-08-21T14:29:04.883518"}]';

//Parse the JSON => JavaScript array of objects
const dataArray = JSON.parse(stemp);

dataArray.forEach(element => {
  console.log(element)
});
console.log("------------------------------");

//Filter objects that match 'hero'
const heroAnimals = dataArray.filter(item => item.animalname.includes('hero'));
heroAnimals.forEach(element => {
  console.log(createHeroPicturelink(element));
})

/*Desired output
<a href="mammal.html">
  <img src="s3" alt="tiger image">
  <p>tiger</p>
</a>*/
function createHeroPicturelink(input) {
  //create hyperlink with image, label, link to HTML
  const temp = input.animalname;

  let inputString = temp;
  let [animal, type] = inputString.split('-')
  let link =`<a href="${type}.html"><img src="${input.image}" alt="${animal} image"> <p>${type}s</p></a>`;
  return link;
}

/*
login as root and run this via cloud shell
 aws s3 rb s3://elasticbeanstalk-us-west-1-396913707603   --force
 aws s3 rb s3://elasticbeanstalk-us-east-1-396913707603 --force
 aws s3 rb s3://elasticbeanstalk-ap-northeast-2-396913707603 --force
 Ilov31914chocol@tepuppie5TJ
 can you creat a quiz to help me practice for AWS AI Practitioner Exam?
 */

 // 0822-2025 temp addition
    // reset zoom-container to NULL 
   /* document.querySelector('.zoom-container').innerHTML=""
    heroArray=createHeroLinksArray();
    heroArray.forEach(element => {
      document.querySelector('.zoom-container').innerHTML+= element;
    })*/

  let s=""
  if (s.length== 0){console.log("s is undefined")}else{console.log("s is defined")}

  //0901-2025
  async function retrieveRecordsFromDatabase() {
    // populate global variable tableDataObject with contents of animal table 
    console.log("start-retrieveRecordsFromDatabase");
    try {
        const response = await fetch('https://mzf4a0i1i0.execute-api.us-east-1.amazonaws.com/dev/posts/all');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.text(); // or use .json() if the response is JSON
        const resultString = data;
        // initial global var with values pulled from API, convert to object 
        tableDataObject=data;
        tableDataObject = JSON.parse(tableDataObject);
        console.log(tableDataObject);
        //displayAllRecordsInHTMLgridTable(resultString);
        //return resultString;
        console.log("end-retrieveRecordsFromDatabase");

    } catch (error) {
        console.error("Error calling AWS API:", error);
        return null;
    }
    
} //retrieveRecordsFromDatabase