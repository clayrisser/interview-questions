# NodeJS Interview Questions

## Question 1
Write a function called `printObjectKeys(obj)` that prints an object's keys to the console. The function will be used the following way.
```js
const obj = {
  one: 1,
  two: 2,
  three: 3
};

printObjectKeys(obj); // one, two, three
```

## Question 2
Write a function called `findChars(string, char)` that finds the index of all the matching characters and returns them in an array.
This function should be case insensitive. The function will be used the following way.
```
const str = 'the quick brOwn fox jumped over the lazy dog';

findChars(str, 'o'); // [12, 17, 27, 42]
```

## Question 3
Write a function called `isArray(item)` that correctly detects a JavaScript array. The function will be used the following way.
```js
const obj = {};
const str = '';
const num = 0;
const array = [];

isArray(obj); // false
isArray(str); // false
isArray(num); // false
isArray(array); // true
```

## Question 4
Write a JavaScript object constructor that instantiates `Dog` with the properties `name` and `breed`. It should also have a method `bark`.
Below is an example of how `Dog` will be used.
```js
const dog = new Dog('Fido', 'Bulldog');
console.log("The dog's name is " + dog.name);
console.log("The dog's breed is " + dog.breed);
dog.bark(); // woof
```

## Question 5
NodeJS has a `setTimeout(callback, time)` function that takes a callback for its first
parameter and time in milliseconds for its second parameter. Below is an example of how
this function is used.
```js
setTimeout(() => {
  console.log('waited 5 seconds');
}, 5000);
```
Convert `setTimeout(callback, time)` into the promise `setTimeoutAsync(time)` so that it can be used the following way.
```js
setTimeoutAsync(5000).then(() => {
  console.log('waited 5 seconds');
});
```

## Question 6
Write a NodeJS file module that converts a string to upperCase. This module will be used the following way.
```js
const upperCase = require('./upper-case.js');
upperCase('Hello, world!'); // HELLO, WORLD!
```

## Question 7
Write express logic that sends `Hello, world!` as the body when a GET request is made to the route `/hello`.
```js
const express = require('express');

const port = 3000;
const app = express();

// your express route logic code goes here

app.listen(port, () => {
  console.log('listening on port ' + port);
});
```

## Question 8
Write a function that demonstrates a closure
