async function callAwsApi() {
    try {
        const response = await fetch('https://497i5a1fgf.execute-api.us-east-1.amazonaws.com/dev/posts/all');
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.text(); // or use .json() if the response is JSON
        const resultString = data;

        console.log("API Response:", resultString);
        return resultString;

    } catch (error) {
        console.error("Error calling AWS API:", error);
        return null;
    }
}
console.log(callAwsApi());