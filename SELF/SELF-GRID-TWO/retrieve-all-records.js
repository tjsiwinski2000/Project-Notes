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
