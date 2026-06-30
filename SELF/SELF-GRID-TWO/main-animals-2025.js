// NOTE: not used 0922-2025 
// ...............TJSiwinski

// global var to hold current contents
let tableDataObject ;

// Get references to the *edit* form elements and container
const editFormContainer = document.getElementById("editFormContainer");
const editForm = document.getElementById("editForm");
const editUuidInput = document.getElementById("editUuid");
const editNameInput = document.getElementById("editName");
const editImageInput = document.getElementById("editImageInput");
const cancelEditButton = document.getElementById("cancelEdit");

// Get references to the *add* form elements and container
const addFormContainer = document.getElementById("addFormContainer");
const addForm = document.getElementById("addForm");
const addNameInput = document.getElementById("addNameInput");
const addImageInput = document.getElementById("addImageInput");
const cancelAddButton = document.getElementById("cancelAdd");

//0825-2025 loade HERO images
window.addEventListener("load", function() {
  console.log("Page fully loaded!");
  displayHeroImagesWithLinks();
});

async function addEntry() {
    console.log("start-addEntry");
    addFormContainer.style.display = "block"
    console.log("end-addEntry");
}

// callAPI function 
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

async function displayHeroImagesWithLinks() {
   // populate tableDataObject via retrieveRecordsFromDatabase [wait for it !]
    await retrieveRecordsFromDatabase();
    let heroArray;
    // reset zoom-container to NULL 
    document.querySelector('.zoom-container').innerHTML=""
    heroArray=createHeroLinksArray();
    heroArray.forEach(element => {
      document.querySelector('.zoom-container').innerHTML+= element;
    })
}//displayHeroImagesWithLinks() 

async function displayAllRecordsInHTMLgridTable(){
    // populate tableDataObject via retrieveRecordsFromDatabase [wait for it !]
    await retrieveRecordsFromDatabase();
     console.log("---------------------")               
    //const todos = JSON.parse(apiInput);
    const delimitor_cell="</td><td>";
    let gridOutput="";
    
    const allAnimals = tableDataObject;
    allAnimals.forEach(element => {
        let temp="";
        let row="<tr><td>";
        row += createIDlink(element.id) + delimitor_cell;
        row += element.animalname + "09222025"+delimitor_cell;
        row += (element.image || 'N/A') +delimitor_cell;
        if (element.updatedAt) {temp=convertToShortDate(element.updatedAt) } else {temp="N/A"}
        row += (temp) +delimitor_cell ;
        if (element.funfacts) {temp = element.funfacts} else {temp = "N/A"} 
        row += (temp) + "</td></tr>";
        //if (element.updatedAt) {temp=convertToShortDate(element.updatedAt) } else {temp="N/A"}
        //row += (temp) + "</td></tr>";
        console.log(row);
        gridOutput +=row;
    });
    // update HTML table with API output 
    document.querySelector('.js-grid-output').innerHTML=gridOutput;
    
} //displayAllRecordsInHTMLgridTable

