// callAPI function 
async function retrieveRecordsFromDatabase() {
    // return an Object with contents of animal table 
    let tableDataObject;
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
        return tableDataObject;
    } catch (error) {
        console.error("Error calling AWS API:", error);
        return null;
    }
  
} //retrieveRecordsFromDatabase

async function displayHeroImagesWithLinks() {
   // populate localTableDataObject via retrieveRecordsFromDatabase [wait for it !]
    let localTableDataObject = await retrieveRecordsFromDatabase();
    let heroArray;
    // reset zoom-container to NULL 
    document.querySelector('.zoom-container').innerHTML=""
    heroArray=createHeroLinksArray(localTableDataObject);
    heroArray.forEach(element => {
      document.querySelector('.zoom-container').innerHTML+= element;
    })
}//displayHeroImagesWithLinks() 

function createHeroLinksArray(localTableDataObject) {
  let returnArray=[];
  console.log("start createHeroLinksArray")
  //Filter objects that match 'hero'
  const heroAnimals = localTableDataObject.filter(item => item.animalname.includes('hero'));
  heroAnimals.forEach(element => {
    console.log(createHeroPicturelink(element));
    //add each hero link to returnArray
    returnArray.push(createHeroPicturelink(element));
  })
  console.log("end createHeroLinksArray")
  return returnArray;
} //createHeroLinksArray

function createHeroPicturelink(input) {
  //create hyperlink with image, label, link to HTML
  const temp = input.animalname;

  let inputString = temp;
  let [animal, type] = inputString.split('-')
  let link =`<a href="${type}.html" class="zoom-img"><img src="${input.image}" alt="${animal} image"  width="300" height="200" > ${type}</a>`;
  return link;
}//createHeroPicturelink


