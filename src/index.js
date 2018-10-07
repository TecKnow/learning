// import React from "react";
// import ReactDOM from "react-dom";
import "./index.css";
// import { createStore } from "redux";
import expect from 'expect';
import deepFreeze from 'deep-freeze';
// import App from './App';
// import * as serviceWorker from './serviceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));

// // If you want your app to work offline and load faster, you can change
// // unregister() to register() below. Note this comes with some pitfalls.
// // Learn more about service workers: http://bit.ly/CRA-PWA
// serviceWorker.unregister();

const addCounter = (list) => {
	return [...list, 0];
};

const removeCounter = (list, index) =>{
	return [...list.slice(0, index), ...list.slice(index+1)];
};

const incrementCounter = (list, index) => {
	return [...list.slice(0, index), list[index]+1, ...list.slice(index+1)];
};

const testAddCounter = () => {
	const listBefore = [];
	const listAfter = [0];

	deepFreeze(listBefore);
	expect(
		addCounter(listBefore)).toEqual(listAfter);
};

const testRemoveCounter = () => {
	const listBefore = [0, 10, 20];
	const listAfter = [0, 20];

	deepFreeze(listBefore);

	expect(removeCounter(listBefore, 1)).toEqual(listAfter);
};

const testIncrementCounter = () => {
	const listBefore = [0, 10,20];
	const listAfter = [0, 11, 20];

	deepFreeze(listBefore);

	expect(incrementCounter(listBefore, 1)).toEqual(listAfter);
};

testAddCounter();
testRemoveCounter();
testIncrementCounter();
console.log("All tests passed");