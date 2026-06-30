const AWS = require('aws-sdk');
const TODO_TABLE = process.env.TODO_TABLE; // Get table name from environment variable
const dynamoDb = new AWS.DynamoDB.DocumentClient();

module.exports.deleteTodo=(event,context,callback) => {
    const params = {
      TableName: TODO_TABLE,
      Key : {
        userId: event.pathParameters.id
      },
    };

  dynamoDb.delete(params, (error,data) =>{
      if (error) {
          console.error(error);
          callback(new Error(error));
          return;
        }

      const response = {
        statusCode: 200,
        body: JSON.stringify({data: "Deletion Successful"})
      };
     callback(null, response)
  });
};