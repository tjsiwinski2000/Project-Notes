
//Gemini provided code , edit by TJS 0715-2025
editForm.addEventListener("submit", async function(event) { // Make the function async
  event.preventDefault(); // Prevent default form submission

  // Get updated values from the form
  const updatedAuthor = editAuthor.value;
  const updatedContent = parseInt(editContentInput.value); 

  // Create an object with the data to send to your API
  const updatedData = {
    name: updatedAuthor,
    age: updatedContent
  };

  try {
    // 1. Make the API call to update the database
    const response = await fetch(`/api/items/${editUuidInput}`, { // Adjust this URL to your API endpoint
      method: 'PUT', // or 'PATCH' depending on your API design
      headers: {
        'Content-Type': 'application/json',
        // Add any necessary authentication headers (e.g., 'Authorization': 'Bearer YOUR_TOKEN')
      },
      body: JSON.stringify(updatedData) // Send the updated data as JSON
    });

    // 2. Check if the API request was successful
    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
    }

    // 3. Parse the response (if your API sends back updated data or a success message)
    const result = await response.json();
    console.log('API update successful:', result);

    // 4. Update the local 'data' array (optional but good for UI consistency)
    /* TBD -TJS const entryIndex = data.findIndex(item => item.id === updatedUuid);
    if (entryIndex !== -1) {
      data[entryIndex] = { ...data[entryIndex], ...updatedData }; // Merge updated fields
      displayTable(data); // Re-display the table to reflect changes
    } */

    // 5. Hide the form and provide user feedback
    editFormContainer.style.display = "none";
    editForm.reset(); // Clear form fields
    callAWSapi(); // update User Interface with the latest data
    alert("Entry updated successfully!");

  } catch (error) {
    console.error('Error updating entry:', error);
    alert('Failed to update entry. Please try again. ' + error.message);
    // Optionally, re-enable the form fields or show a specific error message on the form
  }
});