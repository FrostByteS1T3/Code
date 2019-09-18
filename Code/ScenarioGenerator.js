// day array
var days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
// item array
var items = ['pizza', 'frisbee', 'chocolate', 'candy'];
// random number 1 to 10
var dollars = Math.floor(Math.random(10) * 10) + 1;
var quartervalue = (Math.floor(Math.random(10) * 10) + 1) * 0.25;
var quarterammount = quartervalue / 0.25;
var dimevalue = (Math.floor(Math.random() * 10) + 1) / 10;
var dimeammount = dimevalue * 10
var nickelvalue = (Math.floor(Math.random(10) * 10) + 1) / 20
var nickleammount = nickelvalue * 20
var day = days[(Math.floor(Math.random() * 7))];
var item = items[(Math.floor(Math.random() * 4))]
let price1 = quartervalue + dollars + dimevalue + nickelvalue;
var price = Math.round(price1 * 100) / 100
const coins = ['q', 'd', 'n']
let missing = coins[(Math.floor(Math.random() * 3))]
console.log(missing);
var text = `This ${day} I bought a ${item}, it cost me $${price} to purchase.`
console.log(text);
if (missing === 'q') {
  console.log(`If I paid with ${dollars} dollar bills, ${dimeammount} dimes, and ${nickleammount} nickels, how many quarters did I pay with? Answer: ${quarterammount}`);
  console.log(`${price} - ${dollars} - ${dimevalue} - ${nickelvalue} = ${quartervalue}`);
} else if (missing === 'd') {
  console.log(`If I paid with ${dollars} dollar bills, ${quarterammount} quarters, and ${nickleammount} nickels, how many dimes did I pay with? Answer: ${dimeammount}`);
  console.log(`${price} - ${dollars} - ${nickelvalue} - ${quartervalue} = ${dimevalue}`);
} else {
  console.log(`If I paid with ${dollars} dollar bills, ${dimeammount} dimes, and ${quarterammount} quarters, how many nickels did I pay with? Answer: ${nickleammount}`);
  console.log(`${price} - ${dollars} - ${dimevalue} - ${quartervalue} = ${nickelvalue}`);
}
