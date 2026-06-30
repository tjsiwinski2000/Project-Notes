 // Get updated values from the form
 const updatedAuthor = editAuthorInput.value;
 const updatedContent = editContentInput.value; 

 // Create an object with the data to send to your API
 const updatedData = {"author": updatedAuthor,
   "content": updatedContent};
 console.log("about to log data object");
 console.log(updatedData);
 console.log("finished logging data object")
 const updatedDataAsString=JSON.stringify(updatedData);
 console.log("about to log data string")
 console.log(updatedDataAsString);
 console.log("finished logging updated data string")
 try {
   // 1. Make the API call to update the database
    const response = await fetch(`https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/update/${editUuidInput.value}`, { 
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
});