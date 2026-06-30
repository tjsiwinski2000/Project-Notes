const s="i need a java script function to display this with line skips between numbered comments There are three species of zebra: the plains zebra, the Grévy's zebra, and the mountain zebra. They are easily recognized by their distinctive black-and-white striped coats, which act as a form of camouflage. The patterns of a zebra's stripes are unique to each individual, much like a human's fingerprints. Zebras communicate with one another through various sounds, including barks, brays, and snorts. A group of zebras is called a 'dazzle,' a name thought to be inspired by the way their stripes create a shimmering, confusing effect when they run together. Zebras are herbivores and spend a lot of their time grazing on grass and other plants. While a zebra's kick can be lethal to predators like lions, they are also able to run at speeds of up to 40 miles per hour.";

// const sentences=s.split(".")
// let returnfacts="";
// sentences.forEach((sentence) => {
//   returnfacts+=sentence+"<br>";
// });

const sentences = s.split(/\. /).map(str => str.trim()).filter(Boolean);

let returnfacts = "";
sentences.forEach((sentence, i) => {
  // Add back the period if missing
  if (!sentence.endsWith(".")) sentence += ".";
  returnfacts += `<strong>${i + 1}.</strong> ${sentence}<br><br>`;
});
console.log (returnfacts)
