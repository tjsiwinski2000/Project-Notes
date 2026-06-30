/*
this works, commented out to work on date formatting.
console.log('start');
const s='[{"content": "updated 835pm", "createdAt": "2025-07-09T13:58:10.555798", "todo": "develop project plan ", "id": "639a86ed-2612-47ab-8f31-80a5cc7e0632", "updatedAt": "2025-07-11T01:37:01.509086", "author": "TJ"}, {"id": "e4073569-e065-4e9e-afbe-b0ae37e32049", "createdAt": "2025-07-11T02:18:07.928487", "todo": "show all todos on website"}, {"id": "a9bc82c2-deda-408d-9555-55e54a5dfaf4", "createdAt": "2025-07-11T03:03:08.867864", "todo": "0710-2025 mom and summer"}]';
const todos = JSON.parse(s);
const delimitor_cell="</td><td>";
todos.forEach(element => {
  let row="<tr><td>";
  row += element.id + delimitor_cell;
  row += element.todo + delimitor_cell;
  row += (element.author || 'N/A') +delimitor_cell;
  row += (element.createdAt || 'N/A') +delimitor_cell;
  row += (element.updatedAt || 'N/A') + "</td></tr>";
  console.log(row);
});*/

/* comment out to work on next formatting effort
function convertToShortDate(dateTimeString) {
  const date = new Date(dateTimeString);
  const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
  return date.toLocaleDateString('en-US', options);
}

const dateTimeString = "2025-07-09T13:58:10.555798";
const shortDate = convertToShortDate(dateTimeString);
console.log(shortDate); // Output: 07/09/2025 */

/* comment out to work on next formatting issue
let s="639a86ed-2612-47ab-8f31-80a5cc7e0632";
console.log(s.substring(0,8));
*/

/* comment out to work on next formatting issue
function createIDLink(idNumber) {
  // Create anchor element
  //const link = document.createElement('a');
  
  // Set link text
  link.textContent = 'ID: ' + idNumber;
  
  // Set link href
  link.href = '#';

  // Set click behavior
  link.onclick = function(event) {
    event.preventDefault(); // prevent default anchor behavior
    alert('Identification Number: ' + idNumber);
  };

  return link;
}
createIDLink('1234')
*/
const pi = 3.14159
let tableDataObject;
function showValue(){
  console.log(pi);
  tableDataObject='[{"content": "updated 835pm", "createdAt": "2025-07-09T13:58:10.555798", "todo": "develop project plan ", "id": "639a86ed-2612-47ab-8f31-80a5cc7e0632", "updatedAt": "2025-07-11T01:37:01.509086", "author": "TJ"}, {"id": "e4073569-e065-4e9e-afbe-b0ae37e32049", "createdAt": "2025-07-11T02:18:07.928487", "todo": "show all todos on website"}, {"id": "a9bc82c2-deda-408d-9555-55e54a5dfaf4", "createdAt": "2025-07-11T03:03:08.867864", "todo": "0710-2025 mom and summer"}]';
  console.log(tableDataObject);
  tableDataObject = JSON.parse(tableDataObject);
  console.log(typeof tableDataObject);
}
showValue();
console.log("done");