window.addEventListener("load", function() {
  console.log("Page fully loaded!");
  displayAllImagesForGenre();
});

 async function displayAllImagesForGenre() {
  // determine genre from page name e.g. fish for fish.html
  const path = window.location.pathname; // get current page (e.g. "fish.html")
  const page = path.substring(path.lastIndexOf('/') + 1); // fish.html
  const baseName = page.split('.')[0]; // "fish"
  console.log("animal genre is: " + baseName);
  genreArray= await createGenreLinkArray(baseName);

  document.querySelector('.zoom-container').innerHTML=""
  genreArray.forEach(element => {
    document.querySelector('.zoom-container').innerHTML+= element;
  console.log(element)
  })
  //0915-2025 Update TJS
          // Select the right-section div
          const rightSection = document.querySelector('.right-section');

          // Get all the links that should trigger the update
          const animalLinks = document.querySelectorAll('.animal-link');
  
          // Add a click event listener to each link
          animalLinks.forEach(link => {
          link.addEventListener('click', async (event) => {
              // Prevent the browser from navigating away from the page
              event.preventDefault();
      
              // Get the animal name from the data attribute
              const animalid= link.getAttribute("animalid");
              console.log(animalid);
              // Retrieve and display fun fact in right pane
              rightSection.innerHTML= await retrieveFunFact(animalid);
              });
          });
  //0915-2025 Update END TJS
} //displayAllImagesForGenre

async function retrieveFunFact(animalid){
  // populate localTableDataObject via retrieveRecordsFromDatabase [wait for it !]
  let localTableDataObject = await retrieveRecordsFromDatabase();
  // temp var to hold initial return from database
  let stemp="";
  let returnFacts="";

  console.log("in retrieveFunFact, looking for ", animalid)
  
  //Filter objects that match specific animal id passed in
  const specificAnimal = localTableDataObject.find(item => item.id === animalid);

  if (specificAnimal){
    stemp=specificAnimal.funfacts;
    console.log(stemp)
    //format returnFacts
    const sentences = stemp.split(/\. /).map(str => str.trim()).filter(Boolean);
    sentences.forEach((sentence, i) => {
    // Add back the period if missing
    if (!sentence.endsWith(".")) sentence += ".";
    returnFacts += `<strong>${i + 1}.</strong> ${sentence}<br><br>`;
});
console.log (returnFacts)
  } else {
    console.log("Animal not found!");
  }

  console.log("completed retrieveFunFact")
  return returnFacts;
 
} //retrieveFunFact

async function createGenreLinkArray(animal){
    // populate localTableDataObject via retrieveRecordsFromDatabase [wait for it !]
    let localTableDataObject = await retrieveRecordsFromDatabase();
    let returnArray=[];

    //Filter objects that match specific animal passed
    const genreAnimals = localTableDataObject.filter(item => item.animalname.includes(animal));
    genreAnimals.forEach(element => {
      //save for debug console.log(element);
      console.log(createGenrePicturelink(element));
      //add each hero link to returnArray
      returnArray.push(createGenrePicturelink(element));
    })
    console.log("end createGenreLinkArray")
    return returnArray;
} //createGenreLinkArray

function createGenrePicturelink(inputString){
  //0915-2025 add id to html link to facilitate dispalying fun facts
  const id=inputString.id

  //name e.g. tiger-mammal
  const name=inputString.animalname;

  let [animal, type] = name.split('-')
  let link =`<a href="${animal}.html" animalid=${id} class="zoomimg animal-link"><img src="${inputString.image}" alt="${animal} image"  width="300" height="200" >${animal}</a>`;
  return link;
}