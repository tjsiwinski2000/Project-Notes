//0825-2025 load HERO images
window.addEventListener("load", function() {
  console.log("Page fully loaded!");
  displayHeroImagesWithLinks();
});

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