function createHeroLinksArray() {
  let returnArray=[];
  console.log("start createHeroLinksArray")
  //Filter objects that match 'hero'
  const heroAnimals = tableDataObject.filter(item => item.animalname.includes('hero'));
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

function convertToShortDate(dateTimeString) {
    const date = new Date(dateTimeString);
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return date.toLocaleDateString('en-US', options);
} //convertToShortDate

function createIDlink(id) {
    //create hyperlink with abbreviated uuid
    let displayID=id.substring(0,8);
    let link="<a href='#' onclick=showID('" + id + "')>" + displayID + "</a>";
    return link;
} //createIDlink

function showID(idNumber) {
    console.log("Starting edit process for Identification Number: " + idNumber + " may the force be with you.");
    // find corresponding entry in global-object
    const entryToEdit = tableDataObject.find(item => item.id === idNumber);
    console.log(entryToEdit);

    //Populate the form fields with entry's data
    if (entryToEdit) {
        editUuidInput.value = entryToEdit.id;
        editNameInput.value = entryToEdit.animalname;
        editImageInput.value = entryToEdit.image;
        //alert("found " + entryToEdit.content);
        // Display the form
        editFormContainer.style.display = "block"
    }

}


editForm.addEventListener("submit", async function(event) { // Make the function async
    event.preventDefault(); // Prevent default form submission
  
    // Get updated values from the form
    const updatedName = editNameInput.value;
    const updatedImage = editImageInput.value; 
  
    // Create an object with the data to send to your API
    const updatedData = {"animalname": updatedName,
      "image": updatedImage};
    console.log("about to log data object");
    console.log(updatedData);
    console.log("finished logging data object")
    const updatedDataAsString=JSON.stringify(updatedData);
    console.log("about to log data string")
    console.log(updatedDataAsString);
    console.log("finished logging updated data string")
    try {
      // 1. Make the API call to update the database
        const response = await fetch(`https://mzf4a0i1i0.execute-api.us-east-1.amazonaws.com/dev/posts/update/${editUuidInput.value}`, { 
        method: 'PUT', 
        headers: {
          'Content-Type': 'application/json',
          //"Access-Control-Allow-Origin": "*",
          //"Access-Control-Allow-Methods": "PUT,GET,POST,OPTIONS"
          // Add any necessary authentication headers (e.g., 'Authorization': 'Bearer YOUR_TOKEN')
        },
        body: updatedDataAsString // Send the updated data as JSON
      });
  
      // 2. Check if the API request was successful
      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }
  
      // 3. Parse the response 
      const result = await response;
      console.log('API update successful:', result);
  
      editFormContainer.style.display = "none"; // Make edit form invisible
      editForm.reset(); // Clear form fields
      retrieveRecordsFromDatabase(); // update User Interface with the latest data
      alert("Entry updated successfully!");
  
    } catch (error) {
      console.error('Error updating entry:', error);
      alert('Failed to update entry. Please try again. ' + error.message);
      // Optionally, re-enable the form fields or show a specific error message on the form
    }
  }); //editForm.addEventListener


addForm.addEventListener("submit", async function(event) { // Make the function async
        event.preventDefault(); // Prevent default form submission
          // Get  values from the form
        const addName = addNameInput.value;
        const addImage = addImageInput.value; 
          // Create an object to send to  API
        const addData = {"animalname": addName,
        "image": addImage};
        console.log("about to log add-data object");
        console.log(addData);
        console.log("finished logging add-data object")
        const addDataAsString=JSON.stringify(addData);
        console.log("about to log add-data string")
        console.log(addDataAsString);
        console.log("finished logging updated add-data string")
        try {
            // 1. Make the API call to update the database
              const response = await fetch(`https://mzf4a0i1i0.execute-api.us-east-1.amazonaws.com/dev/posts/create`, { 
              method: 'POST', 
              headers: {
                'Content-Type': 'application/json',
                //"Access-Control-Allow-Origin": "*",
                //"Access-Control-Allow-Methods": "PUT,GET,POST,OPTIONS"
                // Add any necessary authentication headers (e.g., 'Authorization': 'Bearer YOUR_TOKEN')
              },
              body: addDataAsString // Send the updated data as JSON
            });
        
          // 2. Check if the API request was successful
            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
            }

            // 3. Parse the response 
            const result = await response;
            console.log('API update successful:', result);

            addFormContainer.style.display = "none"; // Make edit form invisible
            addForm.reset(); // Clear form fields
            retrieveRecordsFromDatabase(); // update User Interface with the latest data
            alert("Entry updated successfully!");
        } //try
        catch (error) {
        console.error('Error updating entry:', error);
        alert('Failed to update entry. Please try again. ' + error.message);
        } //catch
});//addForm.addEventListener


cancelAddButton.addEventListener("click", function() {
    addFormContainer.style.display = "none"; // Make the form invisible
});

cancelEditButton.addEventListener("click", function() {
    editFormContainer.style.display = "none"; // Make the form invisible
});
