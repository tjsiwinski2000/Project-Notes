const AWS = require('aws-sdk');
const express = require('express');
const serverless = require('serverless-http');

const app = express();

const USERS_TABLE = process.env.USERS_TABLE; // Get table name from environment variable
const dynamoDb = new AWS.DynamoDB.DocumentClient();

app.use(express.json());

// Example route to get an item from DynamoDB
app.get('/users/:userId', async (req, res) => {
  const params = {
    TableName: USERS_TABLE,
    Key: {
      id: req.params.id,
    },
  };


  try {
    const { Item } = await dynamoDb.get(params).promise();
    if (Item) {
      res.json(Item);
    } else {
      res.status(404).json({ error: 'Item not found' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Could not retrieve item' });
  }
});

// Export the Express app wrapped by serverless-http
module.exports.handler = serverless(app);