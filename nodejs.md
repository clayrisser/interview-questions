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
Write a function called `isArray(item)` that correctly detects a JavaScript array. The function will be used the following way.
```js
const obj = {};
const str = '';
const num = 0;
const array = [];
const nothing = null;

isArray(obj); // false
isArray(str); // false
isArray(num); // false
isArray(nothing); // false
isArray(array); // true
```

## Question 3
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

## Question 4
Write a function that demonstrates a closure

## Question 5
Write a function called `removeAccount` that removes the account with the matching email.
```
const acounts = [{
  email: 'email1@example.com',
  password: '123'
},
{
  email: 'email2@example.com',
  password: 'abc'
},
{
  email: 'email3@example.com',
  password: 'ABC'
}];

removeAccount(acounts, 'email1@example.com');
```

## Question 6
Create an event emitter that emits an event called `stop`. Also, create an event listener that listens for the stop event you just created. The following code will get you started.
```js
const events = require('events');
const eventEmitter = new events.EventEmitter();
```

## Question 7
Rewrite the following code without nesting the `setTimeout` functions so that the second timeout starts after the first timeout is finished.
```js
setTimeout(() => {
  console.log(1);
}, 2000);
setTimeout(() => {
  console.log(2);
}, 1000);
```

## Question 8
write a function called `findchars(string, char)` that finds the index of all the matching characters and returns them in an array. this function should be case insensitive. the function will be used the following way.
```
const str = 'the quick brown fox jumped over the lazy dog';

findchars(str, 'o'); // [12, 17, 27, 42]
```

## Question 9
write a javascript object constructor that instantiates `dog` with the properties `name` and `breed`. it should also have a method `bark`. below is an example of how `dog` will be used.

```js
const dog = new dog('fido', 'bulldog');
console.log("the dog's name is " + dog.name);
console.log("the dog's breed is " + dog.breed);
dog.bark(); // woof
```

## Question 10
write a nodejs file module that converts a string to uppercase. this module will be used the following way.
```js
const uppercase = require('./upper-case.js');
uppercase('hello, world!'); // hello, world!
```

## Question 11
write a function that demonstrates a closure
