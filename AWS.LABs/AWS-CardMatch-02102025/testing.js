//Part1 DNW
var d = new Date(); // for now
d.getHours(); // => 9
d.getMinutes(); // =>  30
d.getSeconds(); // => 51
let myVariable= d.getSeconds;
console.log("hello world")
console.log("MyVariable", myVariable)
//-------
//Part2 Worked but elapased time w/o variable
console.time("myTimer");
// Code to measure execution time
for (let i = 0; i < 1000000; i++) {
    // Some operation
}
console.timeEnd("myTimer");

  
//Part3   this actually works
function greeting(){ 
    console.log("Hey Geeks"); 
} 
let start = Date.now(); 
start=Date.now();
greeting(); 
for (let i = 0; i < 1000000000; i++) {
    // Some operation
}
// get the end time 
let end = Date.now(); 
  
// elapsed time in milliseconds 
let elapsed = (end - start)/1000;    
  
// converting milliseconds to seconds  
// by dividing 1000 
console.log(elapsed);